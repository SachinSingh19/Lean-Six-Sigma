import streamlit as st

# Title
st.title("Lean Six Sigma")

# Sidebar or horizontal menu for phases
phases = ["Define", "Measure", "Analyze", "Improve", "Control"]
selected_phase = st.radio("Select Phase", phases, horizontal=True)

# Content for Define phase
define_content = """
### Define Phase: In-Depth Overview

**Purpose of the Define Phase**
- To identify and clearly articulate the problem or opportunity for improvement.
- To align the project with business goals and customer needs.
- To establish a clear project scope and objectives.
- To form a capable project team with defined roles and responsibilities.
- To set the foundation for data collection and analysis in later phases.

**Key Activities in the Define Phase**

**Identify the Problem or Opportunity**
- Understand the current situation and why improvement is needed.
- Develop a clear and concise Problem Statement that describes the issue in measurable terms.

**Define the Project Goal**
- Create a Goal Statement that specifies what the project aims to achieve.
- Goals should be SMART: Specific, Measurable, Achievable, Relevant, and Time-bound.

**Determine the Project Scope**
- Define boundaries to avoid scope creep.
- Specify what is included and excluded from the project.

**Identify Customers and Their Requirements**
- Internal and external customers.
- Gather Voice of Customer (VOC) data to understand customer needs and expectations.

**Develop a High-Level Process Map**
- Use SIPOC or other mapping tools to visualize the process.
- Identify key inputs, outputs, and stakeholders.

**Form the Project Team**
- Assign roles such as Sponsor, Champion, Black Belt, Green Belt, and process owners.
- Clarify responsibilities and communication plans.

**Develop the Project Charter**
- Document all the above elements.
- Obtain formal approval from stakeholders.
"""

# Example video URLs related to Define phase (YouTube links)
define_videos = [
    "https://www.youtube.com/embed/3v5v6v6v6v6",  # Replace with actual video URLs
    "https://www.youtube.com/embed/4x4x4x4x4x4"
]

# Display content based on selected phase
if selected_phase == "Define":
    st.markdown(define_content)
    st.markdown("### Videos related to Define Phase")
    for video_url in define_videos:
        st.video(video_url)
else:
    st.info(f"Content for {selected_phase} phase will be added soon.")
