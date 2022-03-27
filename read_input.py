import sys

from days import days
from block import Block
from colors import colors

def readInput():
    blocks = [[], [], [], [], [], []]

    important = sys.stdin.readline()

    colormap = {}

    for line in sys.stdin:
        line = line.strip()
        parts = line.split(",")

        course = parts[0]

        if not course in colormap:
            colormap[course] = len(colormap) % len(colors)
        color = colormap[course]

        # TODO gerade / ungerade Wochen unterscheiden
        if parts[2] in days:
            blocks[days[parts[2]]].append(
                Block(
                    parts[0],
                    parts[1],
                    parts[2],
                    int(parts[3][0]),
                    parts[4],
                    color,
                    parts[0] in important,
                )
            )
        else:
            hour = int(parts[3][0]) if len(parts[3]) > 0 else 0
            blocks[-1].append(
                Block(
                    parts[0],
                    parts[1],
                    "unbekannt",
                    hour,
                    parts[4],
                    color,
                    parts[0] in important,
                )
            )

    return blocks
