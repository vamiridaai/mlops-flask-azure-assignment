import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parents[1]

if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

from app import app  # noqa: E402


def test_home():
    client = app.test_client()
    response = client.get("/")

    assert response.status_code == 200
    assert response.get_json()["status"] == "running"


def test_health():
    client = app.test_client()
    response = client.get("/health")

    assert response.status_code == 200
    assert response.get_json()["status"] == "healthy"


def test_prediction():
    client = app.test_client()

    response = client.post(
        "/predict",
        json={
            "features": [
                5.1,
                3.5,
                1.4,
                0.2,
            ]
        },
    )

    assert response.status_code == 200

    data = response.get_json()

    assert "prediction" in data
    assert "class_name" in data
    assert data["class_name"] in [
        "setosa",
        "versicolor",
        "virginica",
    ]


def test_invalid_prediction():
    client = app.test_client()

    response = client.post(
        "/predict",
        json={
            "features": [
                1,
                2,
            ]
        },
    )

    assert response.status_code == 400
