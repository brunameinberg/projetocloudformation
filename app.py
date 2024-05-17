from flask import Flask, render_template, request


app = Flask(__name__, template_folder='templates')


@app.route('/', methods=['GET'])
def index():
    return render_template('formulario.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

