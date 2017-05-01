from chatterbot import ChatBot
from flask import jsonify,Flask,request
chatbot = ChatBot(
    'Anvena',
    trainer = 'chatterbot.trainers.ChatterBotCorpusTrainer',
    storage_adapter='chatterbot.storage.MongoDatabaseAdapter',
    database = 'chatbot'
)
chatbot.train('chatterbot.corpus.english.conversations')
app = Flask(__name__)

@app.route("/")
def home():
    q = request.args.get('q')
    res = {
    'response': str(chatbot.get_response(q))
    }
    return jsonify(res)
if __name__ == '__main__':
    app.run()
