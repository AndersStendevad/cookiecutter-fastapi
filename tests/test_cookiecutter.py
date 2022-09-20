"""tests for cookiecutter"""

import pytest
import requests
import socket

from subprocess import run, Popen
from time import sleep

def test_bake_project(bake):
    """check if cookiecutter will even bake"""
    pass


def test_pytest_in_baked_project(bake, helper):
    """check pytest in baked project"""
    helper.install_package(".")
    helper.check_result(run("tox -e pytest", shell=True, capture_output=True))


def test_pre_commit_in_baked_project(bake, helper):
    """check pre-commit in baked project"""
    helper.check_result(
        run("pre-commit run --all-files", shell=True, capture_output=True)
    )


def test_docs(bake, helper):
    """check if docs are generated"""
    helper.check_result(run("tox -e docs", shell=True, capture_output=True))


def test_lint(bake, helper):
    """check lint in baked project"""
    helper.check_result(run("tox -e lint", shell=True, capture_output=True))

def test_fastapi(bake, helper):
    """check api in baked project"""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        if not s.connect_ex(('localhost', 8555)):
            raise Exception("fastapi 8555 port is in use!")
    p = Popen(["tox", "-e api"])
    sleep(20)
    requests.get("http://0.0.0.0:8555/health")
    p.terminate()
