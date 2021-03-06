#!/usr/bin/env just --justfile

install:
  poetry install
  pre-commit install
  git config --bool flake8.strict true

requirements: install
  poetry export -f requirements.txt > requirements.txt

build tag='scaffold': requirements
  docker build -t {{tag}} .

run tag='scaffold': build
  docker run -d {{tag}}:latest

stop tag='scaffold':
  docker stop {{tag}}
  
build:
  python setup.py sdist bdist_wheel

clean:
  rm -rf build/
  rm -rf dist/
  rm -rf *.egg-info/
