from flask import Flask, render_template, request
import boto3


app = Flask(__name__, template_folder='templates')
dynamodb = boto3.resource('dynamodb', region_name='us-east-2')
table = dynamodb.Table('MyDynamoDBTable')


@app.route('/', methods=['GET'])
def index():
    return render_template('formulario.html')

@app.route('/teste', methods=['GET'])
def teste():
    response = table.scan()
    mensagens = [item['mensagem'] for item in response.get('Items', [])]
    return render_template('teste.html', mensagens = mensagens)


@app.route('/salvar_dados', methods=['POST'])
def salvar_dados():
    if request.method == 'POST':
        # Extrai a mensagem do formulário
        mensagem = request.form['mensagem']

        # Insere a mensagem na tabela DynamoDB
        table.put_item(Item={'mensagem': mensagem})

        # Redireciona para a página de teste para exibir as mensagens
        return teste()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)

