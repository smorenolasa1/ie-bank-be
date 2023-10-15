from iebank_api import app
import pytest

def test_get_accounts(testing_client):
    """
    GIVEN a Flask application
    WHEN the '/accounts' page is requested (GET)
    THEN check the response is valid
    """
    response = testing_client.get('/accounts')
    assert response.status_code == 200

def test_dummy_wrong_path():
    """
    GIVEN a Flask application
    WHEN the '/wrong_path' page is requested (GET)
    THEN check the response is valid
    """
    with app.test_client() as client:
        response = client.get('/wrong_path')
        assert response.status_code == 404

def test_create_account(testing_client):
    """
    GIVEN a Flask application
    WHEN the '/accounts' page is posted to (POST)
    THEN check the response is valid
    """
    response = testing_client.post('/accounts', json={'name': 'John Doe', 'currency': '€', 'country': 'Spain'})
    assert response.status_code == 200

def test_create_and_retrieve_account_different_description(testing_client):
    response = testing_client.post('/accounts', json={'name': 'Alice Smith', 'currency': '$', 'country': 'United States'})
    assert response.status_code == 200

def test_delete_account_with_custom_data(testing_client):
    """
    GIVEN a Flask application
    WHEN the '/accounts' page is deleted (DELETE)
    THEN verify that the response is successful
    """
    response = testing_client.post(
        "/accounts", json={'name': 'Bob Johnson', 'currency': '£', 'country': 'United Kingdom'}
    )

    response = testing_client.delete("/accounts/1")
    assert response.status_code == 200

def test_get_account_by_id_updated_data(testing_client):
    """
    GIVEN a Flask application
    WHEN the '/accounts' page is requested (GET)
    THEN ensure that the response is valid
    """
    response = testing_client.post(
        "/accounts", json={'name': 'Eve Brown', 'currency': '€', 'country': 'France'}
    )

    response = testing_client.get("/accounts/1")
    assert response.status_code == 200

def update_account_by_id_modified_data(testing_client):
    """
    GIVEN a Flask application
    WHEN the '/accounts' page is updated (PUT)
    THEN validate that the response is successful
    """
    response = testing_client.post(
        "/accounts", json={'name': 'Charlie Wilson', 'currency': '¥', 'country': 'Japan'}
    )
    response = testing_client.put("/accounts/1", json={"name": "David Lee"})
    assert response.status_code == 200
