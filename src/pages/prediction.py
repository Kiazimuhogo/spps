import streamlit as st
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from utils.data_loader import preprocess_data, get_feature_importance
import plotly.express as px

def train_model(df):
    """Train the prediction model"""
    # Preprocess the data
    df_processed = preprocess_data(df)
    
    # Prepare features and target
    features = ['Study_Hours_per_Week', 'Attendance_Rate', 'Past_Exam_Scores',
                'Gender', 'Parental_Education_Level', 'Internet_Access_at_Home',
                'Extracurricular_Activities']
    
    X = df_processed[features]
    y = df_processed['Pass_Fail']
    
    # Train the model
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X, y)
    
    return model, features

def show_prediction():
    st.title("🎯 Student Performance Prediction")
    
    # Get data from session state
    df = st.session_state.get('data')
    
    if df is None:
        st.warning("No data available. Please upload a CSV file.")
        return
    
    # Train the model
    model, features = train_model(df)
    
    # Create the prediction form
    st.write("""
    ### Enter Student Information
    Please fill in the following information to predict the student's performance.
    """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        study_hours = st.number_input("Study Hours per Week", min_value=0, max_value=40, value=20)
        attendance = st.number_input("Attendance Rate (%)", min_value=0, max_value=100, value=75)
        past_scores = st.number_input("Past Exam Scores", min_value=0, max_value=100, value=70)
        gender = st.selectbox("Gender", ["Male", "Female"])
    
    with col2:
        education = st.selectbox("Parental Education Level", 
                               ["High School", "Bachelors", "Masters", "PhD"])
        internet = st.selectbox("Internet Access at Home", ["Yes", "No"])
        activities = st.selectbox("Extracurricular Activities", ["Yes", "No"])
    
    # Create a prediction button
    if st.button("Predict Performance"):
        # Prepare the input data
        input_data = pd.DataFrame({
            'Study_Hours_per_Week': [study_hours],
            'Attendance_Rate': [attendance],
            'Past_Exam_Scores': [past_scores],
            'Gender': [gender],
            'Parental_Education_Level': [education],
            'Internet_Access_at_Home': [internet],
            'Extracurricular_Activities': [activities]
        })
        
        # Preprocess input data
        input_processed = preprocess_data(input_data)
        
        # Make prediction
        prediction = model.predict(input_processed[features])
        probability = model.predict_proba(input_processed[features])
        
        # Show prediction results
        st.write("### Prediction Results")
        
        # Create columns for results
        col1, col2 = st.columns(2)
        
        with col1:
            result = "Pass" if prediction[0] == 1 else "Fail"
            st.metric("Predicted Outcome", result)
            
        with col2:
            pass_prob = probability[0][1] * 100
            st.metric("Probability of Passing", f"{pass_prob:.1f}%")
        
        # Show feature importance
        st.write("### Feature Importance")
        importance = get_feature_importance(model, features)
        
        if importance:
            importance_df = pd.DataFrame({
                'Feature': importance.keys(),
                'Importance': importance.values()
            }).sort_values('Importance', ascending=False)
            
            fig = px.bar(importance_df, x='Feature', y='Importance',
                        title='Feature Importance in Prediction')
            st.plotly_chart(fig, use_container_width=True)
        
        # Add recommendations based on the prediction
        st.write("### Recommendations")
        if result == "Fail":
            st.warning("""
            Based on the prediction, the student might need additional support. Here are some recommendations:
            - Increase study hours per week
            - Improve attendance rate
            - Seek additional academic support
            - Consider joining study groups
            """)
        else:
            st.success("""
            The student is predicted to pass! To maintain this performance:
            - Continue with the current study routine
            - Maintain good attendance
            - Stay engaged in class activities
            - Keep up the good work!
            """) 