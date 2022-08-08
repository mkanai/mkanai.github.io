#!/usr/bin/env python
import argparse
import io
import jinja2
import os
import string
import subprocess
import yaml
import numpy as np
import re
from pybtex.database import parse_file, Person

from collections import defaultdict

BASEDIR = os.path.dirname(__file__)
LATEX_TEMPLATE = "CV_template.tex"

latex_jinja_env = jinja2.Environment(
    block_start_string="\BLOCK{",
    block_end_string="}",
    variable_start_string="\VAR{",
    variable_end_string="}",
    comment_start_string="\#{",
    comment_end_string="}",
    line_statement_prefix="%%",
    line_comment_prefix="%#",
    trim_blocks=True,
    autoescape=False,
    loader=jinja2.FileSystemLoader(BASEDIR),
)
template = latex_jinja_env.get_template(LATEX_TEMPLATE)


def load_yaml(file, basedir=None):
    if basedir is not None:
        file = os.path.join(basedir, file)
    with io.open(file, "r", encoding="utf-8") as f:
        yml = yaml.load(f, Loader=yaml.FullLoader)
    return yml


def generate_new_bib(
    file,
    my_name_pat=re.compile("^\**Kanai, Masahiro"),
    max_first_authors=5,
    max_last_authors=5,
    required_bib_fields=set(["doi", "journal", "number", "pages", "year", "title", "volume", "keywords"]),
):
    abbr_person = Person("{...}")
    max_authors = max_first_authors + max_last_authors

    bib = parse_file(file)
    for key, entry in bib.entries.items():
        # drop unnecessary fields
        for field in set(entry.fields.keys()) - required_bib_fields:
            del entry.fields[field]

        authors = entry.persons["author"]
        if len(authors) <= max_authors:
            print(key, "Passed")
            continue
        # locate my name index
        idx = np.where([bool(my_name_pat.match(str(author))) for author in authors])[0]
        print(key, idx)

        if len(idx) != 1:
            raise ValueError()

        idx = idx[0]
        k = (len(authors) - max_last_authors - 1)
        if idx <= max_first_authors or idx >= k:
            # [0, 1, 2, ..., -2, -1]
            i = max_first_authors + (idx == max_first_authors)
            j = max_last_authors + (idx == k and k != max_first_authors)
            new_authors = authors[:i] + [abbr_person] + authors[-j:]
        else:
            # [0, 1, 2, ..., idx, ..., -2, -1]
            new_authors = (
                authors[:max_first_authors] + [abbr_person, authors[idx], abbr_person] + authors[-max_last_authors:]
            )
        print(new_authors)

        entry.persons["author"] = new_authors

    bib.to_file(os.path.join(BASEDIR, "CV.abbr.bib"))


def main(args):
    config = load_yaml(args.config)

    if args.private is not None:
        private = load_yaml(args.private)
    else:
        private = defaultdict(None)

    if args.abbreviate_authors:
        generate_new_bib(args.bib)

    data = defaultdict(None)
    for section in ["education", "research", "certification"]:
        fname = section + ".yml"
        if os.path.exists(fname):
            data[section] = load_yaml(fname, args.datadir)
        else:
            data[section] = defaultdict(None)

    out_fname = args.out + ".xtex"
    with io.open(out_fname, "w", encoding="utf-8") as f:
        f.write(
            template.render(
                config=config,
                private=private,
                abbreviate_authors=args.abbreviate_authors,
                data=data,
                ascii_uppercase=string.ascii_uppercase,
            )
        )

    cmd = ["latexmk", "-cd", "-f", "-pdf", out_fname]
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = p.communicate()
    print(stdout)
    print(stderr)

    # cleanup
    cmd = ["latexmk", "-c", out_fname]
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = p.communicate()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", default="CV", type=str)
    parser.add_argument("--config", default="../_config.yml", type=str)
    parser.add_argument("--private", default=None, type=str)
    parser.add_argument("--datadir", default="../_data", type=str)
    parser.add_argument("--bib", default="../_bibliography/publications.bib", type=str)
    parser.add_argument("--abbreviate-authors", action="store_true")
    args = parser.parse_args()

    args.config = os.path.join(BASEDIR, args.config)
    args.datadir = os.path.join(BASEDIR, args.datadir)
    args.bib = os.path.join(BASEDIR, args.bib)

    main(args)

