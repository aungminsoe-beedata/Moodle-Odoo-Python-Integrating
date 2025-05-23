import requests

# Moodle API endpoint and token
url = "https://nesterui.com/gicmd/webservice/rest/server.php"
token = "2b749d8a6155950572de613a1db54461"

# API function to retrieve all courses
function_name = "core_course_get_courses"

# API parameters
payload = {
    "wstoken": token,
    "wsfunction": function_name,
    "moodlewsrestformat": "json",
}

# Send the GET request
response = requests.post(url, data=payload)

# Debugging: Print raw response
print("Status code:", response.status_code)
print("Raw response:", response.text)

# Attempt to parse JSON if valid
try:
    courses = response.json()
    # Check for error in the response
    if "exception" in courses:
        print(f"Error: {courses['message']} (Code: {courses['errorcode']})")
    else:
        print("Courses:")
        for course in courses:
            print(f"ID: {course['id']}, Full Name: {course['fullname']}, Short Name: {course['shortname']}")
except requests.exceptions.JSONDecodeError as e:
    print("JSON decode error:", e)
