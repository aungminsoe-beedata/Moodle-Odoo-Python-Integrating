import requests
import json

# Moodle API endpoint and token
url = "https://nesterui.com/gicmd/webservice/rest/server.php"
token = "2b749d8a6155950572de613a1db54461"

# Function name and course data
function_name = "core_course_create_courses"
course_data = [
    {
        "fullname": "Test Course",
        "shortname": "TEST",
        "categoryid": 1,  # Replace with a valid category ID
    }
]

# API parameters
payload = {
    "wstoken": token,
    "wsfunction": function_name,
    "moodlewsrestformat": "json",
    "courses[0][fullname]": course_data[0]["fullname"],
    "courses[0][shortname]": course_data[0]["shortname"],
    "courses[0][categoryid]": course_data[0]["categoryid"],
}

# Send the POST request
response = requests.post(url, data=payload)

# Print raw response for debugging
print("Status code:", response.status_code)
print("Raw response:", response.text)

# Attempt to parse JSON if valid
try:
    response_data = response.json()
    print("Response JSON:", response_data)
except requests.exceptions.JSONDecodeError as e:
    print("JSON decode error:", e)
