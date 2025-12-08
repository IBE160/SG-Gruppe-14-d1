import pytest
from fastapi.testclient import TestClient
from unittest.mock import patch, MagicMock
from gotrue.errors import AuthApiError
from main import app

client = TestClient(app)

@pytest.fixture
def mock_supabase_client():
    with patch('core.supabase_client.get_supabase_client') as mock_get_client:
        mock_client = MagicMock()
        mock_get_client.return_value = mock_client
        yield mock_client

def test_register_user_success(mock_supabase_client):
    # Arrange
    mock_user = MagicMock()
    mock_user.id = "some-uuid"
    mock_session = MagicMock()
    mock_session.access_token = "fake-jwt-token"
    
    mock_signup_response = MagicMock()
    mock_signup_response.user = mock_user
    mock_signup_response.session = mock_session

    mock_supabase_client.auth.sign_up.return_value = mock_signup_response
    mock_supabase_client.table.return_value.insert.return_value.execute.return_value = None

    # Act
    response = client.post(
        "/api/v1/auth/register",
        json={"name": "Test User", "email": "test@example.com", "password": "a-strong-password"}
    )

    # Assert
    assert response.status_code == 200
    data = response.json()
    assert data["access_token"] == "fake-jwt-token"
    assert data["token_type"] == "bearer"
    
    # Check that supabase functions were called correctly
    mock_supabase_client.auth.sign_up.assert_called_once_with({
        "email": "test@example.com",
        "password": "a-strong-password"
    })
    mock_supabase_client.table.assert_called_once_with("profiles")
    mock_supabase_client.table().insert.assert_called_once_with({
        "id": "some-uuid",
        "name": "Test User"
    })


def test_register_user_already_exists(mock_supabase_client):
    # Arrange
    # Simulate the exception that Supabase client might raise
    mock_supabase_client.auth.sign_up.side_effect = AuthApiError(
        message="User already registered", 
        status_code=400
    )

    # Act
    response = client.post(
        "/api/v1/auth/register",
        json={"name": "Test User", "email": "test@example.com", "password": "a-strong-password"}
    )

    # Assert
    assert response.status_code == 400
    assert response.json() == {"detail": "Email already registered"}
