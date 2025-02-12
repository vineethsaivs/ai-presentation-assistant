# 🚀 AI Presentation Assistant

An **AI-powered virtual assistant** that helps generate structured and engaging **presentation content** using **CrewAI, Streamlit, and Ollama**. This tool automates content creation, slide design recommendations, and speech coaching to enhance **presentation effectiveness**.

---

## 🛠️ **Features**

- 📊 **AI-Generated Structured Content**: Automatically creates well-organized slides based on a given topic.
- 🎨 **Slide Design Recommendations**: Ensures that presentations are visually appealing and follow best design practices.
- 🗣️ **Speech Coaching**: Analyzes presentation rehearsals and provides constructive feedback on clarity and pacing.
- 🎭 **Audience Engagement Strategies**: Suggests ways to make presentations more interactive and engaging.

---

## 🔧 **Technologies Used**

- **CrewAI** → Manages AI agents and workflows for content generation and analysis.
- **Streamlit** → Provides an intuitive UI for users to input presentation details and view results.
- **Ollama** → Handles large language model (LLM) processing locally.
- **Python** → Main programming language used for AI and UI integration.

---

## 📂 **Project Structure**

```
📁 ai-presentation-assistant
│── 📄 app.py                # Main Streamlit UI application
│── 📄 agents.py             # AI agents for different presentation tasks
│── 📄 workflow.py           # CrewAI workflow definition
│── 📄 search_api_integration.py # Handles external API search queries
│── 📂 requirements.txt      # Dependencies required for the project
│── 📂 README.md             # Documentation (this file)
```

---

## 🚀 **Installation & Setup**

### **1️⃣ Clone the Repository**
```sh
git clone https://github.com/vineethsaivs/ai-presentation-assistant.git
cd ai-presentation-assistant
```

### **2️⃣ Set Up a Virtual Environment (Recommended)**
```sh
python3 -m venv presentation_env
source presentation_env/bin/activate  # For macOS/Linux
presentation_env\Scripts\activate    # For Windows
```

### **3️⃣ Install Dependencies**
```sh
pip install -r requirements.txt
```

### **4️⃣ Start Ollama (Ensure It's Running)**
```sh
ollama serve
```

### **5️⃣ Run the Streamlit App**
```sh
streamlit run app.py
```

Now, open **http://localhost:8501/** in your browser to use the AI Presentation Assistant!

---

## 📖 **How It Works**

### **1️⃣ Input Details**
- **Select an Industry** (e.g., Business, Education, Technology)
- **Choose the Number of Slides**
- **Adjust Text Size**
- **Enter Your Presentation Topic**

### **2️⃣ AI-Generated Content**
- The system fetches relevant **search results** to enrich content.
- It **auto-generates slide titles and structured content**.
- **Speech coaching and engagement strategies** are suggested.

### **3️⃣ Output Presentation Outline**
- Each slide is structured with **a title and detailed points**.
- A **summary of the entire presentation** is displayed.
- The UI presents **clear and readable formatted text**.

---

## 🛠️ **Customization & Configuration**

### **Changing the LLM Model**
- The project uses **Qwen2.5** as the default model.
- To change the model, update **`agents.py`**:
  ```python
  from langchain_community.chat_models import ChatOllama
  llm = ChatOllama(model="mistral", base_url="http://localhost:11434")
  ```

### **Modifying Agents**
- Defined in **`agents.py`**, the AI agents control content generation.
- To tweak agent behaviors, modify:
  ```python
  content_specialist_agent = Agent(
      role="Content Specialist",
      goal="Generate structured outlines for presentations.",
      llm=llm,
      max_iter=5,
      verbose=True
  )
  ```

### **Expanding Functionality**
- Add new tasks in **`workflow.py`** to introduce additional AI functionalities.
- Example:
  ```python
  ai_crew = Crew(
      agents=[content_specialist_agent, design_expert_agent],
      tasks=["Generate an outline -> Suggest slide visuals"]
  )
  ```

---

## 🚀 **Future Enhancements**
- ✅ **Export to PowerPoint or Google Slides**
- ✅ **Voice-Based Interaction for Speech Coaching**
- ✅ **Integration with ChatGPT / OpenAI for Enhanced AI Suggestions**

---

## 📜 **License**
This project is open-source and available under the **MIT License**.

Happy Presenting! 🎤📊🚀

