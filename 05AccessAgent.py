import requests
import time

AIXPLAIN_API_KEY = "127ac171414ce790d81e4f9da29069f2d249caf226b95af7024aafa9b54a306c"
AGENT_ID = "67dec93a338999cb9696a1bb"
POST_URL = f"https://platform-api.aixplain.com/sdk/agents/{AGENT_ID}/run"

headers = {
	"x-api-key": AIXPLAIN_API_KEY,
	"Content-Type": 'application/json'
}

data = {
	"query": "Hi",
	# "sessionId": "<SESSIONID_TEXT_DATA>",  # Optional: Specify sessionId from the previous message
}

# POST request to execute the agent
response = requests.post(POST_URL, headers=headers, json=data)
response_data = response.json()
request_id = response_data.get("requestId")

get_url = f"https://platform-api.aixplain.com/sdk/agents/{request_id}/result"

# Polling loop: GET request until the result is completed
while True:
    get_response = requests.get(get_url, headers=headers)
    result = get_response.json()
    if result.get("completed"):
        print(result)
        break
    else:
        print("Waiting for the result...")			
        time.sleep(5) # Wait for 5 seconds before checking the result again

