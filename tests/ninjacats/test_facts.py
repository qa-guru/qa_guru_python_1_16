import requests
from pytest_voluptuous import S

from schemas.facts import facts
from utils.sessions import cats


def test_facts_count():
    """
    1. get https://catfact.ninja/facts?limit=2
    2. asserts
    """
    limit = 2

    response = requests.get("https://catfact.ninja/facts", params={"limit": limit})

    assert len(response.json()['data']) == limit


def test_facts_count_v2():
    """
    1. get https://catfact.ninja/facts?limit=2
    2. asserts
    """
    limit = 2

    response = cats().get("/facts", params={"limit": limit})

    assert len(response.json()['data']) == limit


def test_facts_schema_validation():
    """
    1. get https://catfact.ninja/facts?limit=2
    2. asserts
    """
    limit = 2

    response = requests.get("https://catfact.ninja/facts", params={"limit": limit})

    assert response.status_code == 200
    assert S(facts) == response.json()
