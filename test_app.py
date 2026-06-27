from Test import app


def main():
    client = app.test_client()
    response = client.get("/")

    assert response.status_code == 200
    assert b"Application Successfully Deployed" in response.data

    print("Smoke test passed.")


if __name__ == "__main__":
    main()
