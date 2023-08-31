import streamlit as st

!pip install openai -q
import openai
openai.api_key= "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"
from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
from langchain.agents.agent_types import AgentType
from langchain.agents import create_csv_agent

import os
#os.environ['OPENAI_API_KEY'] = "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"
import pandas as pd

# Create the Streamlit app
def main():
    st.title("CSV Agent App")

    # Create the agent
    agent = create_csv_agent(
        OpenAI(temperature=0),
        path="teststream.csv",  # Replace with the actual file path
        verbose=True,
        agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION
    )

    # Get user input
    user_input = st.text_input("Enter your question:", "")

    if st.button("Ask"):
        # Run the agent based on user input
        response = agent.run(user_input)
        st.write("Agent's response:", response)

if __name__ == "__main__":
    main()
