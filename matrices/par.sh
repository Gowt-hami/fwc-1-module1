#!/bin/bash
cd /sdcard/mgowthani/matrices
texfot pdflatex mat.tex
termux-open mat.pdf
cd /sdcard/mgowthani/matrices
python3 par.py
