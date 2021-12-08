# SPDX-FileCopyrightText: 2021 Carnegie Mellon University
# SPDX-License-Identifier: 0BSD

import nox
import nox_poetry

nox.options.sessions = ["test-3.6", "test-3.7", "test-3.8", "test-3.9"]


@nox_poetry.session(python=["3.6", "3.7", "3.8", "3.9"])
def test(session):
    """Run the test suite."""
    session.install("pytest", ".")
    session.run("pytest", "tests/")
