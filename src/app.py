import streamlit as st
import pandas as pd
import numpy as np
from pages.dashboard import show_dashboard
from pages.data_exploration import show_data_exploration
from pages.prediction import show_prediction
from utils.data_loader import load_data

# Set page config
st.set_page_config(
    page_title="Student Success Predictor",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
    <style>
        .main {
            padding: 2rem;
        }
        .stApp {
            max-width: 1200px;
            margin: 0 auto;
        }
        .st-emotion-cache-1v0mbdj {
            width: 100%;
        }
        .st-emotion-cache-1wrcr25 {
            margin-bottom: 2rem;
        }
    </style>
""", unsafe_allow_html=True)

def main():
    # Sidebar
    with st.sidebar:
        st.title("📚 Navigation")
        
        # File uploader
        uploaded_file = st.file_uploader("Upload your CSV file", type=['csv'])
        
        if uploaded_file is not None:
            df = pd.read_csv(uploaded_file)
            st.session_state['data'] = df
            st.success("File uploaded successfully!")
        else:
            # Load default dataset
            df = load_data()
            st.session_state['data'] = df
        
        # Navigation
        page = st.radio(
            "Go to",
            ["Dashboard", "Data Exploration", "Make Prediction"]
        )
    
    # Main content
    if page == "Dashboard":
        show_dashboard()
    elif page == "Data Exploration":
        show_data_exploration()
    else:
        show_prediction()

if __name__ == "__main__":
    main() 