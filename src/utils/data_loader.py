import pandas as pd
import os

def load_data():
    """Load the default student dataset"""
    try:
        # Get the absolute path to the data directory
        current_dir = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
        data_path = os.path.join(current_dir, 'student_dataset.csv')
        
        # Read the CSV file
        df = pd.read_csv(data_path)
        return df
    except Exception as e:
        print(f"Error loading data: {e}")
        return None

def preprocess_data(df):
    """Preprocess the data for model training"""
    # Create a copy of the dataframe
    df_processed = df.copy()
    
    # Convert categorical variables to numerical
    categorical_columns = ['Gender', 'Parental_Education_Level', 'Internet_Access_at_Home', 
                         'Extracurricular_Activities', 'Pass_Fail']
    
    for col in categorical_columns:
        if col in df_processed.columns:
            df_processed[col] = pd.Categorical(df_processed[col]).codes
    
    return df_processed

def get_feature_importance(model, feature_names):
    """Get feature importance from the model"""
    try:
        importance = model.feature_importances_
        return dict(zip(feature_names, importance))
    except:
        try:
            importance = abs(model.coef_[0])
            return dict(zip(feature_names, importance))
        except:
            return None 