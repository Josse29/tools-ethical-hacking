# pip install requests
import requests

response = requests.get("https://www.apple.com")

print("\n\nRequest Headers")
for k, v in response.request.headers.items():
    print(k, ":", v)

print("\n\nResponse Headers")
for k, v in response.headers.items():
    print(k, ":", v)
   

