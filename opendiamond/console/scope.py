#
# The OpenDiamond Platform for Interactive Search
#
# SPDX-FileCopyrightText: 2021 Carnegie Mellon University
# SPDX-License-Identifier: EPL-1.0
#

import click


@click.command()
def scope():
    """Test CLI scope plugin"""
    print("Hello Scope")
