from http import HTTPStatus

from fastapi.testclient import TestClient

from fast_zero.app import app


def test_root_deve_retornar_ok_e_ola_mundo():  # (1)!
    client = TestClient(app)  # (2)!

    response = client.get('/')  # (3)!

    assert response.status_code == HTTPStatus.OK  # (4)!
    assert response.json() == {'message': 'Olá Mundo!'}  # (5)!
