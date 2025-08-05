import streamlit as st

st.set_page_config(page_title="Lean Six Sigma Circular Layout", layout="wide")

# CSS for circle layout and styling buttons as circles
st.markdown(
    """
    <style>
    .circle-container {
        position: relative;
        width: 450px;
        height: 450px;
        margin: 2rem auto 3rem auto;
        border: 4px solid #004080;
        border-radius: 50%;
        background: radial-gradient(circle at center, #e6f0ff 60%, transparent 100%);
    }
    /* Style for buttons as circles */
    div.stButton > button {
        background: linear-gradient(135deg, #0073e6, #004080);
        color: white;
        border-radius: 50%;
        width: 110px;
        height: 110px;
        font-weight: 700;
        font-size: 1.1rem;
        cursor: pointer;
        box-shadow: 0 4px 12px rgba(0,0,0,0.2);
        transition: transform 0.3s ease, box-shadow 0.3s ease;
        user-select: none;
        text-transform: uppercase;
        letter-spacing: 1.2px;
        border: 3px solid transparent;
        display: flex;
        justify-content: center;
        align-items: center;
        text-align: center;
        padding: 10px;
        margin: 0 auto;
    }
    div.stButton > button:hover {
        transform: scale(1.1);
        box-shadow: 0 8px 20px rgba(0,0,0,0.3);
    }
    /* Selected button style */
    div.stButton > button.selected {
        background: linear-gradient(135deg, #0059b3, #003366) !important;
        box-shadow: 0 0 20px 6px #003366 !important;
        transform: scale(1.2) !important;
        border-color: #001f4d !important;
        z-index: 10;
    }
    /* Positions for buttons in circle using flexbox and margin */
    .circle-row {
        display: flex;
        justify-content: center;
        align-items: center;
        margin: 0;
        padding: 0;
    }
    .circle-row.top {
        margin-bottom: 40px;
    }
    .circle-row.middle {
        justify-content: space-between;
        margin-bottom: 40px;
    }
    .circle-row.bottom {
        justify-content: center;
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

# Function to render buttons arranged in a circle-like layout using rows
def render_circle_buttons(selected_phase):
    # Top row: Define
    cols_top = st.columns([1, 1, 1, 1, 1])
    with cols_top[2]:
        if st.button("Define", key="Define", help="Define Phase"):
            st.session_state.selected_phase = "Define"
    # Middle row: Control and Measure
    cols_middle = st.columns([1, 1, 1, 1, 1])
    with cols_middle[0]:
        if st.button("Control", key="Control", help="Control Phase"):
            st.session_state.selected_phase = "Control"
    with cols_middle[4]:
        if st.button("Measure", key="Measure", help="Measure Phase"):
            st.session_state.selected_phase = "Measure"
    # Bottom row: Improve and Analyze
    cols_bottom = st.columns([1, 1, 1, 1, 1])
    with cols_bottom[1]:
        if st.button("Improve", key="Improve", help="Improve Phase"):
            st.session_state.selected_phase = "Improve"
    with cols_bottom[3]:
        if st.button("Analyze", key="Analyze", help="Analyze Phase"):
            st.session_state.selected_phase = "Analyze"

    # Add CSS to highlight selected button
    # Streamlit doesn't allow direct class manipulation, so we use JS injection hack
    # But here we use a workaround: re-render buttons with selected class by injecting CSS targeting button text

    # Inject JS to add 'selected' class to the selected button
    st.markdown(
        f"""
        <script>
        const buttons = window.parent.document.querySelectorAll('button[kind="primary"]');
        buttons.forEach(btn => {{
            if(btn.innerText.toLowerCase() === "{selected_phase.lower()}") {{
                btn.classList.add('selected');
            }} else {{
                btn.classList.remove('selected');
            }}
        }});
        </script>
        """,
        unsafe_allow_html=True,
    )

render_circle_buttons(st.session_state.selected_phase)

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
