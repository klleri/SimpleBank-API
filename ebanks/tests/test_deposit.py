def test_deposit_flow(client):
    # Reset state
    client.post('/reset')

    # Create account with initial deposit
    resp = client.post('/event', json={"type": "deposit", "destination": "100", "amount": 10})
    assert resp.status_code == 201
    assert resp.json == {"destination": {"id": "100", "balance": 10}}

    # Check balance (plaintext)
    resp = client.get('/balance?account_id=100')
    assert resp.status_code == 200
    assert resp.get_data(as_text=True) == '10'