import requests

def get_response():
    url = "http://localhost:5000/api/generate"  # Update the URL to use port 5000
    headers = {
        "Content-Type": "application/json"
    }
    data = {
        "prompt": "What is AI?"
    }

    try:
        print(f"Sending request to {url}")
        # Use POST method instead of GET
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()  # Raises an HTTPError for bad responses
        print("Response Status Code:", response.status_code)
        # print("Response Body:", response.text)
        return response.json()
    except requests.exceptions.RequestException as e:
        import traceback
        print("An error occurred:")
        traceback.print_exc()


# from IPython.display import display, Markdown
answer =   get_response()
print(answer['response'])