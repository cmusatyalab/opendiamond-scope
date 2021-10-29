# SPDX-FileCopyrightText: 2021 Carnegie Mellon University
# SPDX-License-Identifier: CC0-1.0

import nox
import nox_poetry

nox.options.sessions = ["test-3.6", "test-3.7", "test-3.8", "test-3.9"]


@nox_poetry.session(python=["3.6", "3.7", "3.8", "3.9"])
def test(session):
    """Run the test suite."""
    session.install("pytest", ".")
    session.run("pytest", "tests/")


@nox.session(python=False)
def release(session):
    """Tag and commit a new release version"""
    part = session.posargs[0] if session.posargs else "patch"

    session.run("bump2version", "--tag", "--sign-tags", part)
    session.run("poetry", "build")
    session.notify("test")


@nox.session(python=False)
def publish(session):
    """Push tagged release and publish to PyPI"""
    session.run(
        "bump2version", "--dry-run", "release"
    )  # should fail if we're not release ready
    session.run("poetry", "publish")
    session.run("bump2version", "--no-tag", "release")
    session.run("git", "push")
    session.run("git", "push", "--tags")
