#
#  The OpenDiamond Platform for Interactive Search
#
# SPDX-FileCopyrightText: 2021 Carnegie Mellon University
# SPDX-License-Identifier: EPL-1.0
#

import pytest
from click.testing import CliRunner

from opendiamond.console.scope_generate import generate

from .test_cookies import KeyPair


# Test opendiamond-scope generate
def test_required_servers_option():
    runner = CliRunner()

    result = runner.invoke(generate, [])
    assert result.exit_code == 2
    assert "Missing option" in result.output


@pytest.fixture
def isolated_runner():
    runner = CliRunner()
    with runner.isolated_filesystem():
        yield runner


def test_keyfile_option(isolated_runner):
    # try with non-existing key file
    opts = ["-s", "diamond.test", "-k", "key.pem", "-v"]
    result = isolated_runner.invoke(generate, opts)
    assert result.exit_code == 2
    assert "No such file" in result.output


def test_invalid_keyfile_option(isolated_runner):
    # try with invalid key file
    opts = ["-s", "diamond.test", "-k", "key.pem", "-v"]
    with open("key.pem", "w") as keyfile:
        keyfile.write("")

    result = isolated_runner.invoke(generate, opts)
    assert result.exit_code == 1
    assert result.exception
    assert "Unable to read private key" in str(result.exception)


def test_valid_keyfile_option(isolated_runner):
    # try with valid key file
    opts = ["-s", "diamond.test", "-k", "key.pem", "-v"]
    with open("key.pem", "w") as keyfile:
        keyfile.write(KeyPair.valid[0].key)

    result = isolated_runner.invoke(generate, opts)
    assert result.exit_code == 0
    assert "Servers: diamond.test" in result.output
