#
#  The OpenDiamond Platform for Interactive Search
#
# SPDX-FileCopyrightText: 2021 Carnegie Mellon University
# SPDX-License-Identifier: EPL-1.0
#

from click.testing import CliRunner

from opendiamond.console.scope_generate import generate

from .test_cookies import KeyPair


def test_required_servers_option():
    runner = CliRunner()

    result = runner.invoke(generate, [])
    assert result.exit_code == 2
    assert "Missing option" in result.output


def test_keyfile_option():
    runner = CliRunner()

    opts = ["-s", "diamond.test", "-k", "key.pem", "-v"]

    with runner.isolated_filesystem():
        # try with non-existing key file
        result = runner.invoke(generate, opts)
        assert result.exit_code == 2
        assert "No such file" in result.output

        # try with invalid key file
        with open("key.pem", "w") as keyfile:
            keyfile.write("")

        result = runner.invoke(generate, opts)
        assert result.exit_code == 1
        assert result.exception
        assert "Unable to read private key" in str(result.exception)

        # try with valid key file
        with open("key.pem", "w") as keyfile:
            keyfile.write(KeyPair.valid[0].key)

        result = runner.invoke(generate, opts)
        assert result.exit_code == 0
        assert "Servers: diamond.test" in result.output
