from flask import Flask, request
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/communities", methods=["GET", "POST", "PUT", "DELETE"])
def communities():
    if request.method == "GET":
        return "Consultar comunidades!"
    elif request.method == "POST":
        return "Crear comunidad!"
    elif request.method == "PUT":
        return "Modificar comunidad!"
    elif request.method == "DELETE":
        return "Borrar comunidad!"
    else:
        return "default"

@app.route("/communities/<communityId>/members", methods=["POST"])
def communitiesInscription(communityId):
    return "Inscripción de miembro en la comunidad " + communityId

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)