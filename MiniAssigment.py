import requests


def test_Check_Status():
    response = requests.get("https://hbs-ob-stage.herokuapp.com/status")
    response_body = response.json()
    print(response_body)
    assert response.status_code == 200


def test_Create_User():
    endpoint = "https://hbs-ob-stage.herokuapp.com/status"
    payload = {
        "name": "user077554",
        "phone": "+919043522299",
        "email": "user077554@hashedin.com",
        "password": "admin",
        "otp": 111111
    }

    response = requests.post(url=endpoint, json=payload)
    response_body = response.json()
    print(response_body)
    assert response.status_code == 201


def test_GetOTP():
    endpoint = "https://hbs-ob-stage.herokuapp.com/get_register_otp"
    payload = {
        "phone": "+91906677737"
    }
    response = requests.post(url=endpoint, json=payload)
    response_body = response.json()
    print(response_body)
    assert response.status_code == 200


def test_DeleteUser():
    endpoint = "https://hbs-ob-stage.herokuapp.com/user"
    payload = {
        "phone": "+919066752237",
        "otp": 111111
    }

    response = requests.delete(url=endpoint, json=payload)
    response_body = response.json()
    print(response_body)
    assert response.status_code == 200


def test_Edit_User():
    endpoint = "https://hbs-ob-stage.herokuapp.com/user"
    payload = {
        "name": "userrwoo",
        "phone": "+91906677737",
        "email": "user7732321@hashedin.com",
        "password": "admin",
        "otp": 111111
    }

    response = requests.put(url=endpoint, json=payload)
    response_body = response.json()
    print(response)
    print(response_body)
    assert response.status_code == 200


def test_LoginOTP():
    endpoint = "https://hbs-ob-stage.herokuapp.com/get_otp"
    payload = {
        "phone": "+91906677737"
    }
    response = requests.post(url=endpoint, json=payload)
    response_body = response.json()
    print(response_body)
    assert response.status_code == 200


def test_Authenticate():
    endpoint = "https://hbs-ob-stage.herokuapp.com/authenticate"
    payload = {
        "phone": "+919066752237",
        "LoginType": "OTP",
        "otp": 111111
    }

    headers = {"Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6dHJ1ZSwiaWF0IjoxNjQ0NTc2MDQ3LCJqdGkiOiI4YzNhOGU3Yi0yMzUxLTRmYzItYTZlYy1mODgwYWQyZjViNDMiLCJuYmYiOjE2NDQ1NzYwNDcsInR5cGUiOiJhY2Nlc3MiLCJzdWIiOiI2MjA2M2JkYzliZDlkZGExMzFmNzNjNDUiLCJleHAiOjE2NDQ1NzY5NDd9.wFSob0sFpDqY9PdmelC9DJwpR7DFk24vX5xXI1jlOEw"}

    response = requests.post(url=endpoint, json=payload, headers=headers)
    response_body = response.json()
    print(response_body)
    assert response.status_code == 200

def test_Login():
    header_value = {
        "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6dHJ1ZSwiaWF0IjoxNjQ0NTc2MDQ3LCJqdGkiOiI4YzNhOGU3Yi0yMzUxLTRmYzItYTZlYy1mODgwYWQyZjViNDMiLCJuYmYiOjE2NDQ1NzYwNDcsInR5cGUiOiJhY2Nlc3MiLCJzdWIiOiI2MjA2M2JkYzliZDlkZGExMzFmNzNjNDUiLCJleHAiOjE2NDQ1NzY5NDd9.wFSob0sFpDqY9PdmelC9DJwpR7DFk24vX5xXI1jlOEw"}
    response = requests.get("https://hbs-ob-stage.herokuapp.com/protected_test",headers=header_value)


    response_body = response.json()
    print(response_body)
    assert response.status_code == 200