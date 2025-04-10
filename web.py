from http.server import HTTPServer, BaseHTTPRequestHandler

# Corrected HTML content
content = """ <!doctype html>
<html>
<head>
<title> My Web Server</title>
</head>
<body>
<center><h1>TCP/IP PROTOCOLS</h1><br>
</center>
<h3>
1. Application Layer Protocols - HTTP,FTP,DNS<br>
2. Transport Layer Protocols - TCP/UDP<br>
3. Internet Layer Protocols - IPV4/IPV6<br>
4. Link Layer Protocols - MAC<br>
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
