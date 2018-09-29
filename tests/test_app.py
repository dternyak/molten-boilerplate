def test_users(client, app, auth):
    response = client.get(app.reverse_uri("list_users"), auth=auth)
    assert response.data == "[]"

    response = client.post(app.reverse_uri("create_user"), auth=auth, json={
        "email_address": "wow@gmail.com",
    })
    assert response.status_code == 201

    user = response.json()
    response = client.get(
        app.reverse_uri("get_user", user_id=user["id"]),
        auth=auth,
    )
    assert response.status_code == 200
    assert response.json() == user

    response = client.delete(
        app.reverse_uri("delete_user", user_id=user["id"]),
        auth=auth,
    )
    assert response.status_code == 204

    response = client.get(
        app.reverse_uri("get_user", user_id=user["id"]),
        auth=auth,
    )
    assert response.status_code == 404
