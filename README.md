# Moodle API Integration with Python

This guide provides step-by-step instructions for integrating Moodle API with Python to perform tasks like creating courses, retrieving categories, and managing other Moodle functionalities.

---

## Prerequisites

1. **Moodle Setup**

   * A working Moodle instance.
   * Admin access to enable web services.

2. **API Token**

   * Generate an API token in Moodle:

     * Log in to Moodle as an admin.
     * Navigate to `Site Administration` > `Server` > `Web services` > `Manage tokens`.
     * Create a token for your user.

3. **Python Environment**

   * Python 3 installed.
   * Required library:

     ```bash
     pip install requests
     ```

---

## Step 1: Verify API Access

### Check Site Information

Test your API token by retrieving site information using the `core_webservice_get_site_info` function.

#### Python Code:

```python
import requests

# Moodle API endpoint and token
url = "https://<your_moodle_url>/webservice/rest/server.php"
token = "<your_api_token>"

# API parameters
payload = {
    "wstoken": token,
    "wsfunction": "core_webservice_get_site_info",
    "moodlewsrestformat": "json",
}

response = requests.post(url, data=payload)

# Print response
print("Response:", response.json())
```

#### Expected Output:

A JSON response with site information, confirming that the token works correctly.

---

## Step 2: Retrieve Course Categories

Before creating a course, fetch the list of available categories.

#### Python Code:

```python
payload = {
    "wstoken": token,
    "wsfunction": "core_course_get_categories",
    "moodlewsrestformat": "json",
}

response = requests.post(url, data=payload)

# Print response
print("Categories:", response.json())
```

#### Expected Output:

A list of categories with `id` and `name`. Use the `id` for creating courses.

---

## Step 3: Create a Course

Use the `core_course_create_courses` function to create a course.

#### Python Code:

```python
course_data = [
    {
        "fullname": "Test Course",
        "shortname": "TEST",
        "categoryid": 1,  # Replace with a valid category ID
    }
]

payload = {
    "wstoken": token,
    "wsfunction": "core_course_create_courses",
    "moodlewsrestformat": "json",
    "courses[0][fullname]": course_data[0]["fullname"],
    "courses[0][shortname]": course_data[0]["shortname"],
    "courses[0][categoryid]": course_data[0]["categoryid"],
}

response = requests.post(url, data=payload)

# Print response
print("Response:", response.json())
```

#### Expected Output:

A JSON response with the created course details.

---

## Step 4: Debugging Common Errors

### Error: `invalid_parameter_exception`

* **Cause**: Missing or incorrect parameters.
* **Solution**: Verify required parameters and their values.

### Error: `accessexception`

* **Cause**: Insufficient permissions.
* **Solution**:

  1. Check the capabilities of the user associated with the API token.
  2. Ensure the user has the `moodle/course:create` capability.

---

## Step 5: Additional Resources

* [Moodle API Documentation](https://docs.moodle.org/dev/Web_service_API_functions)
* [Python `requests` Library](https://docs.python-requests.org/en/master/)

---

## Example API Workflow

Here’s a complete example to retrieve categories and create a course:

```python
import requests

# Moodle API endpoint and token
url = "https://<your_moodle_url>/webservice/rest/server.php"
token = "<your_api_token>"

# Get categories
categories_payload = {
    "wstoken": token,
    "wsfunction": "core_course_get_categories",
    "moodlewsrestformat": "json",
}
categories_response = requests.post(url, data=categories_payload)
categories = categories_response.json()
print("Categories:", categories)

# Create a course
course_data = [
    {
        "fullname": "Test Course",
        "shortname": "TEST",
        "categoryid": categories[0]["id"],
    }
]
create_course_payload = {
    "wstoken": token,
    "wsfunction": "core_course_create_courses",
    "moodlewsrestformat": "json",
    "courses[0][fullname]": course_data[0]["fullname"],
    "courses[0][shortname]": course_data[0]["shortname"],
    "courses[0][categoryid]": course_data[0]["categoryid"],
}
create_course_response = requests.post(url, data=create_course_payload)
print("Course Creation Response:", create_course_response.json())
```

