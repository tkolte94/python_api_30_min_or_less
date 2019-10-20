import requests

# First we will check to see if the app is up
url = "http://localhost:8000/"
print("Checking app up...")
resp = requests.get(url)
print(resp.status_code)
print(resp.json())

# Then we will check to see if the basic function works
print("Checking basic function...")
resp = requests.get(url + '/test')
print(resp.status_code)
print(resp.json())

# Testing the say hi function
print("Checking say hi function...")
resp = requests.get(url + '/sayhi/Tanvi')
print(resp.status_code)
print(resp.json())