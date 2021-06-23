import requests
print("timeout = 1")

try:
    r = requests.get('https://www.w3schools.com/', timeout = 0.01)
    print(r.headers)
except requests.exceptions.RequestException as e:
    print(e)    

print("\nServer timeout = 1.0")    
try:
    r = requests.get('https://www.w3schools.com/', timeout = 1.0)
    print("Connected....!")
except requests.exceptions.RequestException as e:
    print(e)