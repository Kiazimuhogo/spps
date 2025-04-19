# Student Success Predictor

A Streamlit web application for predicting student academic performance based on various factors. This application provides data visualization, exploration, and machine learning predictions to help educators and administrators make data-driven decisions.

## Features

- 📊 **Interactive Dashboard**: Visualize key metrics and trends in student performance
- 🔍 **Data Exploration**: Analyze the dataset with custom visualizations and statistics
- 🎯 **Performance Prediction**: Predict student outcomes using machine learning
- 📱 **Responsive Design**: Works well on both desktop and mobile devices
- 📁 **File Upload**: Upload your own dataset for analysis
- 📈 **Custom Visualizations**: Create your own charts and graphs

## Project Structure

```
student_success_predictor/
├── src/
│   ├── app.py              # Main application file
│   ├── components/         # Reusable UI components
│   ├── utils/             # Utility functions
│   │   └── data_loader.py # Data loading and preprocessing
│   ├── models/            # Machine learning models
│   └── pages/             # Application pages
│       ├── dashboard.py   # Dashboard view
│       ├── data_exploration.py # Data exploration view
│       └── prediction.py  # Prediction form and results
├── static/               # Static assets
│   ├── css/             # Custom CSS styles
│   └── images/          # Images and icons
├── requirements.txt     # Python dependencies
└── README.md           # Project documentation
```

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/student_success_predictor.git
cd student_success_predictor
```

2. Create a virtual environment (optional but recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the application:
```bash
streamlit run src/app.py
```

## Usage

### Dashboard
The dashboard provides an overview of student performance metrics including:
- Total number of students
- Pass/Fail distribution
- Average scores
- Performance by various factors
- Correlation between different metrics

### Data Exploration
The data exploration page allows you to:
- View the raw dataset
- Generate basic statistics
- Create custom visualizations
- Download the data
- Analyze relationships between variables

### Prediction
The prediction page enables you to:
- Input student information
- Get performance predictions
- View feature importance
- Receive recommendations based on predictions

## Data Format
The application expects a CSV file with the following columns:
- Student_ID
- Gender
- Study_Hours_per_Week
- Attendance_Rate
- Past_Exam_Scores
- Parental_Education_Level
- Internet_Access_at_Home
- Extracurricular_Activities
- Final_Exam_Score
- Pass_Fail

## Machine Learning Model
The application uses a Random Forest Classifier to predict student performance. The model:
- Takes into account multiple features
- Provides probability scores
- Shows feature importance
- Generates personalized recommendations

## Contributing
1. Fork the repository
2. Create a new branch
3. Make your changes
4. Submit a pull request

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments
- Built with Streamlit
- Uses scikit-learn for machine learning
- Visualizations powered by Plotly 