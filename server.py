import os
from flask import Flask

app = Flask(__name__)

@app.route("/.well-known/acme-challenge/kcMNDL1qCzRvuFpmqwfyM3Rc1iRmxf1MFwzD5Je9s7o.5249X9NOnpSqQPKt8MkLdEtedSVDgAyyxwv9BRg1bGg")
# e.g. /.well-known/acme-challenge/lzrajCaq8vbw5Qz2o_XXXXXXXXXXXXXXXXX
def hello():
    return "kcMNDL1qCzRvuFpmqwfyM3Rc1iRmxf1MFwzD5Je9s7o.5249X9NOnpSqQPKt8MkLdEtedSVDgAyyxwv9BRg1bGg"
    # e.g. return "lzrajCaq8vbw5Qz2o_XXXXXXXXXXXXXXXXXXz4RnfWtLKaIc6EdhsOsr4fb6RFZuUoabZW5dPW36cmc"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

