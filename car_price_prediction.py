import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import datetime
import pickle
import warnings

from sklearn.model_selection import train_test_split, GridSearchCV, cross_val_score
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from xgboost import XGBRegressor

warnings.filterwarnings('ignore')

def main():
    print("=" * 60)
    print("Authentic Kaggle-Spec Car ML System")
    print("=" * 60)
    
    try:
        df = pd.read_csv('used_cars_advanced.csv')
    except FileNotFoundError:
        print("Error: Please run generate_dataset.py first.")
        return
        
    print(f"[*] Initial Dataset shape: {df.shape}")
    
    print("[*] Performing Feature Engineering...")
    # Extract brand and model properly from 'name'
    df['Brand'] = df['name'].apply(lambda x: " ".join(x.split()[:2]) if "Maruti Suzuki" in x else x.split()[0])
    df['Model'] = df['name'].apply(lambda x: " ".join(x.split()[2:]) if "Maruti Suzuki" in x else " ".join(x.split()[1:]))
    
    current_year = 2026
    df['car_age'] = current_year - df['year']
    df.drop(['name', 'year'], axis=1, inplace=True)
    
    df['seats'] = df['seats'].astype(str)
    
    print("[*] Removing Outliers using IQR method...")
    def remove_outliers(data, col):
        Q1 = data[col].quantile(0.25)
        Q3 = data[col].quantile(0.75)
        IQR = Q3 - Q1
        return data[(data[col] >= Q1 - 1.5 * IQR) & (data[col] <= Q3 + 1.5 * IQR)]
        
    df = remove_outliers(df, 'Price')
    df = remove_outliers(df, 'km_driven')
    
    X = df.drop('Price', axis=1)
    y = df['Price']
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    categorical_features = ['Brand', 'Model', 'variant', 'condition', 'city', 'fuel', 'transmission', 'owner', 'seats']
    numeric_features = ['km_driven', 'car_age', 'Original_Price', 'mileage', 'engine', 'max_power']
    
    preprocessor = ColumnTransformer(
        transformers=[
            ('num', StandardScaler(), numeric_features),
            ('cat', OneHotEncoder(drop='first', handle_unknown='ignore'), categorical_features)
        ])
        
    print("\n[*] Training and Evaluating XGBoostRegressor...")
    xgb_pipeline = Pipeline(steps=[('preprocessor', preprocessor), ('model', XGBRegressor(random_state=42))])
    xgb_pipeline.fit(X_train, y_train)
    
    print("[*] Training and Tuning RandomForestRegressor (GridSearchCV)...")
    rf_pipeline = Pipeline(steps=[('preprocessor', preprocessor), ('model', RandomForestRegressor(random_state=42))])
    
    param_grid = {
        'model__n_estimators': [50, 100],
        'model__max_depth': [10, 20, None]
    }
    
    grid_search = GridSearchCV(rf_pipeline, param_grid, cv=3, scoring='r2', n_jobs=-1)
    grid_search.fit(X_train, y_train)
    
    best_rf_pipeline = grid_search.best_estimator_
    
    print("\n" + "="*30)
    for model_pipeline, name in [(xgb_pipeline, "XGBoost Regressor"), (best_rf_pipeline, "Random Forest (Tuned)")]:
        preds = model_pipeline.predict(X_test)
        mae = mean_absolute_error(y_test, preds)
        rmse = np.sqrt(mean_squared_error(y_test, preds))
        r2 = r2_score(y_test, preds)
        cv_scores = cross_val_score(model_pipeline, X, y, cv=5, scoring='r2')
        print(f"--- {name} ---")
        print(f"R2 Score: {r2:.4f}  |  MAE: Rs. {mae:,.2f}  |  RMSE: Rs. {rmse:,.2f}  |  CV R2: {cv_scores.mean():.4f}\n")
    
    print("[*] Saving the best model using pickle...")
    with open('best_rf_model.pkl', 'wb') as f:
        pickle.dump(best_rf_pipeline, f)
    print("Model saved successfully as 'best_rf_model.pkl'.")

if __name__ == "__main__":
    main()
