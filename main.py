from flask import Flask
import json

app = Flask(__name__)

@app.route("/")
def Home():
    return json.dumps({
        "message": "Hey, I am a Flask app",
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int("3000"), debug=True)