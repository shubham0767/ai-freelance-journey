import requests

url=input("Enter API URL:")
try:
    response=requests.get(url,timeout=10)
    if response.status_code==200:
        print("Requests successful!")
        print(response.json())

    else:
        print("Request failed.")
        print("Status Code:",response.status_code)

except requests.exceptions.RequestException:
    print("Could not connect to the API.")