import os
import requests
import streamlit as st

IBM_API_KEY='jNhdhHbmJmiphJ_HnyI3gDK-_SJEmmeTpw8cWkF_yBP_'

# Get Project ID from https://dataplatform.cloud.ibm.com/projects/?context=wx   (it is in your project url)
IBM_PROJECT_ID = "xxxxxxx-xxxx-xxxx-xxxx-xxxxxxxx"
IBM_PROJECT_ID = "68518b55-09d0-4a6c-b75d-6f69507d84eb"

IBM_URL_TOKEN = "https://iam.cloud.ibm.com/identity/token"
IBM_URL_CHAT = "https://us-south.ml.cloud.ibm.com/ml/v1/text/chat?version=2023-10-25"

##############################################
##
##   IBM API
##
##############################################
def IBM_token():
    # Define the headers
    headers = {
        "Content-Type": "application/x-www-form-urlencoded"
    }
    
    # Define the data payload
    data = {
        "grant_type": "urn:ibm:params:oauth:grant-type:apikey",
        "apikey": IBM_API_KEY
    }
    
    # Make the POST request
    response = requests.post(IBM_URL_TOKEN, headers=headers, data=data)
    st.session_state.IBM_ACCESS_TOKEN = response.json().get("access_token", "")

import time



def IBM_chat (messages):
  AIXPLAIN_API_KEY = "127ac171414ce790d81e4f9da29069f2d249caf226b95af7024aafa9b54a306c"
  AGENT_ID = "67dec93a338999cb9696a1bb"
  POST_URL = f"https://platform-api.aixplain.com/sdk/agents/{AGENT_ID}/run"

  headers = {
	"x-api-key": AIXPLAIN_API_KEY,
	"Content-Type": 'application/json'
}
  data = {
	"query": messages
    }
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
        return result['data']['output']
        break
    else:
        print("Waiting for the result...")			
        time.sleep(5) # Wait for 5 seconds before checking the result again
    #eturn response["choices"][0]["message"]["content"]
    #return result

# Initialize
if "messages" not in st.session_state:
    st.session_state.messages = []

#BM_token();

# UI
st.title("💬 Your Energy AI Chatbot")
st.write("Ask me anything!")

# Display chat history
for message in st.session_state.messages:
    if (message["role"]!='system'):
     with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input
user_input = st.chat_input("Type your message...")

if user_input:
  

    # Display user message
    st.chat_message("user").markdown(user_input)
    st.session_state.messages.append({"role": "user", "content": user_input})

    # Get response from IBM
    with st.spinner("Thinking..."):
      #assistant_reply = IBM_chat(st.session_state.messages)
      assistant_reply = IBM_chat(user_input)
    # Display assistant message
    st.chat_message("assistant").markdown(assistant_reply)
    st.session_state.messages.append({"role": "assistant", "content": assistant_reply})