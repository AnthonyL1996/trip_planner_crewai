import os

from crewai import Agent
from tools import BrowserTool
from tools import CalculatorTool
from tools import SearchTool

# GROQ
os.environ["OPENAI_API_BASE"] = "https://api.groq.com/openai/v1"
os.environ["OPENAI_MODEL_NAME"] = "llama3-70b-8192"
os.environ["OPENAI_API_KEY"] = "###"

# os.environ["OPENAI_API_BASE"] = "http://localhost:11434/v1"
# os.environ["OPENAI_MODEL_NAME"] = "mistral"
# os.environ["OPENAI_API_KEY"] = "NAN"

class TripAgents:

    def city_selection_agent(self):
        return Agent(
            role='City Selection Expert',
            goal='Select the best city based on weather, season, and prices',
            backstory=
            'An expert in analyzing travel data to pick ideal destinations',
            tools=[
                SearchTool.search_internet,
                BrowserTool.scrape_and_summarize_website,
            ],
            verbose=True,
            max_iter=3,
            max_rpm=4
        )

    def local_expert(self):
        return Agent(
            role='Local Expert at this city',
            goal='Provide the BEST insights about the selected city',
            backstory="""A knowledgeable local guide with extensive information
        about the city, it's attractions and customs""",
            tools=[
                SearchTool.search_internet,
                BrowserTool.scrape_and_summarize_website,
            ],
            verbose=True,
            max_iter=3,
            max_rpm=4
        )

    def travel_concierge(self):
        return Agent(
            role='Amazing Travel Concierge',
            goal="""Create the most amazing travel itineraries with budget and 
        packing suggestions for the city""",
            backstory="""Specialist in travel planning and logistics with 
        decades of experience""",
            tools=[
                SearchTool.search_internet,
                BrowserTool.scrape_and_summarize_website,
                CalculatorTool.calculate,
            ],
            verbose=True,
            max_iter=3,
            max_rpm=4
        )
