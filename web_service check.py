import requests

# Endpoint and token
url = "https://nesterui.com/gicmd/webservice/rest/server.php"
token = "2b749d8a6155950572de613a1db54461"
function_name = "core_webservice_get_site_info"

# Request parameters
params = {
    "wstoken": token,
    "wsfunction": function_name,
    "moodlewsrestformat": "json",
}

# Make the request
response = requests.post(url, params=params)

# Print response
print("Response:", response.json())
