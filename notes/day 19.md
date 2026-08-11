Day 19 – APIs & JSON
1. What is an API?

API stands for Application Programming Interface. It allows two different applications or systems to communicate and exchange data.

Example:

Python Program → API → GitHub → Response
2. What does HTTP stand for?

HTTP stands for HyperText Transfer Protocol.

It is a protocol used for communication between clients, such as web browsers or Python programs, and web servers.

3. What is a GET request?

A GET request is used to request or retrieve data from a server.

Example:

requests.get(url)

In our GitHub project, we used a GET request to retrieve GitHub profile information.

4. What is JSON?

JSON stands for JavaScript Object Notation.

It is a common format used to store and exchange data between applications.

Example:

{
    "name": "Shubham",
    "age": 21,
    "course": "BCA"
}
5. What does requests.get() do?

requests.get() sends an HTTP GET request to a specified URL and receives the server's response.

Example:

response = requests.get("https://api.github.com")
6. What does response.status_code represent?

response.status_code tells us the result of the HTTP request.

For example:

200 → Request successful
404 → Resource not found

We used it in our GitHub Profile Analyzer to check whether the GitHub user was found.

7. What does response.json() do?

response.json() converts a JSON response from the server into Python data, usually a dictionary when the JSON response is an object.

Example:

data = response.json()

print(data["name"])
8. What is the difference between JSON and a Python dictionary?

JSON is a data-exchange format, while a Python dictionary is a Python data structure.

Example JSON:

{
    "name": "Shubham",
    "age": 21
}

Python dictionary:

student = {
    "name": "Shubham",
    "age": 21
}

They look similar, but JSON is commonly used for exchanging data between applications, while dictionaries are used to work with data inside Python.

9. Why is error handling important when working with APIs?

API requests can fail because of:

No internet connection
Invalid URL
Server problems
Invalid username
Resource not found
Request timeout

Using try-except and checking the status code prevents the program from crashing and allows us to show a useful message to the user.

Example:

try:
    response = requests.get(url)
except requests.exceptions.RequestException:
    print("Could not connect to the API.")
10. Give two real-life examples where APIs are useful.

Example 1 – Weather App

A weather application can use a weather API to retrieve current temperature, humidity, and forecast information.

Example 2 – Payment System

An online shopping website can use a payment API to communicate with a payment service and process payments.

 Day 19 Quick Revision
API          → Allows applications to communicate
HTTP         → Protocol used for web communication
GET          → Requests data
JSON         → Common data-exchange format
requests.get → Sends a GET request
status_code  → Shows request result
response.json() → Converts JSON response into Python data
try-except   → Handles API/network errors