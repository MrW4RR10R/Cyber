from flask import Flask, render_template, request

app = Flask(__name__)


def cifrario_di_cesare(testo, chiave):
    cifrato = ""

    for carattere in testo:
        if carattere.isalpha():
            maiuscola = carattere.isupper()
            carattere = carattere.lower()
            carattere_cifrato = chr(((ord(carattere) - ord('a') + chiave) % 26) + ord('a'))
            if maiuscola:
                carattere_cifrato = carattere_cifrato.upper()
            cifrato += carattere_cifrato
        else:
            cifrato += carattere

    return cifrato


@app.route("/", methods=["GET", "POST"])
def index():
    testo_cifrato = ""

    if request.method == "POST":
        testo_originale = request.form.get("testo_originale")
        chiave = int(request.form.get("chiave"))
        testo_cifrato = cifrario_di_cesare(testo_originale, chiave)

    return render_template("index.html", testo_cifrato=testo_cifrato)


if __name__ == '__main__':
    app.run(debug=True)
