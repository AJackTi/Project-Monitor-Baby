Generate certificate:
1. openssl genrsa -des3 -out server.key 2048
2. openssl rsa -in server.key -out server.key
3. openssl req -sha256 -new -key server.key -out server.csr -subj "/CN=localhost"
4. openssl x509 -req -days 365 -in server.csr -signkey server.key -out server.crt

And after that you can use api.py by using command: python api.py