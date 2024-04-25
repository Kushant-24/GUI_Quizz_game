import requests

parameters = {
    "amount":10,
    "difficulty":"medium",
    "type":"boolean",
}
response = requests.get("https://opentdb.com/api.php",params=parameters)
questions = response.json()["results"]
# print(questions)