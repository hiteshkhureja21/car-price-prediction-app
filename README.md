# Car Price Prediction Project

A beginner-friendly Machine Learning project using Regression algorithms to predict the resale price of used cars, based on popular Kaggle datasets. Perfect for a college 1st-year Data Science project!

## 📌 Problem Statement
Predicting the fair resale price of a used car given some basic features. This helps both **buyers** and **sellers** estimate fair market values so they aren't losing money in the trade.

**Problem Type:** Regression (Because we are predicting a continuous number/price).

## 📊 Dataset Features
For ease of use, we provide a `generate_dataset.py` script that creates a 1000-row clean dataset closely resembling actual Kaggle used car datasets. 
The input features are:
1. `Brand`: Company (Maruti Suzuki, Hyundai, Tata, Mahindra, Kia, etc.)
2. `Model`: The specific vehicle model (e.g., Creta, Nexon, Swift).
3. `Original_Price`: The price the car was bought at new.
4. `Num_Owners`: Number of previous owners (1, 2, 3...).
5. `Has_Dents`: Does the car have dents? (Yes/No).
6. `Has_Scratches`: Does the car have scratches? (Yes/No).
7. `Mileage`: How much the car has been driven (in kilometers).
8. `Engine_Type`: Fuel type (Petrol, Diesel, CNG, Electric).
9. `Age_of_Vehicle`: How many years old the car is.

*Output/Target Feature:* `Price` (Resale value of the car).

## 🧠 Machine Learning Techniques Used
1. **Linear Regression:** A traditional, easy-to-understand statistical algorithm.
2. **Random Forest Regressor:** A powerful, ensemble learning method that creates multiple decision trees and merges them together for a more accurate and stable prediction.

## 📉 Evaluation Metrics
We measure how "wrong" our model is on average using:
- **MAE (Mean Absolute Error):** The absolute dollar amount the prediction is off by on average.
- **RMSE (Root Mean Squared Error):** Gives a higher penalty for larger errors.

## 🚀 How to Run the Project

**1. Install Required Libraries:**
Open your terminal and run:
`pip install -r requirements.txt`

**2. Generate the Dataset:**
Since you might not have the Kaggle dataset downloaded locally, run this script to generate `used_cars.csv` with 1000 sample records.
`python generate_dataset.py`

*(Note: If you have the real Kaggle dataset, simply rename it to `used_cars.csv` and ensure the columns match the features above!)*

**3. Train the Model and See Predictions:**
Run the main script to train the models and output the MAE/RMSE comparisons.
`python car_price_prediction.py`

This will also generate an image called `actual_vs_predicted.png` showing how closely the models guessed the actual prices.

---
**Created for Educational Purpose | 1st Year College Project**
