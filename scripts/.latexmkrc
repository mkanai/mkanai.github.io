#!/usr/bin/env perl
$latex         = 'pdflatex -src-specials -shell-escape -interaction=nonstopmode %O %S';
$biber         = 'biber --input-directory ../_bibliography --bblencoding=utf8 -u -U --output-safechars %O %B';
$clean_ext     = 'synctex.gz synctex.gz(busy) run.xml tex.bak bbl bcf fdb_latexmk run tdo %R-blx.bib %R.abbr.bib xtex'; # http://tex.stackexchange.com/questions/83341/clean-bbl-files-with-latexmk-c

