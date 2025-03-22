import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
#os.environ["TEAM_API_KEY"] = "d5f9ceab4735c08039a826856aa9a5647c47d9031c870f91a54c4557d1851209"
os.environ["TEAM_API_KEY"] = "aaced07ec6593e9355b1d5a1aba6ae7a12de53ea28d7e3c7e712e8a942dc7243"
# Create model tools
from aixplain.factories import AgentFactory
from aixplain.modules.agent.tool.model_tool import ModelTool
from aixplain.enums import Function, Supplier

speech_synthesis_tool = ModelTool(
    function=Function.SPEECH_SYNTHESIS,
    supplier=Supplier.GOOGLE
)

translation_tool = ModelTool(
    function=Function.TRANSLATION,
    supplier=Supplier.MICROSOFT
)

asr_tool = ModelTool(
    function=Function.SPEECH_RECOGNITION,
)
#Create index
consumption_data1 = [
    {"id": "doc1", "Energy Consumption hour": "12:00AM-1:00AM", "Energy Consumption": "1.5kWh"},
    {"id": "doc2", "Energy Consumption hour": "1:00AM-2:00AM", "Energy Consumption": "2.0kWh"},
    {"id": "doc3", "Energy Consumption hour": "2:00AM-3:00AM", "Energy Consumption": "1.8kWh"},
    {"id": "doc4", "Energy Consumption hour": "3:00AM-4:00AM", "Energy Consumption": "1.2kWh"},
    {"id": "doc5", "Energy Consumption hour": "4:00AM-5:00AM", "Energy Consumption": "1.0kWh"},
    {"id": "doc6", "Energy Consumption hour": "5:00AM-6:00AM", "Energy Consumption": "1.7kWh"},
    {"id": "doc7", "Energy Consumption hour": "6:00AM-7:00AM", "Energy Consumption": "2.5kWh"},
    {"id": "doc8", "Energy Consumption hour": "7:00AM-8:00AM", "Energy Consumption": "3.2kWh"},
    {"id": "doc9", "Energy Consumption hour": "8:00AM-9:00AM", "Energy Consumption": "3.8kWh"},
    {"id": "doc10", "Energy Consumption hour": "9:00AM-10:00AM", "Energy Consumption": "4.0kWh"},
    {"id": "doc11", "Energy Consumption hour": "10:00AM-11:00AM", "Energy Consumption": "4.2kWh"},
    {"id": "doc12", "Energy Consumption hour": "11:00AM-12:00PM", "Energy Consumption": "4.5kWh"},
    {"id": "doc13", "Energy Consumption hour": "12:00PM-1:00PM", "Energy Consumption": "4.8kWh"},
    {"id": "doc14", "Energy Consumption hour": "1:00PM-2:00PM", "Energy Consumption": "4.6kWh"},
    {"id": "doc15", "Energy Consumption hour": "2:00PM-3:00PM", "Energy Consumption": "4.3kWh"},
    {"id": "doc16", "Energy Consumption hour": "3:00PM-4:00PM", "Energy Consumption": "4.0kWh"},
    {"id": "doc17", "Energy Consumption hour": "4:00PM-5:00PM", "Energy Consumption": "3.8kWh"},
    {"id": "doc18", "Energy Consumption hour": "5:00PM-6:00PM", "Energy Consumption": "4.2kWh"},
    {"id": "doc19", "Energy Consumption hour": "6:00PM-7:00PM", "Energy Consumption": "4.5kWh"},
    {"id": "doc20", "Energy Consumption hour": "7:00PM-8:00PM", "Energy Consumption": "4.0kWh"},
    {"id": "doc21", "Energy Consumption hour": "8:00PM-9:00PM", "Energy Consumption": "3.5kWh"},
    {"id": "doc22", "Energy Consumption hour": "9:00PM-10:00PM", "Energy Consumption": "3.0kWh"},
    {"id": "doc23", "Energy Consumption hour": "10:00PM-11:00PM", "Energy Consumption": "2.5kWh"},
    {"id": "doc24", "Energy Consumption hour": "11:00PM-12:00AM", "Energy Consumption": "2.0kWh"}
]


from aixplain.factories import IndexFactory
index = IndexFactory.create(name="Energy Consumption 1", description="Index for Estimated energy Consumption")
from aixplain.modules.model.record import Record

records = [
    Record(value=item["Energy Consumption"], value_type="text", id=item["Energy Consumption hour"])
    for item in consumption_data1
]

index.upsert(records)

#Check index
response = index.search("What is the expected consumption at 10:00PM?")
response.details

#Create an agent
from aixplain.factories import AgentFactory

search_tool = ModelTool(
    model=index.id,
    description="This tool searches inside an index on hourly energy consumptin and respond to questions "
)

agent = AgentFactory.create(
    name="Energy-AI-Agetn-ver-01",
    tools=[
        speech_synthesis_tool,
        asr_tool,
        translation_tool,
        search_tool
    ],
    description="This is an Energy AI agent ",
    # required llm_id
    llm_id="6646261c6eb563165658bbb1" # GPT 4o
)
agent.id
#agent id '67de6950338999cb9696a078'