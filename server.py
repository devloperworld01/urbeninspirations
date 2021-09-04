import os
from flask import Flask

app = Flask(__name__)

@app.route("/.well-known/acme-challenge/<copy last part of URL from certbot console>")
def hello():
    return "<copy data from certbot console>"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
