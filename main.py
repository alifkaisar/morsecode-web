from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField
from flask_bootstrap import Bootstrap5
import os

app = Flask(__name__)
app.secret_key = os.environ.get("FLASK_KEY")
bootstrap = Bootstrap5(app)

morse_code = {
    "A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".", "F": "..-.", "G": "--.", "H": "....", "I": "..",
    "J": ".---", "K": "-.-", "L": ".-..", "M": "--", "N": "-.", "O": "---", "P": ".--.", "Q": "--.-", "R": ".-.",
    "S": "...", "T": "-", "U": "..-", "V": "...-", "W": ".--", "X": "-..-", "Y": "-.--", "Z": "--..",
    "0": "-----", "1": ".----", "2": "..---", "3": "...--", "4": "....-", "5": ".....", "6": "-....", "7": "--...",
    "8": "---..", "9": "----.", ".": ".-.-.-", ",": "--..--", "?": "..--..", "'": ".----.", "!": "-.-.--", "/": "-..-.",
    "(": "-.--.", ")": "-.--.-", "&": ".-...", ":": "---...", ";": "-.-.-.", "=": "-...-", "+": ".-.-.", "-": "-....-",
    "_": "..--.-", '"': ".-..-.", "$": "...-..-", "@": ".--.-."
}


class TextArea(FlaskForm):
    text = TextAreaField(label="TEXT", render_kw={"style": "background-color: var(--bs-dark-bg-subtle); "
                                                           "height: 100px;",
                                                  "class": "border border-3"})
    button = SubmitField(label="Encode", render_kw={"class": "btn btn-secondary"})


@app.route('/', methods=["GET", "POST"])
def home_page():
    form = TextArea()
    if form.validate_on_submit():
        text = " ".join(request.form["text"].upper().split())
        morse_result = "".rstrip()
        for letter in text:
            if letter == " ":
                morse_result += "/ "
            else:
                morse_representation = morse_code.get(letter, "#")
                morse_result += f"{morse_representation} "
        return render_template("index.html", form=form, submit=True, decode=morse_result)

    return render_template("index.html", form=form)


if __name__ == "__main__":
    app.run(debug=True)
