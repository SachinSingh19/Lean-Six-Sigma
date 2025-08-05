import streamlit as st

st.set_page_config(page_title="Lean Six Sigma Circular Phases", layout="wide")

# CSS for circular layout and styling buttons as circles
st.markdown(
    """
    <style>
    .circle-container {
        position: relative;
        width: 400px;
        height: 400px;
        margin: 2rem auto 3rem auto;
    }
    /* Hide default Streamlit button style */
    div.stButton > button {
        all: unset;
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
        text-transform: uppercase;
        letter-spacing: 1.2px;
        border: 3px solid transparent;
    }
    div.stButton > button:hover {
        transform: scale(1.1);
        box-shadow: 0 8px 20px rgba(0,0,0,0.3);
    }
    /* Positions for 5 items in circle */
    #Define {
        top: 10%;
        left: 40%;
    }
    #Measure {
        top: 35%;
        left: 75%;
    }
    #Analyze {
        top: 70%;
        left: 60%;
    }
    #Improve {
        top: 70%;
        left: 15%;
    }
    #Control {
        top: 35%;
        left: 5%;
    }
    /* Selected phase style */
    .selected {
        background: linear-gradient(135deg, #0059b3, #003366) !important;
        box-shadow: 0 0 15px 5px #003366 !important;
        transform: scale(1.2) !important;
        z-index: 10 !important;
        border-color: #001f4d !important;
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

# Define phases and their positions (ids for buttons)
phases = ["Define", "Measure", "Analyze", "Improve", "Control"]

# Initialize session state for selected phase
if "selected_phase" not in st.session_state:
    st.session_state.selected_phase = "Define"

# Container for circle buttons
circle_container = st.container()

with circle_container:
    st.markdown('<div class="circle-container">', unsafe_allow_html=True)
    # Render buttons with ids for CSS positioning
    for phase in phases:
        is_selected = (phase == st.session_state.selected_phase)
        btn_key = f"btn_{phase}"
        # Use st.button with key and id for CSS
        # We use st.markdown + st.button hack to assign id to button container
        # So we create a div with id and put button inside
        # But Streamlit doesn't allow id on button, so we use st.markdown + st.button side by side
        # Instead, we use st.button and style by key with CSS attribute selectors
        # So we add a style block to target buttons by key attribute
        # But Streamlit doesn't expose key as attribute, so we rely on button text and nth-child
        # Instead, we create invisible buttons and overlay divs with onclick JS to trigger Streamlit rerun
        # This is complex, so we do a simpler approach: render buttons normally and position by nth-child
        pass
    st.markdown('</div>', unsafe_allow_html=True)

# Because Streamlit buttons cannot be positioned absolutely with unique ids easily,
# we will create 5 columns and position buttons inside with CSS margin to simulate circle.

# Alternative approach: Use columns with CSS margin to simulate circle

col1, col2, col3, col4, col5 = st.columns(5)

# Map phases to columns and add margin-top to simulate circle shape
col_positions = {
    "Define": (col3, "margin-top: 0px;"),
    "Measure": (col4, "margin-top: 50px;"),
    "Analyze": (col5, "margin-top: 100px;"),
    "Improve": (col1, "margin-top: 100px;"),
    "Control": (col2, "margin-top: 50px;"),
}

for phase in phases:
    col, style = col_positions[phase]
    is_selected = (phase == st.session_state.selected_phase)
    btn_style = (
        "background: linear-gradient(135deg, #0059b3, #003366); color: white; font-weight: 700; font-size: 1.1rem; "
        "border-radius: 50%; width: 120px; height: 120px; margin: auto; display: flex; justify-content: center; align-items: center; "
        "box-shadow: 0 0 15px 5px #003366; transform: scale(1.2); cursor: pointer; border: 3px solid #001f4d;"
        if is_selected
        else "background: linear-gradient(135deg, #0073e6, #004080); color: white; font-weight: 700; font-size: 1.1rem; "
        "border-radius: 50%; width: 120px; height: 120px; margin: auto; display: flex; justify-content: center; align-items: center; "
        "box-shadow: 0 4px 12px rgba(0,0,0,0.2); cursor: pointer; border: 3px solid transparent;"
    )
    if col.button(phase, key=phase):
        st.session_state.selected_phase = phase
    # Inject style for the last button clicked to simulate circle position margin-top
    # We can't style buttons directly, so we add a spacer above buttons
    col.markdown(f'<div style="{style}"></div>', unsafe_allow_html=True)

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
st.markdown(
    """
    <style>
    .content-container {
        max-width: 900px;
        margin: 2rem auto 3rem auto;
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
