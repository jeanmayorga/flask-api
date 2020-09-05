from flask import Flask, request, make_response, redirect

app = Flask(__name__)

@app.route('/redirect')
def home():
    name = request.args.get('name')

    if not name :
        name = 'John Doe'

    response = make_response(redirect('/'))
    response.set_cookie('name', name)

    return response

@app.route('/')
def hello():
    name = request.cookies.get('name')

    data = {
        name: name
    }

    return data

if __name__ == "__main__":
    app.run(debug=True)
