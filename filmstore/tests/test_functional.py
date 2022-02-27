import pytest
from rest_framework.test import APIClient
from hypothesis import given, settings, strategies as st

pytestmark = pytest.mark.django_db

client = APIClient()


@settings(max_examples=10)
@given(full_name=st.text(min_size=1), birth_date=st.dates(), age=st.integers(), death_date=st.dates())
def test_functional_director(full_name, birth_date, age, death_date):
    response = client.post("/films/api/directors/", {
        "full_name": full_name,
        "birth_date": str(birth_date),
        "death_date": str(death_date),
        "age": age
    })
    assert response.status_code == 201
    assert response.data["full_name"] == full_name


@settings(max_examples=10)
@given(name=st.text(min_size=2))
def test_functional_genre(name):
    response = client.post("/films/api/genres/", {
        "name": name
    })
    assert response.status_code == 201
    assert response.data["name"] == name
