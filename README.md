# EX01 Developing a Simple Webserver
## Date:27/03/2025
## AIM:
To develop a simple webserver to serve html pages and display the list of protocols in TCP/IP Protocol Suite.

## DESIGN STEPS:
### Step 1: 
HTML content creation.

### Step 2:
Design of webserver workflow.

### Step 3:
Implementation using Python code.

### Step 4:
Import the necessary modules.

### Step 5:
Define a custom request handler.

### Step 6:
Start an HTTP server on a specific port.

### Step 7:
Run the Python script to serve web pages.

### Step 8:
Serve the HTML pages.

### Step 9:
Start the server script and check for errors.

### Step 10:
Open a browser and navigate to http://127.0.0.1:8000 (or the assigned port).

## PROGRAM:
```
from http.server import HTTPServer, BaseHTTPRequestHandler

# Corrected HTML content
content = """<html>
  <body>
    <h1 allign="centre"> Device Specifications</h1>
    <h2 allign ="right">(BINDHUJAA S) </h2>
    <h3 allign="right">(24901119)</h3>
    <ol type="i">
        <li> Device Name-DESKTOP-MOHHBTU</li>
        <li> Processor-13 th Gen Intel core</li>
        <li> Installed RAM -16.0 GB (15.7 GB usable)/li>
        <li> Device ID-15EEA3B2-7EF5-4DEC-903D-577382C3C005</li>
        <li> Product ID- 00342-42709-07172-AAOEM</li>
        <li> System tyope- 64-bit operating system, x64-based processor</li>
        <li> Pen and Touch-No pen or touch input is available for this display </li>
    </ol>
  </body>
</html>
"""
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',8000)
httpd = HTTPServer(server_address,myhandler)
print("my webserver is running...")
httpd.serve_forever()
```

## OUTPUT:
![alt text](<Screenshot 2025-03-27 154701.png>)

## RESULT:
The program for implementing simple webserver is executed successfully.
