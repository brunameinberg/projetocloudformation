from flask import Flask, render_template, request
import boto3
import uuid
import logging
from botocore.exceptions import ClientError


app = Flask(__name__, template_folder='templates')
dynamodb = boto3.resource('dynamodb', region_name='us-east-2')
table = dynamodb.Table('MyDynamoDBTable')


@app.route('/', methods=['GET'])
def index():
    return render_template('formulario.html')

@app.route('/teste', methods=['GET'])
def teste():
    try:
        response = table.scan()
        mensagens = [item['mensagem'] for item in response.get('Items', [])]
        return render_template('teste.html', mensagens=mensagens)
    except Exception as e:
        logging.error(f"Erro ao buscar dados no DynamoDB: {e}")
        return render_template('teste.html', mensagens=[])


@app.route('/salvar_dados', methods=['POST'])
def salvar_dados():
    if request.method == 'POST':
        mensagem = request.form['mensagem']
        unique_id = str(uuid.uuid4())  # Gera um UUID único

        logging.info(f'Mensagem recebida: {mensagem}')
        logging.info(f'UUID gerado: {unique_id}')

        try:
            table.put_item(Item={
                'id': unique_id,  # Use o UUID como a chave de partição
                'mensagem': mensagem
            })

            logging.info('Dados inseridos no DynamoDB com sucesso.')
        except Exception as e:
            logging.error(f'Erro ao inserir dados no DynamoDB: {e}')

        return '', 204  # Retorna um status de sucesso sem conteúdo

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
