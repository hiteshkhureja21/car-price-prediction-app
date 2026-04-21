import os
import time
from pyngrok import ngrok
import subprocess

try:
    auth_token = os.environ.get("NGROK_AUTHTOKEN")
    if not auth_token:
        print("ngrok requires an authtoken to start in most cases.")
        print("You can get one for free at https://dashboard.ngrok.com/get-started/your-authtoken")
        auth_token = input("Enter your ngrok authtoken (or press Enter to try without): ").strip()
    
    if auth_token:
        ngrok.set_auth_token(auth_token)

    # Attempt to start ngrok tunnel
    public_url = ngrok.connect(8501)
    url = public_url.public_url if hasattr(public_url, 'public_url') else public_url
    print(f"==================================================")
    print(f"YOUR APP IS LIVE AT: {url}")
    print(f"==================================================")
    
    # Start streamlit
    print("Starting Streamlit app...")
    subprocess.run(["streamlit", "run", "app.py", "--server.port", "8501", "--server.headless", "true"])
except Exception as e:
    print(f"Error: {e}")
