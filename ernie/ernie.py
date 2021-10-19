from flask import Flask, request, render_template
from transformers import pipeline

from ernie.forms import AskErnie

app = Flask(__name__, template_folder="../templates", static_folder="../static")
app.config["SECRET_KEY"] = "rubber duckie"
unmasker = pipeline("fill-mask", model="distilbert-base-uncased")


@app.route("/")
def index():
    form = AskErnie()
    return render_template("index.html", form=form)


@app.route("/ask", methods=["POST"])
def ask():
    form = AskErnie(request.form)
    masks = unmasker(form.prompt.data)
    return render_template("results.html", masks=masks)

# change
