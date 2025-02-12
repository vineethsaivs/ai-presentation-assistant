from crewai import Crew, Agent

# Define AI Agents

# 1. Content Specialist Agent:
content_agent = Agent(
    name="Content Specialist",
    role="Generate structured content for presentations.",
    goal="Provide well-organized, engaging, and informative presentation outlines."
)

# 2. Design Expert Agent:
design_agent = Agent(
    name="Design Expert",
    role="Suggest visually appealing slide designs.",
    goal="Ensure the slides follow best practices for readability and aesthetics."
)

# 3. Speech Coach Agent:
speech_coach_agent = Agent(
    name="Speech Coach",
    role="Analyze speech recordings and provide constructive feedback.",
    goal="Help users improve clarity, pacing, and engagement during presentations."
)

# 4. Engagement Strategist Agent:
engagement_agent = Agent(
    name="Engagement Strategist",
    role="Suggest ways to keep audiences engaged.",
    goal="Enhance audience participation using interactive elements."
)

# Define the Crew and Task Flow
ai_crew = Crew(
    agents=[content_agent, design_agent, speech_coach_agent, engagement_agent],
    tasks=[
        "Generate outline -> Suggest slide designs -> Provide speech feedback -> Recommend engagement strategies"
    ]
)

# Run the AI Workflow
if __name__ == '__main__':
    result = ai_crew.execute()
    print("Workflow executed. Result:", result)

