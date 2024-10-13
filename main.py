from flask import Flask, request, Response
import random;
import json;
from text_data import data


app = Flask(__name__)

app.config['JSON_AS_ASCII'] = False

@app.route("/get-quote")
def get_quote():
    randdata = random.randint(0, len(data)-1)
    response_data = {
        "quote": data[randdata]
    }
    response_json = json.dumps(response_data, ensure_ascii=False)
    return Response(response_json, content_type='application/json; charset=utf-8')

if __name__ == "__main__":
    app.run(debug=True)