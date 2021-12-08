# SPDX-FileCopyrightText: 2021 Carnegie Mellon University
# SPDX-License-Identifier: 0BSD

# pyinvoke file for maintenance tasks

from invoke import task


@task
def update_dependencies(c):
    """Update python package dependencies"""
    c.run("poetry update")
    c.run("poetry run pre-commit autoupdate")
    c.run("poetry run nox -s test")
    c.run("git commit -m 'Update dependencies' poetry.lock .pre-commit-config.yaml")


@task
def release(c, part="patch"):
    """Tag and commit a new release version"""
    c.run(f"bump2version --tag {part}")
    c.run("poetry build")
    c.run("poetry run nox -s test")


@task
def publish(c):
    """Push tagged release and publish to PyPI"""
    # should fail if we're not release ready
    c.run("bump2version --dry-run release")

    c.run("poetry publish")
    c.run("bump2version --no-tag release")
    c.run("git push")
    c.run("git push --tags")
