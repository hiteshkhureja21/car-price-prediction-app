import streamlit as st
import pandas as pd
import pickle

st.set_page_config(page_title="VisionaryX - Indian Used Car Predictor", page_icon="🏎️", layout="wide")

# Theme Toggle
if 'theme' not in st.session_state:
    st.session_state.theme = 'dark'

def toggle_theme():
    st.session_state.theme = 'light' if st.session_state.theme == 'dark' else 'dark'

st.sidebar.button("🌓 Toggle Dark/Light Mode", on_click=toggle_theme)
st.sidebar.markdown("---")
st.sidebar.markdown("**About this App:**\nThis AI-driven platform incorporates realistic Indian domain knowledge (regional utility demand, exact depreciation models) to predict reliable used car prices.")
st.sidebar.markdown("[🔗 Visit Main Website](#)")

if st.session_state.theme == 'dark':
    bg_gradient = "radial-gradient(circle at 10% 20%, rgb(14, 21, 38) 0%, rgb(8, 12, 23) 90%)"
    text_color = "#f8fafc"
    card_bg = "rgba(255, 255, 255, 0.03)"
    card_border = "rgba(255, 255, 255, 0.05)"
    label_color = "#94a3b8"
else:
    bg_gradient = "linear-gradient(135deg, #fdfbfb 0%, #ebedee 100%)"
    text_color = "#1e293b"
    card_bg = "rgba(0, 0, 0, 0.02)"
    card_border = "rgba(0, 0, 0, 0.1)"
    label_color = "#475569"

st.markdown(f"""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600;800&display=swap');
    
    html, body, [class*="css"]  {{
        font-family: 'Outfit', sans-serif;
    }}
    
    .stApp {{
        background: {bg_gradient};
        color: {text_color};
        transition: background 0.5s ease;
    }}
    
    .stSelectbox label, .stNumberInput label, .stSlider label {{
        color: {label_color} !important;
        font-weight: 600;
        letter-spacing: 0.5px;
        display: flex;
        align-items: center;
        gap: 5px;
    }}
    
    [data-testid="stMarkdownContainer"] h1 {{
        background: -webkit-linear-gradient(45deg, #00f2fe, #4facfe, #00f2fe);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 800;
        text-align: center;
        padding-bottom: 20px;
        text-shadow: 0px 4px 15px rgba(79, 172, 254, 0.3);
    }}
    
    [data-testid="stMarkdownContainer"] p {{
        color: {text_color};
    }}
    
    .stButton>button {{
        width: 100%;
        background: linear-gradient(90deg, #3b82f6 0%, #8b5cf6 100%);
        color: white;
        font-weight: 800;
        letter-spacing: 1px;
        border: none;
        border-radius: 12px;
        padding: 0.8rem;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(139, 92, 246, 0.4);
    }}
    
    .stButton>button:hover {{
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(139, 92, 246, 0.6);
        background: linear-gradient(90deg, #2563eb 0%, #7c3aed 100%);
    }}

    [data-testid="column"] {{
        background: {card_bg};
        backdrop-filter: blur(16px);
        -webkit-backdrop-filter: blur(16px);
        border: 1px solid {card_border};
        border-radius: 16px;
        padding: 1.5rem;
        transition: transform 0.3s ease, box-shadow 0.3s ease;
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.15);
        margin-bottom: 1rem;
    }}
    
    [data-testid="column"]:hover {{
        transform: translateY(-5px);
        border: 1px solid rgba(139, 92, 246, 0.5);
        box-shadow: 0 12px 40px 0 rgba(0, 0, 0, 0.25);
    }}

    .stSuccess {{
        background: rgba(16, 185, 129, 0.1) !important;
        border: 1px solid rgba(16, 185, 129, 0.4) !important;
        color: #34d399 !important;
        border-radius: 12px;
    }}
    
    .stInfo {{
        background: rgba(59, 130, 246, 0.1) !important;
        border: 1px solid rgba(59, 130, 246, 0.4) !important;
        color: #60a5fa !important;
        border-radius: 12px;
    }}
    
    hr {{
        border-color: rgba(139, 92, 246, 0.2);
    }}
    
    #MainMenu {{visibility: hidden;}}
    header {{visibility: hidden;}}
    footer {{visibility: hidden;}}
    
    @media (max-width: 768px) {{
        [data-testid="column"] {{
            padding: 1rem !important;
            margin-bottom: 0.5rem !important;
        }}
        [data-testid="stMarkdownContainer"] h1 {{
            font-size: 1.8rem !important;
        }}
        .stButton>button {{
            padding: 1rem !important;
            font-size: 1.1rem !important;
        }}
        .stSelectbox label, .stNumberInput label, .stSlider label {{
            font-size: 0.9rem !important;
        }}
    }}
</style>
""", unsafe_allow_html=True)

st.title("🚗 VisionaryX: AI Price Calculator")
st.write("Fast, reliable, and strictly optimized market calculations to predict true resale value seamlessly.")

