import pytest
from rest_framework.test import APIClient


@pytest.mark.django_db
def test_nonexisting():
    factory = APIClient()
    response = factory.get('/rates/SUPBRO/')
    assert response.status_code == 404
