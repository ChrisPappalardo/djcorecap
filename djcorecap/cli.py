# -*- coding: utf-8 -*-

'''
cli
---

console script for djcorecap.
'''


import click
import sys


@click.command()
def main(args=None):
    '''
    djcorecap command line interface
    '''

    click.echo("update djcorecap.cli.main")
    return 0


def entry_point():
    '''
    required to make setuptools and click play nicely (context object)
    '''

    return sys.exit(main())  # add obj={} to create in context


if __name__ == "__main__":
    entry_point()
