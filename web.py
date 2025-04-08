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
