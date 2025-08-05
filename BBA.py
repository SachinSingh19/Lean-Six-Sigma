import streamlit as st

st.set_page_config(page_title="Lean Six Sigma", layout="wide")

# Title
st.title("Lean Six Sigma")

# Phases menu
phases = ["Define", "Measure", "Analyze", "Improve", "Control"]
selected_phase = st.radio("Select Phase", phases, horizontal=True)

# Define phase content with topics, descriptions, and video URLs
define_topics = {
    "Purpose of the Define Phase": {
        "content": """
- To identify and clearly articulate the problem or opportunity for improvement.
- To align the project with business goals and customer needs.
- To establish a clear project scope and objectives.
- To form a capable project team with defined roles and responsibilities.
- To set the foundation for data collection and analysis in later phases.
""",
        "video": "https://www.youtube.com/embed/3v5v6v6v6v6"  # Replace with actual video URL
    },
    "Identify the Problem or Opportunity": {
        "content": """
- Understand the current situation and why improvement is needed.
- Develop a clear and concise Problem Statement that describes the issue in measurable terms.
""",
        "video": "https://www.youtube.com/embed/4x4x4x4x4x4"  # Replace with actual video URL
    },
    "Define the Project Goal": {
        "content": """
- Create a Goal Statement that specifies what the project aims to achieve.
- Goals should be SMART: Specific, Measurable, Achievable, Relevant, and Time-bound.
""",
        "video": "https://www.youtube.com/embed/5y5y5y5y5y5"  # Replace with actual video URL
    },
    "Determine the Project Scope": {
        "content": """
- Define boundaries to avoid scope creep.
- Specify what is included and excluded from the project.
""",
        "video": "https://www.youtube.com/embed/6z6z6z6z6z6"  # Replace with actual video URL
    },
    "Identify Customers and Their Requirements": {
        "content": """
- Internal and external customers.
- Gather Voice of Customer (VOC) data to understand customer needs and expectations.
""",
        "video": "https://www.youtube.com/embed/7a7a7a7a7a7"  # Replace with actual video URL
    },
    "Develop a High-Level Process Map": {
        "content": """
- Use SIPOC or other mapping tools to visualize the process.
- Identify key inputs, outputs, and stakeholders.
""",
        "video": "https://www.youtube.com/embed/8b8b8b8b8b8"  # Replace with actual video URL
    },
    "Form the Project Team": {
        "content": """
- Assign roles such as Sponsor, Champion, Black Belt, Green Belt, and process owners.
- Clarify responsibilities and communication plans.
""",
        "video": "https://www.youtube.com/embed/9c9c9c9c9c9"  # Replace with actual video URL
    },
    "Develop the Project Charter": {
        "content": """
- Document all the above elements.
- Obtain formal approval from stakeholders.
""",
        "video": "https://www.youtube.com/embed/0d0d0d0d0d0"  # Replace with actual video URL
    },
}

def show_define_phase():
    st.header("Define Phase: In-Depth Overview")
    for topic, info in define_topics.items():
        with st.expander(topic):
            st.markdown(info["content"])
            if st.button(f"See Video: {topic}", key=topic):
                st.video(info["video"])

if selected_phase == "Define":
    show_define_phase()
else:
    st.info(f"Content for {selected_phase} phase will be added soon.")
