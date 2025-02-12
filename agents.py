import os
from crewai import Agent
from crewai_tools import SerperDevTool
from langchain_community.chat_models import ChatOllama

# Load API keys from environment variables
OLLAMA_BASE_URL = "http://localhost:11434"  # Ollama runs locally

# ✅ Correctly initializing ChatOllama
llm = ChatOllama(
    model="qwen2.5",  # Change this to any model you prefer (e.g., mistral, llama3, etc.)
    base_url=OLLAMA_BASE_URL
)

# ✅ Initialize the search tool
search_tool = SerperDevTool()

# ================================
# Define the AI Agent Roles
# ================================

# 1. Content Specialist Agent
content_specialist_agent = Agent(
    role="Content Specialist",
    goal="Generate structured outlines and detailed content based on user-provided topics.",
    backstory=(
        "You are a skilled content creator with expertise in various domains. "
        "Your role is to generate detailed and structured content that aligns with the presentation's objectives."
    ),
    llm=llm,
    max_iter=5,
    tools=[search_tool],
    allow_delegation=True,
    verbose=True
)

# 2. Design Expert Agent
design_expert_agent = Agent(
    role="Design Expert",
    goal="Suggest visually appealing slide layouts, color schemes, and graphics.",
    backstory="You are an expert in visual communication, ensuring slides are engaging and aesthetically pleasing.",
    llm=llm,
    max_iter=5,
    tools=[],
    allow_delegation=False,
    verbose=True
)

# 3. Speech Coach Agent
speech_coach_agent = Agent(
    role="Speech Coach",
    goal="Analyze speech recordings and provide constructive feedback.",
    backstory="As a speech coach, you specialize in enhancing vocal clarity, pacing, and confidence.",
    llm=llm,
    max_iter=5,
    tools=[],
    allow_delegation=False,
    verbose=True
)

# 4. Engagement Strategist Agent
engagement_strategist_agent = Agent(
    role="Engagement Strategist",
    goal="Enhance audience participation through storytelling and interactive elements.",
    backstory="You specialize in keeping the audience engaged through compelling storytelling and dynamic presentation elements.",
    llm=llm,
    max_iter=5,
    tools=[],
    allow_delegation=False,
    verbose=True
)

if __name__ == '__main__':
    print("Agents initialized successfully.")
