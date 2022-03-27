# make\_stundenplan.py

Build a Stundenplan from a list of lecture and exercise times.

## Input definition

Enter the list as csv per stdin:

- first line: comma-separated list of important module names
- every line thereafter: comma-separated list of
  - module name
  - either "Vorlesung" or "Übung"
  - day of the week (German, uppercase)
  - time of day: [0-9]. DS
  - location

### Sample input

`course_list.csv`:

```csv
Prog,MMI
Prog,Vorlesung,Freitag,4. DS,Loc1
Prog,Übung,Mittwoch,1. DS,Loc2
Prog,Übung,Mittwoch,2. DS,Loc3
MMI,Vorlesung,Dienstag,6. DS,Loc4
```

## Running

```sh
./make_stundenplan.py < course_list.csv
```
