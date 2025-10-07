import http.server
import socketserver
import webbrowser
import os
import threading
import time
import socket

# Configuration
PORT = 1979

def get_local_ip():
    """Get the local IP address of the machine"""
    try:
        # Create a socket connection to get the local IP
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))  # Connect to Google's DNS
        ip = s.getsockname()[0]
        s.close()
        return ip
    except Exception:
        return "127.0.0.1"

def start_server():
    """Start the HTTP server"""
    # Get the directory where this script is located
    script_dir = os.path.dirname(os.path.abspath(__file__))
    HTML_FILE = os.path.join(script_dir, "index.html")
    
    # Check if index.html exists in the script's directory
    if not os.path.exists(HTML_FILE):
        print(f"Error: index.html not found in the script directory!")
        print(f"Looking for: {HTML_FILE}")
        print("Please make sure index.html is in the same directory as this script.")
        return False
    
    # Change to the script's directory so the server serves files from there
    os.chdir(script_dir)
    
    # Get local IP
    local_ip = get_local_ip()
    
    # Print the IP address clearly
    print(f"IP Address: {local_ip}")
    
    # Create a simple HTTP request handler
    handler = http.server.SimpleHTTPRequestHandler
    
    try:
        # Create the server - bind to all interfaces (0.0.0.0) so it's accessible externally
        with socketserver.TCPServer(("0.0.0.0", PORT), handler) as httpd:
            print(f"Server started!")
            print(f"Local access: http://localhost:{PORT}")
            print(f"Local network access: http://{local_ip}:{PORT}")
            print(f"Serving files from: {script_dir}")
            print("Press Ctrl+C to stop the server")
            
            # Start the server
            httpd.serve_forever()
            
    except OSError as e:
        if e.errno == 48:  # Address already in use
            print(f"Error: Port {PORT} is already in use!")
            print("Please close any other applications using this port or change the PORT variable.")
        else:
            print(f"Server error: {e}")
        return False
    except KeyboardInterrupt:
        print("\nServer stopped by user")
        return True

def open_browser():
    """Open the browser after a short delay using localhost"""
    time.sleep(1)  # Wait for server to start
    # Use localhost for browser opening (more reliable for local development)
    webbrowser.open(f"http://localhost:{PORT}/index.html")

if __name__ == "__main__":
    # Start browser in a separate thread
    browser_thread = threading.Thread(target=open_browser)
    browser_thread.daemon = True
    browser_thread.start()
    
    # Start the server
    start_server()