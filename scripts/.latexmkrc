#!/usr/bin/env perl
$latex         = 'pdflatex -src-specials -shell-escape -interaction=nonstopmode %O %S';
$biber         = 'biber --input_directory="../_bibliography" --bblencoding=utf8 -u -U --output_safechars %O %B';
$clean_ext     = 'synctex.gz synctex.gz(busy) run.xml tex.bak bbl bcf fdb_latexmk run tdo %R-blx.bib xtex'; # http://tex.stackexchange.com/questions/83341/clean-bbl-files-with-latexmk-c

