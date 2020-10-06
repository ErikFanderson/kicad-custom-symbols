#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Erik Anderson
# Email: erik.francis.anderson@gmail.com
# Date: 10/06/2020
"""Docstring for module default"""

# Imports - standard library

# Imports - 3rd party packages

# Imports - local source
import os, sys

dir_path = os.path.dirname(os.path.realpath(__file__))

if __name__ == '__main__':
    csv = ["PGA208"]
    csv.append("Pin, Name, Side")
    names = [
        "B2", "D3", "B1", "E4", "C2", "E3", "C1", "F4", "D2", "F3", "D1", "G4",
        "E2", "G3", "E1", "H3", "F2", "H4", "F1", "H2", "G2", "J2", "G1", "J3",
        "H1", "J4", "J1", "K2", "K1", "K3", "L1", "K4", "M1", "L2", "N1", "L3",
        "M2", "L4", "P1", "M3", "N2", "M4", "R1", "N3", "P2", "N4", "T1", "P3",
        "R2", "P4", "U1", "R3", "T2", "R4", "U2", "P5", "T3", "R5", "U3", "P6",
        "T4", "R6", "U4", "P7", "T5", "R7", "U5", "R8", "T6", "P8", "U6", "T8",
        "T7", "T9", "U7", "R9", "U8", "P9", "U9", "T10", "U10", "R10", "U11",
        "P10", "U12", "T11", "U13", "R11", "T12", "P11", "U14", "R12", "T13",
        "P12", "U15", "R13", "T14", "P13", "U16", "R14", "T15", "P14", "U17",
        "R15", "T16", "P15", "T17", "N14", "R16", "N15", "R17", "M14", "P16",
        "M15", "P17", "L14", "N16", "L15", "N17", "K15", "M16", "K14", "M17",
        "K16", "L16", "J16", "L17", "J15", "K17", "J14", "J17", "H16", "H17",
        "H15", "G17", "H14", "F17", "G16", "E17", "G15", "F16", "G14", "D17",
        "F15", "E16", "F14", "C17", "E15", "D16", "E14", "B17", "D15", "C16",
        "D14", "A17", "C15", "B16", "C14", "A16", "D13", "B15", "C13", "A15",
        "D12", "B14", "C12", "A14", "D11", "B13", "C11", "A13", "C10", "B12",
        "D10", "A12", "B10", "B11", "B9", "A11", "C9", "A10", "D9", "A9", "B8",
        "A8", "C8", "A7", "D8", "A6", "B7", "A5", "C7", "B6", "D7", "A4", "C6",
        "B5", "D6", "A3", "C5", "B4", "D5", "A2", "C4", "B3", "D4", "A1", "C3"
    ]
    # check for 208 connections
    if len(names) != 208:
        sys.exit("ERROR: Length of names array is not equal to 208")
    # check for duplicates
    names_dict = {}
    for i, n in enumerate(names):
        if n in names_dict.values():
            sys.exit("ERROR: Duplicate pin names supplied")
        names_dict[str(i)] = names[i] 

    for i in range(208):
        string = f"{names_dict[str(i)]}, {names_dict[str(i)]}"
        # Right and Left are switched from package to pinout for PGA20809
        if (i + 1) < 53:
            string += ", left"
        elif (i + 1) < 105:
            string += ", top"
        elif (i + 1) < 157:
            string += ", right"
        else:
            string += ", bottom"
        csv.append(string)

    with open(os.path.join(dir_path, "PGA208.csv"), "w") as fp:
        fp.write("\n".join(csv))
    print("PGA208.csv successfully created")
