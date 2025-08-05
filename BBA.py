import streamlit as st

st.set_page_config(page_title="Lean Six Sigma Circular Phases", layout="wide")

# CSS for circular layout and styling
st.markdown(
    """
    <style>
    .circle-container {
        position: relative;
        width: 400px;
        height: 400px;
        margin: 2rem auto 3rem auto;
    }
    .circle-item {
        position: absolute;
        width: 120px;
        height: 120px;
        background: linear-gradient(135deg, #0073e6, #004080);
        color: white;
        border-radius: 50%;
        display: flex;
        justify-content: center;
        align-items: center;
        font-weight: 700;
        font-size: 1.1rem;
        cursor: pointer;
        box-shadow: 0 4px 12px rgba(0,0,0,0.2);
        transition: transform 0.3s ease, box-shadow 0.3s ease;
        user-select: none;
        text-align: center;
        padding: 10px;
    }
    .circle-item:hover {
        transform: scale(1.1);
        box-shadow: 0 8px 20px rgba(0,0,0,0.3);
    }
    /* Positions for 5 items in circle */
    .pos-define { top: 10%; left: 40%; }
    .pos-measure { top: 35%; left: 75%; }
    .pos-analyze { top: 70%; left: 60%; }
    .pos-improve { top: 70%; left: 15%; }
    .pos-control { top: 35%; left: 5%; }

    /* Selected phase style */
    .selected {
        background: linear-gradient(135deg, #0059b3, #003366);
        box-shadow: 0 0 15px 5px #003366;
        transform: scale(1.2);
        z-index: 10;
    }

    /* Content container */
    .content-container {
        max-width: 900px;
        margin: 0 auto 3rem auto;
        background-color: white;
        padding: 2rem 3rem;
        border-radius: 15px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.1);
        color: #222222;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    h2 {
        color: #004080;
        font-weight: 700;
        margin-bottom: 1rem;
    }
    ul {
        margin-left: 1.5rem;
        margin-bottom: 1.5rem;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Title
st.markdown('<h1 style="text-align:center; color:#004080; font-family:Segoe UI, Tahoma, Geneva, Verdana, sans-serif;">Lean Six Sigma</h1>', unsafe_allow_html=True)

# Define phases and their positions
phases = [
    ("Define", "pos-define"),
    ("Measure", "pos-measure"),
    ("Analyze", "pos-analyze"),
    ("Improve", "pos-improve"),
    ("Control", "pos-control"),
]

# Initialize session state for selected phase
if "selected_phase" not in st.session_state:
    st.session_state.selected_phase = "Define"

# Function to render the circle with clickable phases
def render_circle(selected):
    html = '<div class="circle-container">'
    for phase, pos in phases:
        cls = "circle-item " + pos
        if phase == selected:
            cls += " selected"
        # Use a clickable div with onclick to send phase name to Streamlit via query params
        # Since Streamlit can't handle JS events directly, we use buttons below instead
        html += f'<div class="{cls}" id="{phase}">{phase}</div>'
    html += "</div>"
    st.markdown(html, unsafe_allow_html=True)

# Render the circle (non-clickable, just for visual)
render_circle(st.session_state.selected_phase)

# Below the circle, create buttons for each phase to handle clicks
cols = st.columns(len(phases))
for i, (phase, _) in enumerate(phases):
    if cols[i].button(phase):
        st.session_state.selected_phase = phase

# Content for each phase (example content for Define, placeholders for others)
phase_contents = {
    "Define": {
        "What is the Define Phase?
The Define phase is the first step in the Lean Six Sigma DMAIC methodology. Its purpose is to clearly identify and articulate the problem or opportunity for improvement, align the project with business goals, and set a clear scope and objectives. This phase establishes a solid foundation for the project by understanding customer needs, defining measurable goals, and organizing the project team..
""",
        "Identify the Problem or Opportunity": """
- Understand the current situation and why improvement is needed.
- Develop a clear and concise Problem Statement that describes the issue in measurable terms.
""",
        "Define the Project Goal": """
- Create a Goal Statement that specifies what the project aims to achieve.
- Goals should be SMART: Specific, Measurable, Achievable, Relevant, and Time-bound.
""",
        "Determine the Project Scope": """
- Define boundaries to avoid scope creep.
- Specify what is included and excluded from the project.
""",
        "Identify Customers and Their Requirements": """
- Internal and external customers.
- Gather Voice of Customer (VOC) data to understand customer needs and expectations.
""",
        "Develop a High-Level Process Map": """
- Use SIPOC or other mapping tools to visualize the process.
- Identify key inputs, outputs, and stakeholders.
""",
        "Form the Project Team": """
- Assign roles such as Sponsor, Champion, Black Belt, Green Belt, and process owners.
- Clarify responsibilities and communication plans.
""",
        "Develop the Project Charter": """
- Document all the above elements.
- Obtain formal approval from stakeholders.
""",
    },
    "Measure": {"Content": "Content for Measure phase will be added soon."},
    "Analyze": {"Content": "Content for Analyze phase will be added soon."},
    "Improve": {"Content": "Content for Improve phase will be added soon."},
    "Control": {"Content": "Content for Control phase will be added soon."},
}

# Display content container
st.markdown('<div class="content-container">', unsafe_allow_html=True)
st.markdown(f"<h2>{st.session_state.selected_phase} Phase: In-Depth Overview</h2>", unsafe_allow_html=True)

content = phase_contents.get(st.session_state.selected_phase, {"Content": "Content coming soon."})

if st.session_state.selected_phase == "Define":
    for topic, text in content.items():
        with st.expander(topic):
            st.markdown(text)
else:
    st.info(content.get("Content"))

st.markdown("</div>", unsafe_allow_html=True)
