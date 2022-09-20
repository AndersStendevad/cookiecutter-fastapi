"""Conftest file for all fixtures"""

import pytest
from click.testing import CliRunner
from fastapi.testclient import TestClient
from {{cookiecutter.package_name}}.api import app


@pytest.fixture
def runner():
    return CliRunner()


@pytest.fixture(scope="session")
def client():
    return TestClient(app)
