#!/usr/bin/env nix-shell
#!nix-shell -i python3.10 -p python310Packages.ortools

from typing import Dict, Tuple, List, Any
from read_input import readInput
from block import Block
from optimize import optimize
from output import printGrid

blocks = readInput()

bls = []
vorls = []

for bs in blocks:
    for b in bs:
        bls.append(b)
        if b.type == "Vorlesung":
            vorls.append(b)

by_module: Dict[str, List[List[Block]]] = {}

for bs in blocks:
    for b in bs:
        if b.course not in by_module:
            by_module[b.course] = [[], []]

        if b.type == "Übung":
            by_module[b.course][1].append(b)
        else:
            by_module[b.course][0].append(b)


# Vorfestgelegt
predet = {"SwT":("Montag", 4)}

# frei halten
blocked = {("Freitag", 1)}

uebs = optimize(by_module, vorls, blocked, predet)
printGrid(uebs + vorls, False)
