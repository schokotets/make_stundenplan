from days import days, days_rev
from colors import colors

def printList(blocks, hideÜbungen, compact):
    # sort blocks
    def sortfn(block: Block):
        return (
            str(days[block.day])
            + str(block.time)
            + ("V" if block.type == "Vorlesung" else "Ü")
            + block.course
        )

    for bs in blocks:
        bs.sort(key=sortfn)

    for i, bs in enumerate(blocks):
        if not compact:
            print()
            print(days_rev[i])
            print("=" * len(days_rev[i]))
        lasttime = -1
        for b in bs:
            if b.type == "Übung" and hideÜbungen:
                continue
            if lasttime != b.time:
                if not compact:
                    print()
                lasttime = b.time
            print(b.oneline(not hideÜbungen))


def printCal(blocks, hideÜbungen, compact):
    # sort blocks
    def sortfn(block: Block):
        return (
            str(days[block.day])
            + str(block.time)
            + ("V" if block.type == "Vorlesung" else "Ü")
            + block.course
        )

    for bs in blocks:
        bs.sort(key=sortfn)

    for i, bs in enumerate(blocks):
        if not compact:
            print()
            print(days_rev[i])
            print("=" * len(days_rev[i]))
        lasttime = -1
        for b in bs:
            if b.type == "Übung" and hideÜbungen:
                continue
            if lasttime != b.time:
                if not compact:
                    print()
                lasttime = b.time
                print(f"{b.time}. DS")
                print(f"-----")
            print(b.multiline(not hideÜbungen))


def printGrid(bls, hideÜbungen):

    print("┌─┬" + ("─" * 6 + "┬") * 5 + ("─" * 6 + "┐"))
    print("│h", end="│ ")
    for day in days:
        print(day[:3], end="  │ ")
    print()
    print("├─┼" + ("─" * 6 + "┼") * 5 + ("─" * 6 + "┤"))

    grid = [
        [[], [], [], [], [], []],
        [[], [], [], [], [], []],
        [[], [], [], [], [], []],
        [[], [], [], [], [], []],
        [[], [], [], [], [], []],
        [[], [], [], [], [], []],
        [[], [], [], [], [], []],
        [[], [], [], [], [], []],
    ]

    for b in bls:
        if b.type == "Übung" and hideÜbungen:
            continue
        grid[b.time][days[b.day]].append(b)
        grid[b.time][days[b.day]].sort(key=lambda b: f"{not b.important}{b.type}")

    for hour, hrow in enumerate(grid):
        print("│" + str(hour), end="│")
        maxlen = max(max(map(len, hrow)), 1)
        for r in range(maxlen):
            if r != 0:
                print("│ │", end="")
            for dslot in hrow:
                if dslot and len(dslot) > r:
                    b = dslot[r]
                    print(b.courseonly(), end="│")
                else:
                    print("      ", end="│")
            print()
        if hour < len(grid) - 1:
            print("├─┼" + ("─" * 6 + "┼") * 5 + ("─" * 6 + "┤"))
        else:
            print("└─┴" + ("─" * 6 + "┴") * 5 + ("─" * 6 + "┘"))
