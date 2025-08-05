import streamlit as st

st.set_page_config(page_title="Lean Six Sigma Circular Layout", layout="wide")

# CSS for circle layout and styling
st.markdown(
    """
    <style>
    .circle-wrapper {
        position: relative;
        width: 450px;
        height: 450px;
        margin: 2rem auto 3rem auto;
        border: 4px solid #004080;
        border-radius: 50%;
        background: radial-gradient(circle at center, #e6f0ff 60%, transparent 100%);
    }
    .phase-circle {
        position: absolute;
        width: 110px;
        height: 110px;
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
        text-align: center;
        padding: 10px;
        user-select: none;
        text-transform: uppercase;
        letter-spacing: 1.2px;
        border: 3px solid transparent;
    }
    .phase-circle:hover {
        transform: scale(1.1);
        box-shadow: 0 8px 20px rgba(0,0,0,0.3);
    }
    .selected {
        background: linear-gradient(135deg, #0059b3, #003366) !important;
        box-shadow: 0 0 20px 6px #003366 !important;
        transform: scale(1.2) !important;
        border-color: #001f4d !important;
        z-index: 10;
    }
    /* Positions for 5 phases evenly spaced on circle */
    #Define {
        top: 10%;
        left: 50%;
        transform: translate(-50%, -50%);
    }
    #Measure {
        top: 35%;
        left: 85%;
        transform: translate(-50%, -50%);
    }
    #Analyze {
        top: 75%;
        left: 75%;
        transform: translate(-50%, -50%);
    }
    #Improve {
        top: 75%;
        left: 25%;
        transform: translate(-50%, -50%);
    }
    #Control {
        top: 35%;
        left: 15%;
        transform: translate(-50%, -50%);
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
st.markdown(
    '<h1 style="text-align:center; color:#004080; font-family:Segoe UI, Tahoma, Geneva, Verdana, sans-serif;">Lean Six Sigma</h1>',
    unsafe_allow_html=True,
)

# Phases list
phases = ["Define", "Measure", "Analyze", "Improve", "Control"]

# Initialize session state for selected phase
if "selected_phase" not in st.session_state:
    st.session_state.selected_phase = "Define"

# Render the circle with phases as HTML divs
circle_html = '<div class="circle-wrapper">'
for phase in phases:
    selected_class = "phase-circle selected" if phase == st.session_state.selected_phase else "phase-circle"
    # Each div has an id for CSS positioning and a data-phase attribute for JS (not used here)
    circle_html += f'<form method="post"><button name="phase" value="{phase}" class="{selected_class}" id="{phase}">{phase}</button></form>'
circle_html += "</div>"

st.markdown(circle_html, unsafe_allow_html=True)

# Capture button clicks via form submission
clicked_phase = st.experimental_get_query_params().get("phase", [None])[0]

# Streamlit doesn't support form button clicks inside markdown, so we use st.form workaround:
# Instead, we create invisible buttons below the circle to capture clicks and sync with circle buttons visually.

# Alternative approach: Use st.form with buttons for each phase, styled to be invisible, and sync selection.

with st.form("phase_form"):
    cols = st.columns(5)
    for i, phase in enumerate(phases):
        if cols[i].form_submit_button(phase):
            st.session_state.selected_phase = phase
    st.form_submit_button("Submit", disabled=True, key="dummy")  # Dummy to keep form valid

# Content for each phase (example content for Define, placeholders for others)
phase_contents = {
    "Define": {
        "Purpose of the Define Phase": """
- To identify and clearly articulate the problem or opportunity for improvement.
- To align the project with business goals and customer needs.
- To establish a clear project scope and objectives.
- To form a capable project team with defined roles and responsibilities.
- To set the foundation for data collection and analysis in later phases.
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
