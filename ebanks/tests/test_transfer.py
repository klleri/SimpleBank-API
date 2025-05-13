def test_transfer_flows(client):
    # Reset state
    client.post('/reset')
    
    # transfer from missing origin
    resp = client.post('/event', json={"type":"transfer","origin":"200","destination":"300","amount":5})
    assert resp.status_code == 404
    assert resp.get_data(as_text=True) == '0'
    
    # deposit then transfer
    client.post('/event', json={"type":"deposit","destination":"100","amount":15})
    resp = client.post('/event', json={"type":"transfer","origin":"100","destination":"300","amount":15})
    assert resp.status_code == 201
    assert resp.json == { "origin": {"id":"100","balance":0}, "destination": {"id":"300","balance":15}
}
