from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/armstrong/<int:n>')
def armstrong(n):
    sum = 0
    copy_n = n
    order = len(str(n))
    while(n > 0):
        digit = n % 10
        sum += digit ** order
        n = n // 10

    if(sum == copy_n):
        print("Armstrong number")
        result = {
            "Number":copy_n,
            "Armstrong": True,
        }
    else:
        print("not Armstrong number")
        result = {
            "Number": copy_n,
            "Armstrong": False,
        }
    return jsonify(result)


app.run(debug=True)