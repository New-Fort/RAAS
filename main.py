from flask import Flask, request, Response
import random;
import json;
from text_data import data


app = Flask(__name__)

app.config['JSON_AS_ASCII'] = False

@app.route("/get-quote")
def get_quote():
    key = request.args.get("key")
    curateddata = []

    if key:
        for quote in data:
            if key.lower() in quote.lower():
                curateddata.append(quote)

    if curateddata:
        selected_quote = random.choice(curateddata)
    else:
        selected_quote = random.choice(data)  # Fallback to a random quote from the full data

    response_data = {
        "quote": selected_quote
    }

    response_json = json.dumps(response_data, ensure_ascii=False)
    return Response(response_json, content_type='application/json; charset=utf-8')

@app.route("/")
def home():
    return Response("To get a quote, use /get-quote \n To get a quote with a specified key in it, use /get-quote?key=EXAMPLE")

if __name__ == "__main__":
    app.run(debug=True)