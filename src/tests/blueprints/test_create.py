
from unittest.mock import patch
from src.errors.errors import EmailAlreadyBlacklisted, InvalidParams

def test_create_blacklist_entry_success(client):
    with patch('src.commands.create_blacklist.CreateBlacklist.execute') as mock_execute:
        mock_execute.return_value = {
            'message': 'Blacklist entry successfully registered.',
            'data': {
                'email': 'test@test.com',
                'app_uuid': '123e4567-e89b-12d3-a456-426614174000',
                'blocked_reason': 'Spamming',
                'ip_address': '0.0.0.0'
            }
        }

        response = client.post(
            "/blacklists",
            headers={"Authorization": "Bearer token-super-secreto"},
            json={
                "email": "test@test.com",
                "app_uuid": "123e4567-e89b-12d3-a456-426614174000",
                "blocked_reason": "Spamming",
                "ip_address": "0.0.0.0"
            }
        )

        assert response.status_code == 201
        assert response.get_json() == mock_execute.return_value
        mock_execute.assert_called_once()

def test_create_blacklist_entry_invalid_params(client):
    with patch('src.commands.create_blacklist.CreateBlacklist.execute') as mock_execute:
        mock_execute.side_effect = InvalidParams('Invalid parameters.')

        response = client.post(
            "/blacklists",
            headers={"Authorization": "Bearer token-super-secreto"},
            json={
                "a": "test.com",
                "aaa": "123e4567-e89b-12d3-a456-426614174000",
                "blocked_reason": "Spamming",
                "ip_address": "0.0.0.1"
            }
        )

        assert response.status_code == 400
        assert response.data.decode() == 'Invalid parameters.'

def test_create_blacklist_entry_already_blacklisted(client):
    with patch('src.commands.create_blacklist.CreateBlacklist.execute') as mock_execute:
        mock_execute.side_effect = EmailAlreadyBlacklisted('The email is already blacklisted.')

        response = client.post(
            "/blacklists",
            headers={"Authorization": "Bearer token-super-secreto"},
            json={
                "email": "test@test.com",
                "app_uuid": "123e4567-e89b-12d3-a456-426614174000",
                "blocked_reason": "Spamming",
                "ip_address": "0.0.0.0"
            }
        )

        assert response.status_code == 409
        assert response.data.decode() == 'The email is already blacklisted.'

def test_create_blacklist_email_invalid(client):
    with patch('src.decorators.auth.token_required') as mock_verify_token, \
         patch('src.commands.create_blacklist.CreateBlacklist.execute') as mock_execute:
        # Configura el mock para que simule una excepción de token inválido
        mock_verify_token.side_effect = Exception('Token inválido o ausente.')

        response = client.post(
            "/blacklists",
            headers={"Authorization ": "Bearer token-super-secreto"},  # Cabecera incorrecta
            json={
                "email": "test.com",  # Email inválido
                "app_uuid": "123e4567-e89b-12d3-a456-426614174000",
                "blocked_reason": "Spamming",
                "ip_address": "0.0.0.1"
            }
        )

        assert response.status_code == 401
        mock_verify_token.assert_not_called()  # Puede que no se llame si la cabecera es incorrecta
        mock_execute.assert_not_called()
