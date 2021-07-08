#!/usr/bin/env python
import argparse
import io
import jinja2
import os
import string
import subprocess
import sys
import yaml

from collections import defaultdict

BASEDIR = os.path.dirname(__file__)
LATEX_TEMPLATE = 'CV_template.tex'

latex_jinja_env = jinja2.Environment(
    block_start_string = '\BLOCK{',
    block_end_string = '}',
    variable_start_string = '\VAR{',
    variable_end_string = '}',
    comment_start_string = '\#{',
    comment_end_string = '}',
    line_statement_prefix = '%%',
    line_comment_prefix = '%#',
    trim_blocks = True,
    autoescape = False,
    loader = jinja2.FileSystemLoader(BASEDIR)
)
template = latex_jinja_env.get_template(LATEX_TEMPLATE)


def load_yaml(file, basedir=None):
    if basedir is not None:
        file = os.path.join(basedir, file)
    with io.open(file, 'r', encoding='utf-8') as f:
        yml = yaml.load(f, Loader=yaml.FullLoader)
    return yml


def main(args):
    config = load_yaml(args.config)

    if args.private is not None:
        private = load_yaml(args.private)
    else:
        private = defaultdict(None)

    data = defaultdict(None)
    for section in ['education', 'research', 'certification']:
        fname = section + '.yml'
        if os.path.exists(fname):
            data[section] = load_yaml(fname, args.datadir)
        else:
            data[section] = defaultdict(None)

    out_fname = args.out + '.xtex'
    with io.open(out_fname, 'w', encoding='utf-8') as f:
        f.write(template.render(config = config,
                                private = private,
                                data = data,
                                ascii_uppercase = string.ascii_uppercase))

    cmd = ['latexmk', '-cd', '-f', '-pdf', out_fname]
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = p.communicate()
    print(stdout)
    print(stderr)

    # cleanup
    cmd = ['latexmk', '-c', out_fname]
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = p.communicate()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--out', default='CV', type=str)
    parser.add_argument('--config', default='../_config.yml', type=str)
    parser.add_argument('--private', default=None, type=str)
    parser.add_argument('--datadir', default='../_data', type=str)
    args = parser.parse_args()

    args.config = os.path.join(BASEDIR, args.config)
    args.datadir = os.path.join(BASEDIR, args.datadir)

    main(args)

