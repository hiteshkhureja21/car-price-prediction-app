from pycloudflared import try_cloudflare
import time

print("=" * 50)
print("Generating public link for your Streamlit app...")
print("=" * 50)

try:
    tunnel = try_cloudflare(port=8501)
    print(f"\n{'=' * 60}")
    print(f"  YOUR APP IS LIVE AT:")
    print(f"  {tunnel}")
    print(f"{'=' * 60}")
    print("\nKeep this terminal open to keep the link active.")
    print("Press Ctrl+C to stop.\n")
    
    # Keep the script alive
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("\nTunnel closed.")
except Exception as e:
    print(f"Error: {e}")
