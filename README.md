# Classification and regression task using Saint-Petersburg real estate dataset
- [Описание на русском]()
- [Description en francais]()
  
## Project Overview

This project aims to analyze the Saint-Petersburg real estate market using a machine learning pipeline. The goal is to develop models for both classification and regression tasks, leveraging the real estate data to predict property prices (regression) and classify property types (classification).

## Table of Contents
- [Project Overview](#project-overview)
- [Dataset](#dataset)
- [Project Workflow](#project-workflow)
- [Installation](#installation)
- [Usage](#usage)
- [Results](#results)
- [Future Work](#future-work)
- [Contributing](#contributing)
- [License](#license)

## Dataset

The dataset provides information on real estate listings in Saint-Petersburg, including:
- **Numerical features**: price, area, rooms, floor, total floors, etc.
- **Categorical features**: district, property type, and others.


## Project Workflow

### 1. Data Collection and Understanding

Load and inspect the dataset to understand its structure, feature types, and any target variables.

### 2. Data Preprocessing

- **Handle missing values**: Remove or impute missing data based on analysis.
- **Outlier detection**: Identify and address outliers, especially in features like price and area.
- **Encoding categorical variables**: Encode categorical features using one-hot encoding or label encoding.

```python
# Example of handling missing values
df.fillna(df.mean(), inplace=True)
```

### 3. Exploratory Data Analysis (EDA)

Conduct EDA to understand feature distributions and correlations. Visualize the data to explore trends and patterns.

### 4. Feature Engineering

Generate new features based on domain knowledge, such as price per square meter or proximity to central areas. Feature engineering may improve model performance by adding useful information.

### 5. Modeling

#### Classification Task
Predict the property type (e.g., apartment, house) using a classification model such as Random Forest or Logistic Regression.

#### Regression Task
Predict the price of the property based on its characteristics using a regression model like Linear Regression or Gradient Boosting.

### 6. Model Evaluation

Assess model performance using metrics appropriate for each task:
- **Classification**: Use accuracy, precision, recall, F1-score.
- **Regression**: Use metrics such as RMSE, MAE, and \( R^2 \) score.

### 7. Hyperparameter Tuning

Use grid search or randomized search to optimize the hyperparameters of the models.

### 8. Save the Model

Save the trained models for deployment or future use.

## Installation

1. Clone the repository:
   ```bash
  
   ```

2. Install the required libraries:
   ```bash
   pip install -r requirements.txt
   ```

The results for classification and regression tasks will be printed, and the trained models will be saved in the project directory.

## Results

### Classification

| Metric   | Score |
|----------|-------|
| Accuracy | XX%   |
| F1 Score | XX    |

### Regression

| Metric        | Score |
|---------------|-------|
| RMSE          | XX    |
| MAE           | XX    |
| \( R^2 \) Score | XX |

## Future Work

- Implement more advanced feature engineering, such as location-based proximity analysis.
- Experiment with more complex models, like Neural Networks and XGBoost.
- Optimize models for deployment in a web application or API.

## Contributing

Contributions are welcome! Please fork this repository and submit a pull request if you have any ideas or improvements.

## License

This project is licensed under the MIT License.
