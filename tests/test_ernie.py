import pytest

from ernie.ernie import app


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


def test_ernie_results(client):
    resp = client.post(
        "/ask",
        data={
            "prompt": "You might wonder what a city kid like me is doing out here in the [MASK]?"
        },
    )
    assert b"you might wonder what a city kid" in resp.data
