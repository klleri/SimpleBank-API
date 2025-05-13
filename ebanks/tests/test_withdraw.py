def test_withdraw_flows(client):
    # Reset state
    client.post('/reset')
    
    # withdraw from missing account
    resp = client.post('/event', json={"type":"withdraw","origin":"200","amount":10})
    assert resp.status_code == 404
    assert resp.get_data(as_text=True) == '0'
    
    # deposit and then withdraw
    client.post('/event', json={"type":"deposit","destination":"100","amount":20})
    resp = client.post('/event', json={"type":"withdraw","origin":"100","amount":5})
    assert resp.status_code == 201
    assert resp.json == {"origin": {"id":"100","balance":15}}
