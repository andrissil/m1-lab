"""CR-1: personas koda pārbaude iesniegumā (9 pārbaudes)."""

import pytest


def _saved_personal_code(client, response):
    submission_id = response.json()["id"]
    return client.get(f"/submissions/{submission_id}").json()["personalCode"]


@pytest.mark.parametrize(
    ("personal_code", "saved"),
    [
        ("32000000001", "32000000001"),  # 1
        ("320000-00001", "32000000001"),  # 2
        ("  32000000001  ", "32000000001"),  # 3: atstarpes noņemtas
        ("311299-21233", "31129921233"),  # 8: vecais formāts
    ],
)
def test_valid_personal_code_is_saved_normalized(
    client, valid_payload, personal_code, saved
):
    valid_payload["personalCode"] = personal_code
    response = client.post("/submissions", json=valid_payload)
    assert response.status_code == 201
    assert _saved_personal_code(client, response) == saved


@pytest.mark.parametrize(
    "personal_code",
    [
        "3200000000",  # 4: 10 cipari
        "320000000012",  # 5: 12 cipari
        "32000000O01",  # 6: burts O, nevis nulle
        "3200-0000001",  # 9: defise nepareizā vietā
    ],
)
def test_invalid_personal_code_returns_invalid_format(
    client, valid_payload, personal_code
):
    valid_payload["personalCode"] = personal_code
    response = client.post("/submissions", json=valid_payload)
    assert response.status_code == 400
    error = response.json()["error"]
    assert error["code"] == "VALIDATION_ERROR"
    assert error["details"] == [{"field": "personalCode", "issue": "INVALID_FORMAT"}]


@pytest.mark.parametrize("personal_code", [None, "", "   "])  # 7
def test_missing_or_empty_personal_code_returns_required(
    client, valid_payload, personal_code
):
    if personal_code is None:
        del valid_payload["personalCode"]
    else:
        valid_payload["personalCode"] = personal_code
    response = client.post("/submissions", json=valid_payload)
    assert response.status_code == 400
    error = response.json()["error"]
    assert error["code"] == "VALIDATION_ERROR"
    assert error["details"] == [{"field": "personalCode", "issue": "REQUIRED"}]


def test_invalid_personal_code_is_not_saved(client, valid_payload, fake_omd):
    valid_payload["personalCode"] = "3200000000"
    client.post("/submissions", json=valid_payload)
    assert fake_omd.calls == []


def test_omd_is_called_with_normalized_code(client, valid_payload, fake_omd):
    valid_payload["personalCode"] = " 320000-00001 "
    response = client.post("/submissions", json=valid_payload)
    assert response.json()["replyChannel"] == "E_ADDRESS"
    assert fake_omd.calls == ["32000000001"]


def test_invalid_personal_code_is_not_echoed(client, valid_payload, caplog):
    valid_payload["personalCode"] = "320000-0000X"
    with caplog.at_level("DEBUG"):
        response = client.post("/submissions", json=valid_payload)
    assert response.status_code == 400
    assert "0000X" not in response.text
    assert "0000X" not in caplog.text
