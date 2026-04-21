import pandas as pd
import numpy as np
import random
import datetime

def generate_data(num_samples=1500):
    car_models = {
        'Maruti Suzuki': ['Alto', 'Swift', 'Baleno', 'Dzire', 'Brezza', 'Ertiga'],
        'Hyundai': ['Grand i10', 'i20', 'Venue', 'Verna', 'Creta'],
        'Tata': ['Tiago', 'Altroz', 'Nexon', 'Harrier', 'Safari'],
        'Mahindra': ['Bolero', 'XUV300', 'Thar', 'Scorpio', 'XUV700'],
        'Kia': ['Sonet', 'Carens', 'Seltos'],
        'Toyota': ['Glanza', 'Urban Cruiser', 'Innova', 'Fortuner'],
        'Honda': ['Amaze', 'Elevate', 'City'],
        'Volkswagen': ['Polo', 'Vento', 'Taigun', 'Virtus']
    }
    
    # Define exact Kaggle attributes per model
    model_specs = {
        'Alto': {'engine': 796, 'power': 47, 'mileage': 22.0, 'seats': 5, 'base_price': 350000},
        'Swift': {'engine': 1197, 'power': 82, 'mileage': 21.0, 'seats': 5, 'base_price': 600000},
        'Baleno': {'engine': 1197, 'power': 88, 'mileage': 22.0, 'seats': 5, 'base_price': 750000},
        'Dzire': {'engine': 1197, 'power': 88, 'mileage': 23.0, 'seats': 5, 'base_price': 700000},
        'Brezza': {'engine': 1462, 'power': 103, 'mileage': 19.0, 'seats': 5, 'base_price': 900000},
        'Ertiga': {'engine': 1462, 'power': 103, 'mileage': 20.0, 'seats': 7, 'base_price': 1000000},
        'Grand i10': {'engine': 1197, 'power': 82, 'mileage': 20.0, 'seats': 5, 'base_price': 650000},
        'i20': {'engine': 1197, 'power': 82, 'mileage': 20.0, 'seats': 5, 'base_price': 800000},
        'Venue': {'engine': 998, 'power': 118, 'mileage': 18.0, 'seats': 5, 'base_price': 1000000},
        'Verna': {'engine': 1497, 'power': 113, 'mileage': 19.0, 'seats': 5, 'base_price': 1200000},
        'Creta': {'engine': 1497, 'power': 113, 'mileage': 16.0, 'seats': 5, 'base_price': 1500000},
        'Tiago': {'engine': 1199, 'power': 84, 'mileage': 20.0, 'seats': 5, 'base_price': 600000},
        'Altroz': {'engine': 1199, 'power': 84, 'mileage': 19.0, 'seats': 5, 'base_price': 800000},
        'Nexon': {'engine': 1199, 'power': 118, 'mileage': 17.0, 'seats': 5, 'base_price': 1100000},
        'Harrier': {'engine': 1956, 'power': 167, 'mileage': 16.0, 'seats': 5, 'base_price': 1800000},
        'Safari': {'engine': 1956, 'power': 167, 'mileage': 14.0, 'seats': 7, 'base_price': 2000000},
        'Bolero': {'engine': 1493, 'power': 75, 'mileage': 16.0, 'seats': 7, 'base_price': 950000},
        'XUV300': {'engine': 1197, 'power': 108, 'mileage': 17.0, 'seats': 5, 'base_price': 1100000},
        'Thar': {'engine': 1997, 'power': 150, 'mileage': 15.0, 'seats': 4, 'base_price': 1500000},
        'Scorpio': {'engine': 2184, 'power': 130, 'mileage': 15.0, 'seats': 7, 'base_price': 1600000},
        'XUV700': {'engine': 2198, 'power': 182, 'mileage': 13.0, 'seats': 7, 'base_price': 2000000},
        'Sonet': {'engine': 998, 'power': 118, 'mileage': 18.0, 'seats': 5, 'base_price': 1000000},
        'Carens': {'engine': 1497, 'power': 113, 'mileage': 16.0, 'seats': 7, 'base_price': 1200000},
        'Seltos': {'engine': 1497, 'power': 113, 'mileage': 16.0, 'seats': 5, 'base_price': 1600000},
        'Glanza': {'engine': 1197, 'power': 88, 'mileage': 22.0, 'seats': 5, 'base_price': 800000},
        'Urban Cruiser': {'engine': 1462, 'power': 103, 'mileage': 18.0, 'seats': 5, 'base_price': 1000000},
        'Innova': {'engine': 2393, 'power': 148, 'mileage': 11.0, 'seats': 7, 'base_price': 2500000},
        'Fortuner': {'engine': 2755, 'power': 201, 'mileage': 10.0, 'seats': 7, 'base_price': 3500000},
        'Amaze': {'engine': 1199, 'power': 88, 'mileage': 18.0, 'seats': 5, 'base_price': 800000},
        'Elevate': {'engine': 1498, 'power': 119, 'mileage': 15.0, 'seats': 5, 'base_price': 1300000},
        'City': {'engine': 1498, 'power': 119, 'mileage': 17.0, 'seats': 5, 'base_price': 1400000},
        'Polo': {'engine': 999, 'power': 108, 'mileage': 18.0, 'seats': 5, 'base_price': 800000},
        'Vento': {'engine': 999, 'power': 108, 'mileage': 17.0, 'seats': 5, 'base_price': 1100000},
        'Taigun': {'engine': 1498, 'power': 148, 'mileage': 16.0, 'seats': 5, 'base_price': 1400000},
        'Virtus': {'engine': 1498, 'power': 148, 'mileage': 18.0, 'seats': 5, 'base_price': 1500000}
    }
    
    brand_variants = {
        'Maruti Suzuki': ['LXI (Base)', 'VXI (Mid)', 'ZXI (Top)'],
        'Hyundai': ['E (Base)', 'S (Mid)', 'SX (Top)'],
        'Tata': ['XE (Base)', 'XM (Mid)', 'XZ (Top)'],
        'Mahindra': ['Base', 'Mid', 'Top'],
        'Kia': ['HTE (Base)', 'HTK (Mid)', 'GTX (Top)'],
        'Toyota': ['G (Base)', 'V (Top)'],
        'Honda': ['E (Base)', 'S (Mid)', 'VX (Top)'],
        'Volkswagen': ['Trendline (Base)', 'Comfortline (Mid)', 'Highline (Top)']
    }
    conditions = ['Excellent', 'Good', 'Fair', 'Poor']
    cities = ['Metro (High Demand)', 'Tier 2 (Medium)', 'Rural (Low)']
    
    fuels = ['Petrol', 'Diesel', 'CNG']
    transmissions = ['Manual', 'Automatic']
    owners = ['First Owner', 'Second Owner', 'Third Owner', 'Fourth & Above Owner']
    
    data = []
    
    # 2026 is the base year for our program
    current_year = 2026
    
    for _ in range(num_samples):
        brand = random.choice(list(car_models.keys()))
        model = random.choice(car_models[brand])
        variant = random.choice(brand_variants[brand])
        condition = random.choices(conditions, weights=[0.2, 0.5, 0.2, 0.1])[0]
        city = random.choices(cities, weights=[0.4, 0.4, 0.2])[0]
        
        name = f"{brand} {model}" # Will be extracted back out via feature engineering
        km_driven = round(random.uniform(5000, 150000), 2)
        
        fuel = random.choice(fuels)
        transmission = random.choice(transmissions)
        owner_str = random.choices(owners, weights=[0.5, 0.3, 0.15, 0.05])[0]
        
        age = random.randint(1, 15)
        year = current_year - age 
        
        specs = model_specs[model]
        engine = specs['engine']
        max_power = specs['power']
        mileage_val = specs['mileage']
        seats = specs['seats']
        
        original_price = specs['base_price'] + random.uniform(0, 150000)
        
        # Modifier logic
        if fuel == 'Diesel': original_price += 100000
        if transmission == 'Automatic': original_price += 120000
        if 'Mid' in variant: original_price += 40000
        elif 'Top' in variant: original_price += 100000
            
        # Realistic Indian Depreciation
        # 1st year: 15-20% drop
        drop_year_1 = random.uniform(0.15, 0.20)
        price = original_price * (1 - drop_year_1)
        
        if 'Mid' in variant: price *= 1.05
        elif 'Top' in variant: price *= 1.10
        
        if condition == 'Excellent': price *= 1.10
        elif condition == 'Fair': price *= 0.85
        elif condition == 'Poor': price *= 0.70
        
        if city == 'Metro (High Demand)': price *= 1.05
        elif city == 'Rural (Low)': price *= 0.95
        
        # Next years: 8-12% per year
        if age > 1:
            for y in range(age - 1):
                price = price * (1 - random.uniform(0.08, 0.12))
                
        # Premium retention for high demand models
        if model in ['Creta', 'Fortuner', 'Innova', 'Scorpio', 'XUV700', 'Swift']:
            price *= 1.15  # retain 15% more value
            
        # Low km driven boosts price
        if km_driven < 50000:
            price *= 1.10
        elif km_driven > 100000:
            price *= 0.85
            
        # First owner boosts price
        if owner_str == 'First Owner':
            price *= 1.10
        elif owner_str == 'Second Owner': 
            price *= 0.90
        elif owner_str == 'Third Owner': 
            price *= 0.80
        elif owner_str == 'Fourth & Above Owner': 
            price *= 0.65
            
        # Add market randomness
        price += random.uniform(-25000, 25000)
        
        # Outlier demonstrations
        if random.random() < 0.03: price = price * random.uniform(3, 5) 
        if random.random() < 0.03: km_driven = km_driven + random.uniform(300000, 600000)
            
        # Hard limits
        min_price = original_price * 0.30
        max_price = original_price * 0.90
        if price < min_price: price = min_price + random.uniform(10000, 30000)
        if price > max_price: price = max_price - random.uniform(10000, 30000)
        
        data.append([
            name, variant, condition, city, year, km_driven, fuel, transmission, owner_str, 
            mileage_val, engine, max_power, seats, round(original_price, 2), round(price, 2)
        ])
        
    df = pd.DataFrame(data, columns=[
        'name', 'variant', 'condition', 'city', 'year', 'km_driven', 'fuel', 'transmission', 'owner', 
        'mileage', 'engine', 'max_power', 'seats', 'Original_Price', 'Price'
    ])
    df.to_csv('used_cars_advanced.csv', index=False)
    print("Dataset generated successfully as 'used_cars_advanced.csv' with authentic Kaggle features!")

if __name__ == '__main__':
    generate_data(1500)
