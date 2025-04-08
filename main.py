from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['POST'])
def webhook():
    try:
        data = request.get_data(as_text=True)
        print("✅ Webhook empfangen:", data)
        return '', 200
    except Exception as e:
        print("❌ Fehler beim Verarbeiten:", e)
        return '', 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

