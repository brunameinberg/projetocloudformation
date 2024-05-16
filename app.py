from flask import Flask, render_template, request

import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('MyDynamoDBTable')

app = Flask(__name__)

@app.route('/db', methods=['GET'])
def read_from_dynamodb():
    response = table.scan()
    items = response['Items']
    return f'Dados da tabela DynamoDB: {items}'

@app.route('/db', methods=['POST'])
def write_to_dynamodb():
    data = {'example_key': 'example_value'}
    table.put_item(Item=data)
    return 'Item adicionado à tabela DynamoDB com sucesso!'

if __name__ == '__main__':
    app.run(debug=True)
