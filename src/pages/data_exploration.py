import streamlit as st
import plotly.express as px
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from io import StringIO

def show_data_exploration():
    st.title("🔍 Data Exploration")
    
    # Get data from session state
    df = st.session_state.get('data')
    
    if df is None:
        st.warning("No data available. Please upload a CSV file.")
        return
    
    # Add a description
    st.write("""
    This page allows you to explore the student performance dataset in detail.
    You can view the raw data, basic statistics, and create custom visualizations.
    """)
    
    # Show data overview
    st.subheader("📋 Data Overview")
    
    # Create tabs for different views
    tab1, tab2, tab3 = st.tabs(["Raw Data", "Statistics", "Custom Visualization"])
    
    with tab1:
        st.dataframe(df, use_container_width=True)
        
        # Add download button
        csv = df.to_csv(index=False)
        st.download_button(
            label="Download Data as CSV",
            data=csv,
            file_name='student_data.csv',
            mime='text/csv',
        )
    
    with tab2:
        # Show basic statistics
        st.write("Basic Statistics:")
        st.dataframe(df.describe(), use_container_width=True)
        
        # Show data info
        st.write("Dataset Information:")
        buffer = StringIO()
        df.info(buf=buffer)
        st.text(buffer.getvalue())
        
        # Show missing values
        st.write("Missing Values:")
        missing_values = df.isnull().sum()
        st.dataframe(missing_values, use_container_width=True)
    
    with tab3:
        st.write("Create your own visualization:")
        
        # Select chart type
        chart_type = st.selectbox(
            "Select Chart Type",
            ["Scatter Plot", "Bar Chart", "Box Plot", "Violin Plot", "Line Plot"]
        )
        
        # Select variables
        numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns
        categorical_cols = df.select_dtypes(include=['object']).columns
        
        if chart_type == "Scatter Plot":
            x_var = st.selectbox("Select X variable", numeric_cols)
            y_var = st.selectbox("Select Y variable", numeric_cols)
            color_var = st.selectbox("Select Color variable", categorical_cols)
            
            fig = px.scatter(df, x=x_var, y=y_var, color=color_var,
                           title=f"{x_var} vs {y_var} by {color_var}")
            st.plotly_chart(fig, use_container_width=True)
            
        elif chart_type == "Bar Chart":
            x_var = st.selectbox("Select X variable", categorical_cols)
            y_var = st.selectbox("Select Y variable", numeric_cols)
            
            fig = px.bar(df, x=x_var, y=y_var,
                        title=f"Average {y_var} by {x_var}")
            st.plotly_chart(fig, use_container_width=True)
            
        elif chart_type in ["Box Plot", "Violin Plot"]:
            x_var = st.selectbox("Select X variable", categorical_cols)
            y_var = st.selectbox("Select Y variable", numeric_cols)
            
            if chart_type == "Box Plot":
                fig = px.box(df, x=x_var, y=y_var,
                           title=f"Distribution of {y_var} by {x_var}")
            else:
                fig = px.violin(df, x=x_var, y=y_var,
                              title=f"Distribution of {y_var} by {x_var}")
            st.plotly_chart(fig, use_container_width=True)
            
        elif chart_type == "Line Plot":
            x_var = st.selectbox("Select X variable", numeric_cols)
            y_var = st.selectbox("Select Y variable", numeric_cols)
            
            fig = px.line(df, x=x_var, y=y_var,
                         title=f"Trend of {y_var} vs {x_var}")
            st.plotly_chart(fig, use_container_width=True)
    
    # Additional Analysis Section
    st.subheader("📊 Additional Analysis")
    
    # Feature relationships
    st.write("### Feature Relationships")
    feature_cols = st.multiselect(
        "Select features to analyze",
        df.columns.tolist(),
        default=df.select_dtypes(include=['float64', 'int64']).columns[:3].tolist()
    )
    
    if len(feature_cols) > 1:
        fig = px.scatter_matrix(
            df,
            dimensions=feature_cols,
            title="Feature Relationships Matrix"
        )
        st.plotly_chart(fig, use_container_width=True) 