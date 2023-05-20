#!/usr/bin/env bash

set -e
set -x

mypy app
black app --check
isort --check-only app
flake8 app
