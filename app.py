from flask import Flask, render_template, request
import boto3
import uuid

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
        mensagem = request.form['mensagem']  # Extrai a mensagem do formulário
        unique_id = str(uuid.uuid4())  # Gera um UUID único

        # Insere a mensagem na tabela DynamoDB com o UUID como chave de partição
        table.put_item(Item={
            'MyPartitionKey': unique_id,  # Use o UUID como a chave de partição
            'mensagem': mensagem
        })

        # Redireciona para a página de teste para exibir as mensagens
        return teste()
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)

