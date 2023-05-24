from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/')
def index():
    dici_enviado = request.args
    if 'nome' in request.args.keys() and 'idade' in request.args.keys():
        nomeForm = request.args['nome']
        idade = request.args['idade']
        idade = int(idade)

        if (idade < 16):
            votar = f'{nomeForm}, pessoas com idade de {idade} anos não podem votar.'
        elif (idade < 18):
            votar = f'{nomeForm}, pessoas com idade de {idade} anos podem votar, mas não é obrigatório.'
        else:
            votar = f'{nomeForm}, pessoas com idade de {idade} anos são obrigadas a votar.'

        return render_template('index.html', nome=nomeForm, idade=idade, votar=votar)
    return render_template('index.html')


app.run(host='localhost', port=8080, debug=True)
