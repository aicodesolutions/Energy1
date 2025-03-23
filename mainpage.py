
import requests
import time

#import os
#os.environ["TEAM_API_KEY"] = "7b49158bfdd4208b296a6710ce770e00cb79a7b6a23013cefafa90632ff3e16f"
#AIXPLAIN_API_KEY = os.getenv("TEAM_API_KEY")

AIXPLAIN_API_KEY = "127ac171414ce790d81e4f9da29069f2d249caf226b95af7024aafa9b54a306c"
AGENT_ID = "67dec11e338999cb9696a19a"
POST_URL = f"https://platform-api.aixplain.com/sdk/agents/{AGENT_ID}/run"

headers = {
	"x-api-key": AIXPLAIN_API_KEY,
	"Content-Type": 'application/json'
}

data = {
	"query": "<QUERY_TEXT_DATA>",
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
			time.sleep(5) # Wait for 5 seconds before checking the result again


import streamlit as st
import os

st.write("""
# My first app
Hello *world!*
""")

from aixplain.factories import AgentFactory
os.environ["TEAM_API_KEY"] = "7b49158bfdd4208b296a6710ce770e00cb79a7b6a23013cefafa90632ff3e16f"
os.environ["AIXPLAIN_API_KEY"]= "7b49158bfdd4208b296a6710ce770e00cb79a7b6a23013cefafa90632ff3e16f"
AIXPLAIN_API_KEY = os.getenv("TEAM_API_KEY")
TEAM_API_KEY = os.getenv("TEAM_API_KEY")

def AIXPL_chat (messages):
    agent_id= '67deb299181c58b7238eb57c'
    agent_id='67dec11e338999cb9696a19a'
    agent = AgentFactory.get(agent_id)
    agent_response1 = agent.run(messages)
    return agent_response1["data"]["output"]

user_input = st.chat_input("Type your message...")

if user_input:
    # Display user message
    st.chat_message("user").markdown(user_input)
    st.session_state.messages.append(user_input)

    # Get response from AIXPL
    with st.spinner("Thinking..."):
        assistant_reply = AIXPL_chat(st.session_state.messages)
    
    # Display assistant message
    st.chat_message("assistant").markdown(assistant_reply)
    st.session_state.messages.append(assistant_reply)