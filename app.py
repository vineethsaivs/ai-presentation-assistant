# import streamlit as st
# from search_api_integration import search_query
# from agents import content_specialist_agent  # Import the content specialist agent
# from crewai import Crew, Task  # Import Crew and Task from CrewAI

# # Helper function to generate slide content via the agent
# def generate_slide_content(prompt):
#     """
#     Generate slide content using the Content Specialist Agent via a temporary Crew and Task.
#     Ensures the output is fully formed and does not get truncated.
#     """
#     task = Task(
#         description=prompt,
#         expected_output="A fully formed, well-structured paragraph that expands the given content.",
#         agent=content_specialist_agent,
#         async_execution=False
#     )
#     crew = Crew(
#         agents=[content_specialist_agent],
#         tasks=[task],
#         process="sequential"
#     )
#     result = crew.kickoff(inputs={})
    
#     if isinstance(result, dict):
#         return result.get("output", str(result)).strip()
#     elif isinstance(result, str):
#         return result.strip()
#     else:
#         return str(result).strip()

# # Configure page layout and title
# st.set_page_config(page_title="AI-Powered Virtual Presentation Assistant", layout="wide")

# # Custom CSS styling
# st.markdown(
#     """
#     <style>
#     .title {
#         color: #3E4E88;
#         font-size: 3em;
#         text-align: center;
#     }
#     .footer {
#         text-align: center;
#         font-size: 0.9em;
#         color: #888;
#     }
#     </style>
#     """,
#     unsafe_allow_html=True,
# )
# st.markdown("<h1 class='title'>AI-Powered Virtual Presentation Assistant</h1>", unsafe_allow_html=True)

# # ---- Presentation Details Input Section ----
# st.header("Presentation Details")

# # 1. Industry selection (first input)
# industry = st.selectbox("Select your industry:", ["Business", "Education", "Technology", "Other"])

# # 2. Number of slides needed (second input)
# num_slides = st.number_input("Number of slides needed:", min_value=3, max_value=20, value=6, step=1)

# # 3. Customize slide text size (third input)
# text_size = st.slider("Customize slide text size (px):", min_value=12, max_value=36, value=16)

# # 4. Presentation topic (fourth input)
# topic = st.text_input("Enter your presentation topic:")

# # ---- Generate Presentation Content when all inputs are provided ----
# if industry and num_slides and text_size and topic:
#     st.subheader("Generating Presentation Content...")
    
#     # Create a richer search query by combining topic and industry
#     combined_query = f"{topic} in {industry}"
#     try:
#         results = search_query(combined_query)
#     except Exception as e:
#         st.error(f"Error fetching search results: {e}")
#         results = []
    
#     # Display the search results (for reference)
#     st.subheader("Search Results:")
#     if results:
#         for result in results:
#             st.markdown(f"**{result['name']}**")
#             st.markdown(f"[Read more]({result['url']})")
#             st.write(result['snippet'])
#             st.write("---")
#     else:
#         st.write("No search results found.")
    
#     # ---- Generate a Slide Content Outline ----
#     st.subheader("Slide Content Outline")
#     slide_contents = []
    
#     # Slide 1: Introduction
#     slide_contents.append((
#         "Introduction",
#         f"Introduce the topic of **{topic}** in the context of the **{industry}** industry. Define key terms, set the context, and outline the presentation goals."
#     ))
    
#     # Calculate the number of main slides (slides between Introduction and Conclusion)
#     num_main = num_slides - 2
#     for i in range(num_main):
#         if i < len(results):
#             # Use search result title and snippet if available
#             title = results[i]["name"]
#             snippet = results[i]["snippet"]
            
#             # Detect and fix truncation issues ("...")
#             if snippet.endswith("..."):
#                 expansion_prompt = (
#                     f"Expand and rewrite the following snippet for better clarity: {snippet} "
#                     f"in the context of '{topic}' in the '{industry}' industry."
#                 )
#                 expanded_snippet = generate_slide_content(expansion_prompt)
#                 content = f"Discuss the point: **{title}**. {expanded_snippet}"
#             else:
#                 content = f"Discuss the point: **{title}**. {snippet}"
#         else:
#             # Use Content Specialist Agent to generate slide content when search results are insufficient
#             prompt = (
#                 f"Generate detailed slide content for slide number {i+2} of a presentation on '{topic}' "
#                 f"in the '{industry}' industry. Provide a concise title on the first line and a detailed description on the following lines."
#             )
#             generated_output = generate_slide_content(prompt)
#             parts = generated_output.split("\n", 1)
#             if len(parts) >= 2:
#                 title = parts[0].strip()
#                 content = parts[1].strip()
#             else:
#                 title = f"Additional Consideration {i+1}"
#                 content = generated_output.strip()
#         slide_contents.append((title, content))
    
#     # Slide Last: Conclusion
#     slide_contents.append((
#         "Conclusion",
#         f"Summarize the key points about **{topic}** and provide actionable insights for the **{industry}** industry. Reinforce main takeaways and suggest next steps."
#     ))
    
