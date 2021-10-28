[//]: <> SPDX-FileCopyrightText: 2021 Carnegie Mellon University
[//]: <> SPDX-License-Identifier: CC0-1.0

# Opendiamond-scope

Library and tools for manipulating OpenDiamond search scopes.


# Building from source

Build depends on SWIG and OpenSSL to build the M2Crypto wheels.

    sudo apt install swig libssl-dev

    poetry install
    poetry run opendiamond-scope -h
