# Simple Server

```
chmod +x ./get_cert.sh

# for https server
python3 app_https.py

# for http server
python3 app_http.py

```

#### If you want to set the location header do as below
```
def do_GET(self):
	self.send_response(302)
	self.send_haeder("Location", {Location_URL})
	self.end_header
```
