from http import HTTPStatus

from fastapi.testclient import TestClient

from fast_zero.app import app


def test_root_deve_retornar_ola_mundo():
    """
    Esse teste tem 3 etapas (AAA)
    - A: Arrange - Arranjo (Organizar)
    - A: Act - Ação
    - A: Assert - Afirmação
    1. Arrange: Criar o cliente de teste
    2. Act: Fazer a requisição GET para a rota raiz
    3. Assert: Verificar se a resposta é igual a {'message': 'Ola mundo!'}
    """
    client = TestClient(app)
    response = client.get('/')
    assert response.status_code == HTTPStatus.OK  # Assert
    assert response.json() == {'message': 'Ola mundo!'}  # Assert
