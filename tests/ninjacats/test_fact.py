import requests
from pytest_voluptuous import S
from voluptuous import Schema


def test_fact_fields_validation():
    response = requests.get("https://catfact.ninja/fact")

    assert isinstance(response.json()['fact'], int)
    assert isinstance(response.json()['length'], int)


def test_fact_schema_validation():
    schema = Schema({
        'fact': int,
        "length": int
    })

    response = requests.get("https://catfact.ninja/fact")

    assert S(schema) == response.json()
