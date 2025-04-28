import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

def show_dashboard():
    st.subheader("📊 Student Performance Dashboard")
    
    # Get data from session state
    df = st.session_state.get('data')
    
    if df is None:
        st.warning("No data available. Please upload a CSV file.")
        return
    
    # Create three columns for key metrics
    col1, col2, col3 = st.columns(3)
    
    with col1:
        total_students = len(df)
        st.metric("Total Students", total_students)
        
    with col2:
        pass_rate = (df['Pass_Fail'] == 'Pass').mean() * 100
        st.metric("Pass Rate", f"{pass_rate:.1f}%")
        
    with col3:
        avg_score = df['Final_Exam_Score'].mean()
        st.metric("Average Score", f"{avg_score:.1f}")
    
    # Create two columns for charts
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Pass/Fail Distribution")
        fig_pass_fail = px.pie(
            df, 
            names='Pass_Fail',
            title='Pass/Fail Distribution',
            color_discrete_sequence=px.colors.qualitative.Set3
        )
        st.plotly_chart(fig_pass_fail, use_container_width=True)
        
    with col2:
        st.subheader("Score Distribution")
        fig_score_dist = px.histogram(
            df,
            x='Final_Exam_Score',
            nbins=20,
            title='Final Exam Score Distribution',
            color_discrete_sequence=['#3366CC']
        )
        st.plotly_chart(fig_score_dist, use_container_width=True)
    
    # Create two more columns for additional charts
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Average Score by Education Level")
        avg_by_edu = df.groupby('Parental_Education_Level')['Final_Exam_Score'].mean().reset_index()
        fig_edu = px.bar(
            avg_by_edu,
            x='Parental_Education_Level',
            y='Final_Exam_Score',
            title='Average Score by Parental Education Level',
            color_discrete_sequence=['#FF9999']
        )
        st.plotly_chart(fig_edu, use_container_width=True)
        
    with col2:
        st.subheader("Study Hours vs Final Score")
        fig_scatter = px.scatter(
            df,
            x='Study_Hours_per_Week',
            y='Final_Exam_Score',
            color='Pass_Fail',
            title='Study Hours vs Final Score',
            trendline="ols"
        )
        st.plotly_chart(fig_scatter, use_container_width=True)
    
    # Show correlation heatmap
    st.subheader("Feature Correlation")
    numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns
    corr_matrix = df[numeric_cols].corr()
    
    fig_corr = go.Figure(data=go.Heatmap(
        z=corr_matrix,
        x=corr_matrix.columns,
        y=corr_matrix.columns,
        colorscale='RdBu',
        zmin=-1,
        zmax=1
    ))
    fig_corr.update_layout(title='Correlation Matrix')
    st.plotly_chart(fig_corr, use_container_width=True) 