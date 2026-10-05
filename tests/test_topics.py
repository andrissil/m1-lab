"""CR-0: tēma "Parki un skvēri" un tēmu saraksts."""

EXPECTED_TOPICS = [
    {"code": "ROADS", "name": "Ceļi un ielas"},
    {"code": "WASTE", "name": "Atkritumi"},
    {"code": "PLANNING", "name": "Teritorijas plānošana"},
    {"code": "PARKS", "name": "Parki un skvēri"},
    {"code": "OTHER", "name": "Cits"},
]


def test_list_topics(client):
    response = client.get("/topics")
    assert response.status_code == 200
    assert response.json() == EXPECTED_TOPICS


def test_create_submission_with_parks_topic(client, valid_payload):
    valid_payload["topic"] = "PARKS"
    response = client.post("/submissions", json=valid_payload)
    assert response.status_code == 201


def test_unknown_topic_returns_validation_error(client, valid_payload):
    valid_payload["topic"] = "ZOO"
    response = client.post("/submissions", json=valid_payload)
    assert response.status_code == 400
    error = response.json()["error"]
    assert error["code"] == "VALIDATION_ERROR"
    assert "topic" in [detail["field"] for detail in error["details"]]


def test_existing_topics_unchanged_and_other_last(client):
    topics = client.get("/topics").json()
    for existing in ("ROADS", "WASTE", "PLANNING", "OTHER"):
        expected = next(t for t in EXPECTED_TOPICS if t["code"] == existing)
        assert expected in topics
    assert topics[-1] == {"code": "OTHER", "name": "Cits"}
