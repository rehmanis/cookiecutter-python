#!/usr/bin/env python
import os
import shutil

PROJ_DIR = os.getcwd()


def setup_docs():

    # remove the docs folder not used
    shutil.move(
        os.path.join(
            PROJ_DIR, "doc_options", "{{ cookiecutter.doc_type }}", "docs"
        ),
        PROJ_DIR,
    )
    # move the mkdocs.yml to root if doctype is mkdocs
    if "{{ cookiecutter.doc_type }}" == "mkdocs":
        shutil.move(os.path.join(PROJ_DIR, "docs", "mkdocs.yml"), PROJ_DIR)
    # remove the doc_options folder
    shutil.rmtree(os.path.join(PROJ_DIR, "doc_options"))


if __name__ == "__main__":
    setup_docs()
