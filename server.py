import os
from flask import Flask

app = Flask(__name__)

@app.route("/.well-known/acme-challenge/IRCg5C1rDFaR8shC3yfwPROHXTv8-pMvSnZkQFsE-4o.5249X9NOnpSqQPKt8MkLdEtedSVDgAyyxwv9BRg1bGg")
# e.g. /.well-known/acme-challenge/lzrajCaq8vbw5Qz2o_XXXXXXXXXXXXXXXXX
def hello():
    return "IRCg5C1rDFaR8shC3yfwPROHXTv8-pMvSnZkQFsE-4o.5249X9NOnpSqQPKt8MkLdEtedSVDgAyyxwv9BRg1bGg"
    # e.g. return "lzrajCaq8vbw5Qz2o_XXXXXXXXXXXXXXXXXXz4RnfWtLKaIc6EdhsOsr4fb6RFZuUoabZW5dPW36cmc"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

