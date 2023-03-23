from flask import Flask, request
from worker import countWords

app = Flask(__name__, template_folder='template')


@app.route('/count', methods=["POST"])
def count():
    data = request.get_json()
    text = data['text']
    
    num_words = countWords(text)
    print("\n\n\n\n", num_words)
    
    return {"num_words": num_words}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050, debug=True)