@st.cache_resource
def load_model():
    try:
        with open('best_rf_model.pkl', 'rb') as f:
            return pickle.load(f)
    except FileNotFoundError:
        return None
        
model = load_model()

if model is None:
    st.error("⚠️ Model not found! Please run 'python car_price_prediction.py' first!")
else:
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
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("### 🏷️ Vehicle Details")
        brand = st.selectbox("🏎️ Brand", list(car_models.keys()))
        selected_model = st.selectbox("🚘 Model", car_models[brand])
        variant = st.selectbox("⚙️ Variant", brand_variants[brand])

    with col2:
        st.markdown("### 👤 Usage History")
        condition = st.selectbox("✨ Condition", ['Excellent', 'Good', 'Fair', 'Poor'])
        owner = st.selectbox("👥 Owner", ['First Owner', 'Second Owner', 'Third Owner', 'Fourth & Above Owner'])
        km_driven = st.number_input("🛣️ KM Driven", min_value=0, max_value=500000, value=40000, step=5000)
        year = st.slider("📅 Year", 2010, 2026, 2018)

    with col3:
        st.markdown("### 🔧 Specifications")
        fuel = st.selectbox("⛽ Fuel", ['Petrol', 'Diesel', 'CNG'])
        transmission = st.selectbox("🕹️ Transmission", ['Manual', 'Automatic'])
        city = st.selectbox("🌆 City Reg", ['Metro (High Demand)', 'Tier 2 (Medium)', 'Rural (Low)'])
        mileage = st.number_input("🍃 Mileage (kmpl)", min_value=5.0, max_value=35.0, value=20.0, step=1.0)
        engine = st.number_input("🛠️ Engine (cc)", min_value=600, max_value=3000, value=1197, step=100)
        max_power = st.number_input("⚡ Power (bhp)", min_value=30, max_value=300, value=82, step=10)
        seats = st.selectbox("💺 Seats", ['4', '5', '7'], index=1)
        
    st.markdown("---")
    original_price = st.number_input("💵 Original Showroom Price (Rs.)", min_value=100000, value=750000, step=25000)
    
    if st.button("Predict Resale Price 🚀"):
        input_data = pd.DataFrame({
            'Brand': [brand],
            'Model': [selected_model],
            'variant': [variant],
            'condition': [condition],
            'city': [city],
            'fuel': [fuel],
            'transmission': [transmission],
            'owner': [owner],
            'mileage': [mileage],
            'engine': [engine],
            'max_power': [max_power],
            'seats': [seats],
            'km_driven': [km_driven],
            'car_age': [2026 - year],
            'Original_Price': [original_price]
        })
        
        # Raw AI Price
        raw_pred = model.predict(input_data)[0]
        
        # --- DOMAIN KNOWLEDGE SANITY PIPELINE ---
        final_pred = raw_pred
        
        # Rule 1: High Demand SUVs retain insane value in India (e.g., Creta, Fortuner)
        indian_premium_suvs = ['Creta', 'Fortuner', 'Innova', 'Scorpio', 'Thar', 'XUV700']
        if selected_model in indian_premium_suvs:
            final_pred *= 1.15
            
        # Rule 2: Absolute Limits Sanity check (Cannot drop below 30% unless poor, Cannot exceed 90% typically)
        min_allowed = original_price * 0.30
        max_allowed = original_price * 0.90
        
        if final_pred < min_allowed:
            final_pred = min_allowed + (original_price * 0.05)
        elif final_pred > max_allowed:
            final_pred = max_allowed - (original_price * 0.05)
            
        # Final formatting
        depreciation_pct = max(((original_price - final_pred) / original_price) * 100, 0)
        price_range_low = final_pred * 0.95
        price_range_high = final_pred * 1.05
        
        st.write("---")
        st.markdown(f"### 📋 Prediction Breakdown")
        
        ex1, ex2 = st.columns([1, 1])
        
        with ex1:
            st.markdown(f"**Original Price:** ₹ {original_price:,.0f}")
            st.markdown(f"**Age:** {2026 - year} years")
            if selected_model in indian_premium_suvs:
                st.markdown("✅ **Market Adjustment:** +15% (Premium SUV Indian Market Demand)")
            else:
                st.markdown("✅ **Market Adjustment:** Standard AI depreciation applied.")
                
            if final_pred == (min_allowed + (original_price * 0.05)):
                st.markdown("⚠️ **Safety Cap:** Prediction was raised to meet the 30% minimum market value floor.")
            elif final_pred == (max_allowed - (original_price * 0.05)):
                st.markdown("⚠️ **Safety Cap:** Prediction corrected downwards to respect 90% resale ceiling.")

        with ex2:
            st.markdown(f"**Depreciation Applied:** {depreciation_pct:.0f} %")
            st.success(f"### Predicted Price: ₹ {final_pred:,.0f}")
            st.info(f"**Market Range:** ₹ {price_range_low:,.0f} - ₹ {price_range_high:,.0f}")
