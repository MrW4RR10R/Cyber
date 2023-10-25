from flask import Flask, request, make_response
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'supersecretkey'


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Controlla se le credenziali sono valide (da implementare)
        # Qui potresti avere una funzione per verificare le credenziali nel tuo database

        # Se le credenziali sono valide, registra l'orario dell'accesso nel cookie
        access_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        response = make_response(f'Benvenuto, {username}! Ultimo accesso: {access_time}')
        response.set_cookie('username', username)
        response.set_cookie('access_time', access_time)
        return response

    # Se l'utente ha già effettuato l'accesso, mostra il messaggio di benvenuto
    username = request.cookies.get('username')
    access_time = request.cookies.get('access_time')
    if username and access_time:
        return f'Benvenuto, {username}! Ultimo accesso: {access_time}'

    # Mostra il form per l'inserimento delle credenziali
    return '''
        <form method="post">
            <label for="username">Username:</label>
            <input type="text" id="username" name="username" required><br>
            <label for="password">Password:</label>
            <input type="password" id="password" name="password" required><br>
            <input type="submit" value="Accedi">
        </form>
    '''


if __name__ == '__main__':
    app.run(debug=True)