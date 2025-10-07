import http.server
import socketserver
import webbrowser
import os
import threading
import time
import socket

# Configuration
PORT = 8080

def get_local_ip():
    """Get the local IP address of the machine"""
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except Exception:
        return "127.0.0.1"

def start_server():
    """Start the HTTP server"""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    HTML_FILE = os.path.join(script_dir, "index.html")
    
    if not os.path.exists(HTML_FILE):
        print(f"Error: index.html not found!")
        print(f"Looking for: {HTML_FILE}")
        return False
    
    os.chdir(script_dir)
    local_ip = get_local_ip()
    
    print(f"IP Address: {local_ip}")
    print(f"Make sure port {PORT} is open in your cloud security group!")
    print(f"Server starting on port {PORT}...")
    
    handler = http.server.SimpleHTTPRequestHandler
    
    try:
        # Bind to all interfaces
        with socketserver.TCPServer(("0.0.0.0", PORT), handler) as httpd:
            print(f"✓ Server running!")
            print(f"Local: http://localhost:{PORT}")
            print(f"Network: http://{local_ip}:{PORT}")
            print("Press Ctrl+C to stop")
            httpd.serve_forever()
            
    except OSError as e:
        if e.errno == 48:
            print(f"Port {PORT} is already in use!")
        else:
            print(f"Server error: {e}")
        return False
    except KeyboardInterrupt:
        print("\nServer stopped")
        return True

# Don't auto-open browser on server (browsers aren't available on headless servers)
# Just start the server directly
if __name__ == "__main__":
    start_server()