#     # ---- Display Each Slide's Content with Customized Text Size ----
#     for slide_num, (title, content) in enumerate(slide_contents, start=1):
#         st.markdown(
#             f"<h2 style='font-size:{text_size + 4}px;'>Slide {slide_num}: {title}</h2>",
#             unsafe_allow_html=True
#         )
#         st.markdown(
#             f"<p style='font-size:{text_size}px;'>{content}</p>",
#             unsafe_allow_html=True
#         )
#         st.write("---")
    
#     # ---- Consolidated Presentation Outline ----
#     st.subheader("Consolidated Presentation Outline")
#     outline = f"**Presentation Outline for {topic} in {industry}:**\n"
#     for slide_num, (title, _) in enumerate(slide_contents, start=1):
#         outline += f"{slide_num}. {title}\n"
#     st.markdown(outline)
    
# # ---- Footer ----
# st.markdown("<p class='footer'>Developed with CrewAI and Streamlit.</p>", unsafe_allow_html=True)


import streamlit as st
from search_api_integration import search_query
from agents import content_specialist_agent
from crewai import Crew, Task

# Helper function to generate slide content
def generate_slide_content(prompt):
    """
    Generate slide content using the Content Specialist Agent via a temporary Crew and Task.
    The task expects the agent to produce output where the first line is a concise title,
    and subsequent lines form the detailed description.
    """
    task = Task(
        description=prompt,
        expected_output="A slide title on the first line and detailed content on the following lines.",
        agent=content_specialist_agent,
        async_execution=False
    )
    crew = Crew(
        agents=[content_specialist_agent],
        tasks=[task],
        process="sequential"
    )
    result = crew.kickoff(inputs={})
    
    # Extract and return the result
    if isinstance(result, dict):
        return result.get("output", str(result))
    elif isinstance(result, str):
        return result
    else:
        return str(result)

# Configure Streamlit page layout
st.set_page_config(page_title="AI-Powered Virtual Presentation Assistant", layout="wide")

st.markdown("<h1 class='title'>AI-Powered Virtual Presentation Assistant</h1>", unsafe_allow_html=True)

# ---- Presentation Details Input Section ----
st.header("Presentation Details")

industry = st.selectbox("Select your industry:", ["Business", "Education", "Technology", "Other"])
num_slides = st.number_input("Number of slides needed:", min_value=3, max_value=20, value=6, step=1)
text_size = st.slider("Customize slide text size (px):", min_value=12, max_value=36, value=16)
topic = st.text_input("Enter your presentation topic:")

# ---- Generate Presentation Content when inputs are provided ----
if industry and num_slides and text_size and topic:
    st.subheader("Generating Presentation Content...")

    # Perform a search query
    combined_query = f"{topic} in {industry}"
    try:
        results = search_query(combined_query)
    except Exception as e:
        st.error(f"Error fetching search results: {e}")
        results = []
    
    # Display Search Results
    st.subheader("Search Results:")
    if results:
        for result in results:
            st.markdown(f"**{result['name']}**")
            st.markdown(f"[Read more]({result['url']})")
            st.write(result['snippet'])
            st.write("---")
    else:
        st.write("No search results found.")

    # ---- Generate a Slide Content Outline ----
    st.subheader("Slide Content Outline")
    slide_contents = [("Introduction", f"Introduce the topic of **{topic}** in the **{industry}** industry.")]

    # Generate slides
    num_main = num_slides - 2
    for i in range(num_main):
        if i < len(results):
            title = results[i]["name"]
            content = f"Discuss: **{results[i]['name']}**. {results[i]['snippet']}"
        else:
            prompt = f"Generate content for slide {i+1} on '{topic}' in the '{industry}' industry."
            generated_output = generate_slide_content(prompt)
            parts = generated_output.split("\n", 1)
            title, content = parts[0].strip(), parts[1].strip() if len(parts) > 1 else (f"Slide {i+1}", generated_output.strip())
        
        slide_contents.append((title, content))

    slide_contents.append(("Conclusion", f"Summarize the key points and provide actionable insights for **{topic}**."))

    # Display each slide's content
    for slide_num, (title, content) in enumerate(slide_contents, start=1):
        st.markdown(f"<h2 style='font-size:{text_size + 4}px;'>Slide {slide_num}: {title}</h2>", unsafe_allow_html=True)
        st.markdown(f"<p style='font-size:{text_size}px;'>{content}</p>", unsafe_allow_html=True)
        st.write("---")

    # Display Consolidated Outline
    st.subheader("Consolidated Presentation Outline")
    outline = f"**Presentation Outline for {topic} in {industry}:**\n"
    for slide_num, (title, _) in enumerate(slide_contents, start=1):
        outline += f"{slide_num}. {title}\n"
    st.markdown(outline)

# ---- Footer ----
st.markdown("<p class='footer'>Developed with CrewAI and Streamlit.</p>", unsafe_allow_html=True)
