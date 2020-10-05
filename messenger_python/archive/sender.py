import requests

response = requests.post(
    "http://127.0.0.1:5000/send_message?after=0",
    json={"text": "Hi", "author": "X"}
)
print(response.status_code)
print(response.text)
