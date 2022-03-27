from dataclasses import dataclass
from colors import colors

FgBlack = "\033[30m"
FgGray = "\033[38;2;90;90;90m"
BgWhite = "\033[47m"

Color_Reset = "\033[0m"

Bright = "\033[1m"
Cross = "\033[9m"
Italic = "\033[3m"
Underline = "\033[4m"

@dataclass
class Block:
    """Klasse für einen Übungs- / Vorlesungstermin."""

    course: str
    type: str
    day: str
    time: int
    loc: str
    color: int
    important: bool
    printed: bool = False

    def oneline(block, highlightVL):
        c = (
            Bright + FgBlack + BgWhite
            if block.type == "Vorlesung" and highlightVL
            else Color_Reset
        )
        return f"{c}{block.day[:2]} {block.time}. [{block.type[:1]}] {colors[block.color]}{block.course}{Color_Reset}{c} ({block.loc}){Color_Reset}"

    def multiline(block, highlightVL):
        c = (
            Bright + FgBlack + BgWhite
            if block.type == "Vorlesung" and highlightVL
            else Color_Reset
        )
        return f"{c}[{block.type[:1]}] {colors[block.color]}{block.course}{Color_Reset}{c} ({block.loc}){Color_Reset}"

    def courseonly(block):
        pad = " " * (4 - len(block.course))

        c = FgBlack + BgWhite # if block.type == "Vorlesung" else Color_Reset
        if not block.important:
            c += Italic + FgGray
        elif block.type == "Vorlesung":
            c = Bright + c
        c += colors[block.color]

        icon = " "

        if block.type == "Vorlesung":
            if block.important:
                icon = Underline + "🥥"
            else:
                icon = Underline + "🥝"
        else:
            if block.important:
                icon = "🧀"
            else:
                icon = "🥒"

        return f"{c}{icon}{block.course}{Color_Reset}{pad}"
