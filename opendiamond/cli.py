#
# The OpenDiamond Platform for Interactive Search
#
# SPDX-FileCopyrightText: 2021 Carnegie Mellon University
# SPDX-License-Identifier: EPL-1.0
#

import click
from click_plugins import with_plugins
from pkg_resources import iter_entry_points

from opendiamond.console.options import CONTEXT_SETTINGS


@with_plugins(iter_entry_points("opendiamond.cli_plugins"))
@click.group(context_settings=CONTEXT_SETTINGS)
def cli():
    """Commandline interface for manipulating and validating OpenDiamond scopes."""
