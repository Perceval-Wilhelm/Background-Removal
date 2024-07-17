from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_segment_image_success():
    with open("tests/sample_image.png", "rb") as img:
        response = client.post(
            "/segment",
            files={"file": img},
            data={"challenge": "cv3"}
        )
    assert response.status_code == 200
    assert "segmented_image_path" in response.json()

def test_invalid_challenge():
    with open("tests/sample_image.png", "rb") as img:
        response = client.post(
            "/segment",
            files={"file": img},
            data={"challenge": "invalid"}
        )
    assert response.status_code == 400
    assert response.json() == {"message": "Invalid challenge type"}
