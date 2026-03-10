import requests

url = "https://api.github.com/repos/python/cpython"

response = requests.get(url)
data = response.json()

print("Repository:", data ["name"] )
print("Stars:", data["stargazers_count"])