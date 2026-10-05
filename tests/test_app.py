from http import HTTPStatus

from fastapi.testclient import TestClient


def test_root_deve_retornar_ola_mundo(client: TestClient):
    """
    Esse teste tem 3 etapas (AAA)
    - A: Arrange - Arranjo (Organizar)
    - A: Act - Ação
    - A: Assert - Afirmação
    1. Arrange: Criar o cliente de teste
    2. Act: Fazer a requisição GET para a rota raiz
    3. Assert: Verificar se a resposta é igual a {'message': 'Ola mundo!'}
    """
    response = client.get('/')
    assert response.status_code == HTTPStatus.OK  # Assert
    assert response.json() == {'message': 'teste'}  # Assert


def test_create_user(client: TestClient):
    """
    teste se retorna um user
    """
    response = client.post(
        '/users/',
        json={
            'username': 'gracieli',
            'email': 'gracieli@email.com',
            'password': '123456',
        },
    )

    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        'id': 1,
        'username': 'gracieli',
        'email': 'gracieli@email.com',
    }


def test_read_users(client: TestClient):
    response = client.get('/users/')
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'users': [
            {
                'id': 1,
                'username': 'gracieli',
                'email': 'gracieli@email.com',
            }
        ]
    }


def test_get_user(client):
    client.post(
        '/users/',
        json={
            'username': 'gracieli',
            'email': 'gracieli@email.com',
            'password': '123456',
        },
    )

    response = client.get('/users/1')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'id': 1,
        'username': 'gracieli',
        'email': 'gracieli@email.com',
    }


def test_get_user_not_found(client):
    response = client.get('/users/999')

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'User not found'}


def test_update_user(client: TestClient):
    response = client.put(
        '/users/1',
        json={
            'username': 'bob',
            'email': 'bob@example.com',
            'password': 'secret',
        },
    )
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'id': 1,
        'email': 'bob@example.com',
        'username': 'bob',
    }


def test_update_user_should_return_not_found__exercicio(client: TestClient):
    response = client.put(
        '/users/666',
        json={
            'username': 'bob',
            'email': 'bob@example.com',
            'password': 'mynewpassword',
        },
    )
    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'Usuário não encontrado'}


def test_delete_user(client: TestClient):
    response = client.delete('/users/1')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'Usuario deletado'}


def test_delete_user_should_return_not_found__exercicio(client: TestClient):
    response = client.delete('/users/555')

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'Usuário não encontrado'}
