from flask import Flask, jsonify
import automationhat
app = Flask(__name__)

val = 0

def number_to_word(id):
    if int(id) == 1:
        return "one"
    elif int(id) == 2:
        return "two"
    elif int(id) == 3:
        return "three"
    else:
        return None


@app.route("/")
def hello():
    return "Hello World!"

@app.route("/api/relay/<id>", methods=['PUT', 'GET'])
def toggle(id):
    id_str = number_to_word(id)
    if id_str:
        automationhat.relay[id_str].toggle()
        return jsonify(active=automationhat.relay[id_str].read())
    else:
        return jsonify(result={"status": 500})

@app.route("/api/analog/<id>", methods=['GET'])
def readAnalog(id):
    id_str = number_to_word(id)
    if id_str:
        return jsonify(value=automationhat.analog[id_str].read())
    else:
        return jsonify(result={"status": 500})

@app.route("/api/input/<id>", methods=['GET'])
def readInput(id):
    id_str = number_to_word(id)
    if id_str:
        return jsonify(value=automationhat.input[id_str].read())
    else:
        return jsonify(result={"status": 500})


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)