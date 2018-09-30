def test_comments(client, app, auth):
    response = client.get(app.reverse_uri("list_comments"), auth=auth)
    assert response.data == "[]"

    response = client.post(app.reverse_uri("create_user"), auth=auth, json={
        "emailAddress": "wow@gmail.com",
    })
    assert response.status_code == 201
    user = response.json()

    response = client.post(app.reverse_uri("create_comment"), auth=auth, json={
        "content": "Such a comment",
        "userId": user["id"]
    })

    comment = response.json()

    assert response.status_code == 201

    response = client.get(
        app.reverse_uri("get_comment", comment_id=comment["id"]),
        auth=auth,
    )

    assert response.json() == comment
