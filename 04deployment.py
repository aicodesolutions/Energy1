# This program is to deploy the agent

import os

# Set the TEAM_API_KEY environment variable
# Note: The API key should be kept secure and not hard-coded in production code
os.environ["TEAM_API_KEY"] = "7b49158bfdd4208b296a6710ce770e00cb79a7b6a23013cefafa90632ff3e16f"

# Retrieve the API key from the environment variable
AIXPLAIN_API_KEY = os.getenv("TEAM_API_KEY")

# Import the AgentFactory from the aixplain package
from aixplain.factories import AgentFactory

# Define the agent ID to be deployed
AGENT_ID = "67dec93a338999cb9696a1bb"

# Get the agent instance using the AgentFactory
agent = AgentFactory.get(AGENT_ID)

# Deploy the agent
agent.deploy()
