from flask import Flask, render_template, request
import random
import json

app = Flask(__name__)

with open("intents.json") as f:
    data = json.load(f)

@app.route("/", methods=["GET", "POST"])
def home():
    response = ""
    if request.method == "POST":
        user_msg = request.form["msg"].lower()
        for intent in data["intents"]:
            for pattern in intent["patterns"]:
                if pattern in user_msg:
                    response = random.choice(intent["responses"])
    return render_template("index.html", response=response)

if __name__ == "__main__":
    app.run(debug=True)
