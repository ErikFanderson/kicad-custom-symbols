#!/usr/bin/env bash

# Generate CSVs
./PGA208/main.py
./samtec_qsh_qth/main.py

# Call kipart
kipart --overwrite --append --output zz_sockets.lib \
    PGA208/PGA208.csv

kipart --overwrite --append --output zz_samtec_qsh_qth.lib \
    samtec_qsh_qth/samtec_qsh_qth.csv
