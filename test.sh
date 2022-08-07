#!/usr/bin/bash

export DEV=TEST
cd ./tests/
python3 tests.py
export DEV=DEV

