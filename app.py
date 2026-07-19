from flask import Flask, render_template, request, jsonify
from chatbot import chat_with_ai, clear_history

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    question = data.get("message", "")

    try:
        response = chat_with_ai(question)

        return jsonify({
            "success": True,
            "category": response["category"],
            "answer": response["answer"]
        })

    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        })


@app.route("/clear", methods=["POST"])
def clear():
    clear_history()
    return jsonify({"success": True})


if __name__ == "__main__":
    app.run(debug=True)