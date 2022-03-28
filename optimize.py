from ortools.linear_solver import pywraplp
from days import days

def optimize(by_module, vorls, blocked, predet):
    # Solver
    # Create the mip solver with the SCIP backend.
    solver = pywraplp.Solver.CreateSolver("GLOP")

    # Variables
    vars: Dict[str,List[Tuple[Block,Any]]] = {}

    for course in by_module:
        vars[course] = []
        for i, ueb in enumerate(by_module[course][1]):

            # Übungen, deren Zeit ungewiss ist, nicht platzieren
            if ueb.time == 0:
                continue

            # Übungen gleich überspringen, die gleichzeitig mit einer VL stattfinden
            skip = False
            for vorl in vorls:
                if vorl.time == ueb.time and vorl.day == ueb.day:
                    skip = True
                    break
            if skip:
                continue

            # ob vorfestgelegt
            is_predet = ueb.course in predet and predet[ueb.course] == (ueb.day, ueb.time)

            is_blocked = False
            for day, time in blocked:
                if ueb.day == day and ueb.time == time:
                    is_blocked = True
                    break

            vars[course].append(
                (
                    ueb,
                    solver.IntVar(
                        1 if is_predet and not is_blocked else 0,
                        1 if not is_blocked else 0,
                        f"{course} #{i} {ueb.time} {ueb.day}",
                    ),
                )
            )

    # don't overlap with each other
    for day in days:
        for time in range(0, 8):
            bucket = []
            for course in vars:
                for u, v in vars[course]:
                    if u.time == time and u.day == day:
                        bucket.append(v)
            solver.Add(solver.Sum(bucket) <= 1)

    # Von jedem Modul wird eine Übung besucht
    for course in vars:
        if vars[course]:
            solver.Add(solver.Sum([x[1] for x in vars[course]]) == 1)

    # Ziel:
    # - möglichst früh
    # - möglichst nicht in 4. DS (Mittag)
    objective_terms = []
    for course in vars:
        for u, v in vars[course]:
            if u.time == 4:
                # noch besser als 7. DS
                coeff = 13
            elif u.time >= 5:
                coeff = u.time * 2
            else:
                coeff = u.time
            #if u.day == "Mittwoch":
            #    coeff = 8
            objective_terms.append(coeff * v)
    solver.Minimize(solver.Sum(objective_terms))

    # lösen
    status = solver.Solve()

    # Lösung (Auswahl an Übungen)
    choice = []

    # Print solution.
    if status == pywraplp.Solver.OPTIMAL or status == pywraplp.Solver.FEASIBLE:
        print(f"Kosten: {solver.Objective().Value()}\n")
        # Test if x[i,j] is 1 (with tolerance for floating point arithmetic).
        for course in vars:
            for u, v in vars[course]:
                if v.solution_value() > 0.5:
                    # print(v.name())
                    choice.append(u)
    else:
        print("No solution found.")

    return choice
