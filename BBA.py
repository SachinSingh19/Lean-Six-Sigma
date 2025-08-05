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
    /* Header */
    .header {
        background-color: #004080;
        padding: 2rem 1rem;
        color: white;
        text-align: center;
        border-radius: 0 0 20px 20px;
        font-weight: 700;
        font-size: 3rem;
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

    
