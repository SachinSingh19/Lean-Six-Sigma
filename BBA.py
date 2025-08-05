import streamlit as st

# Page config
st.set_page_config(page_title="Lean Six Sigma", layout="wide")

# Custom CSS to replicate LSSA style
st.markdown(
    """
    <style>
    /* Body and font */
    body, .main {
        font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
        background-color: #f9f9f9;
        color: #333333;
    }
    /* Header */
    .header {
        background-color: #004080;
        padding: 1.5rem 2rem;
        color: white;
        font-size: 2.5rem;
        font-weight: 700;
        letter-spacing: 1.5px;
        border-radius: 0 0 15px 15px;
        text-align: center;
        margin-bottom: 2rem;
    }
    /* Navigation bar */
    .nav-bar {
        display: flex;
        justify-content: center;
        gap: 2rem;
        margin-bottom: 2rem;
    }
    .nav-button {
        background-color: transparent;
        border: none;
        font-size: 1.1rem;
        font-weight: 600;
        color: #004080;
        padding: 0.5rem 1rem;
        cursor: pointer;
        border-bottom: 3px solid transparent;
        transition: border-color 0.3s ease;
    }
    .nav-button:hover {
        border-bottom: 3px solid #0073e6;
    }
    .nav-button.selected {
        border-bottom: 3px solid #004080;
        font-weight: 700;
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
    }
    /* Section titles */
    h2 {
        color: #004080;
        font-weight: 700;
        margin-top: 1.5rem;
        margin-bottom: 1rem;
    }
    /* Lists */
    ul {
        margin-left: 1.5rem;
        margin-bottom: 1.5rem;
    }
    /* Expanders */
    .streamlit-expanderHeader {
        font-weight: 600 !important;
        font-size: 1.15rem !important;
        color: #004080 !important;
    }
    /* Buttons */
    div.stButton > button:first-child {
        background-color: #004080;
        color: white;
        border-radius: 8px;
        padding: 0.5rem 1.5rem;
        font-weight: 600;
        transition: background-color 0.3s ease;
        margin-top: 1rem;
    }
    div.stButton > button:first-child:hover {
        background-color: #0073e6;
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Header
st.markdown('<div class="header">Lean Six Sigma</div>', unsafe_allow_html=True)

# Navigation bar with phases
phases = ["Define", "Measure", "Analyze", "Improve", "Control"]

# Use session state to keep track of selected phase
if "selected_phase" not in st.session_state:
    st.session_state.selected_phase = "Define"

# Navigation buttons
nav_cols = st.columns(len(phases))
for i, phase in enumerate(phases):
    is_selected = (phase == st.session_state.selected_phase)
    btn_class = "nav-button selected" if is_selected else "nav-button"
    # Use markdown with button styling
    if nav_cols[i].button(phase):
        st.session_state.selected_phase = phase

# Content for Define phase (your provided content)
define_content = {
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
}

# Placeholder content for other phases
other_phase_content = "Content for this phase will be added soon."

# Content container
st.markdown('<div class="content-container">', unsafe_allow_html=True)

st.markdown(f"## {st.session_state.selected_phase} Phase: In-Depth Overview")

if st.session_state.selected_phase == "Define":
    for topic, content in define_content.items():
        with st.expander(topic):
            st.markdown(content)
else:
    st.info(other_phase_content)

st.markdown("</div>", unsafe_allow_html=True)
