import pytest


@pytest.fixture()
def headers_without_authorization():
    headers = {"Accept": "application/json",
               "Content-Type": "application/json"}
    return headers
