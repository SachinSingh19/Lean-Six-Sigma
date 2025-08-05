import streamlit as st

# Page config
st.set_page_config(page_title="Lean Six Sigma", layout="wide")

# Inject custom CSS for styling
st.markdown(
    """
    <style>
    /* General body */
    .main {
        background-color: #f5f7fa;
        color: #333333;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    /* Header text */
    .header-text {
        color: #004080;
        font-weight: 700;
        font-size: 3.5rem;
        text-align: center;
        margin-top: 1rem;
        margin-bottom: 1rem;
        letter-spacing: 2px;
    }
    /* Phase cards */
    .phase-card {
        background: white;
        border-radius: 15px;
        padding: 1.5rem;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        transition: transform 0.2s ease-in-out;
        cursor: pointer;
        text-align: center;
        color: #004080;
        font-weight: 600;
        font-size: 1.25rem;
    }
    .phase-card:hover {
        transform: translateY(-10px);
        box-shadow: 0 8px 16px rgba(0,0,0,0.2);
    }
    /* Content area */
    .content-area {
        background: white;
        border-radius: 15px;
        padding: 2rem;
        box-shadow: 0 4px 12px rgba(0,0,0,0.1);
        margin-top: 2rem;
        color: #222222;
    }
    /* Video container */
    .video-container {
        margin-top: 1rem;
        text-align: center;
    }
    /* Button style */
    div.stButton > button:first-child {
        background-color: #004080;
        color: white;
        border-radius: 8px;
        padding: 0.5rem 1.5rem;
        font-weight: 600;
        transition: background-color 0.3s ease;
    }
    div.stButton > button:first-child:hover {
        background-color: #0066cc;
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Header text
st.markdown('<div class="header-text">Lean Six Sigma</div>', unsafe_allow_html=True)

# Embed the large dramatic video as header
video_url = "https://amundi-my.sharepoint.com/personal/sachin_singh_amundi_com/Documents/A_large_dramatic_202507231819.mp4?csf=1&web=1&nav=eyJyZWZlcnJhbEluZm8iOnsicmVmZXJyYWxBcHAiOiJPbmVEcml2ZUZvckJ1c2luZXNzIiwicmVmZXJyYWxBcHBQbGF0Zm9ybSI6IldlYiIsInJlZmVycmFsTW9kZSI6InZpZXciLCJyZWZlcnJhbFZpZXciOiJNeUZpbGVzTGlua0NvcHkifX0&e=UIxLho"

st.video(video_url, start_time=0)

# Phases list
phases = ["Define", "Measure", "Analyze", "Improve", "Control"]

# Display phases as clickable cards in columns
cols = st.columns(len(phases))
selected_phase = None
for i, phase in enumerate(phases):
    if cols[i].button(phase):
        selected_phase = phase

# If no phase selected yet, default to Define
if selected_phase is None:
    selected_phase = "Define"

# Define phase content and videos
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

def show_phase_content(phase):
    st.markdown(f"<div class='content-area'><h2>{phase} Phase: In-Depth Overview</h2>", unsafe_allow_html=True)
    if phase == "Define":
        for topic, info in define_topics.items():
            with st.expander(topic):
                st.markdown(info["content"])
                if st.button(f"See Video: {topic}", key=topic):
                    st.video(info["video"])
    else:
        st.info(f"Content for {phase} phase will be added soon.")
    st.markdown("</div>", unsafe_allow_html=True)

show_phase_content(selected_phase)
