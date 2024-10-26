from unittest.mock import patch
from src.errors.errors import EmailNotFound, InvalidParams

def test_get_blacklist_info_success(client):
    with patch('src.commands.get_blacklist_info.GetBlacklistInfo.execute') as mock_execute:
        mock_execute.return_value = {
            'found': True,
            'reason': 'Spamming'
        }

        response = client.get(
            "/blacklists/test@example.com",
            headers={"Authorization": "Bearer token-super-secreto"}
        )

        assert response.status_code == 200
        assert response.get_json() == mock_execute.return_value
        mock_execute.assert_called_once()

def test_get_blacklist_info_not_found(client):
    with patch('src.commands.get_blacklist_info.GetBlacklistInfo.execute') as mock_execute:
        mock_execute.side_effect = EmailNotFound()

        response = client.get(
            "/blacklists/test@example.com",
            headers={"Authorization": "Bearer token-super-secreto"}
        )

        assert response.status_code == 404
        mock_execute.assert_called_once()

def test_get_blacklist_info_invalid_email(client):
    with patch('src.commands.get_blacklist_info.GetBlacklistInfo.execute') as mock_execute:
        mock_execute.side_effect = InvalidParams('Invalid email format.')

        response = client.get(
            "/blacklists/invalid_email_format",
            headers={"Authorization": "Bearer token-super-secreto"}
        )

        assert response.status_code == 500
        assert response.data.decode() == 'Invalid email format.'
        mock_execute.assert_called_once()

def test_get_blacklist_info_missing_token(client):
    response = client.get("/blacklists/test@example.com")
    assert response.status_code == 401
