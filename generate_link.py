"""
VisionaryX — Public Link Generator
Starts the Flask server and creates a Cloudflare tunnel for public access.
"""
import subprocess
import sys
import time
import threading

# Ensure pycloudflared is installed
try:
    from pycloudflared import try_cloudflare
except ImportError:
    print("[INFO] Installing pycloudflared...")
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'pycloudflared'])
    from pycloudflared import try_cloudflare

FLASK_PORT = 5000

def start_server():
    """Start the Flask server in a background thread."""
    subprocess.Popen(
        [sys.executable, 'server.py'],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )

print("\n" + "=" * 60)
print("   VisionaryX — Public Link Generator")
print("=" * 60)
print(f"\n[1/2] Starting Flask server on port {FLASK_PORT}...")

# Start server in background
server_thread = threading.Thread(target=start_server, daemon=True)
server_thread.start()
time.sleep(3)  # Wait for server to boot

print(f"[2/2] Creating public tunnel...")

try:
    tunnel = try_cloudflare(port=FLASK_PORT)
    print(f"\n{'=' * 60}")
    print(f"  YOUR APP IS LIVE AT:")
    print(f"  {tunnel}")
    print(f"{'=' * 60}")
    print("\n  Share this link - works on any device!")
    print("  Keep this terminal open to keep the link active.")
    print("  Press Ctrl+C to stop.\n")

    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("\n[INFO] Tunnel closed.")
except Exception as e:
    print(f"\n[ERROR] {e}")
    print("Make sure no other process is using port 5000.")
