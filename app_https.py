#!/usr/bin/env python
# -*- coding: utf-8 -*-

from http.server import BaseHTTPRequestHandler, HTTPServer
import ssl

class MyHandler(BaseHTTPRequestHandler):
	def do_GET(self):
		if self.path == '/index.html' or \
					  self.path == '/':
			filename = './index.html'
			self.send_response(200)
			self.send_header('Content-type', 'text/html')
		self.end_headers()

		print(self.path)
		print(self.headers)
		with open(filename, 'rb') as f:
			file = f.read()
			self.wfile.write(file)

if __name__ == "__main__":
	httpd = HTTPServer(('0.0.0.0', 8000), MyHandler)
	ctx = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
	ctx.check_hostname = False
	ctx.load_cert_chain(certfile='./cert.pem', keyfile='./key.pem')
	httpd.socket = ctx.wrap_socket(httpd.socket, server_side=True)
	httpd.serve_forever()
