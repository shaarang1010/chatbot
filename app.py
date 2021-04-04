from flask import Flask, request, jsonify, render_template, url_for, redirect
from flask_cors import CORS, cross_origin
from bot_scripts.bot import Bot
import os
from dotenv import load_dotenv

app = Flask(__name__)


load_dotenv()

app.config['SECRET_KEY'] = os.getenv('APP_SECRET')

CORS(app)

basedir = os.path.abspath(os.path.dirname(__file__))


@app.route('/bottest', methods=['POST'])
def bot_test():
    args= request.get_json(force=True)
    bot = Bot(args['botname'])
    status = 200
    try:
        test_message = bot.bot_test()
        bot_name = bot.get_name()
    except Exception as e:
        status = 400
    return jsonify({'value':test_message, 'botname': bot_name}), status


@app.route('/converse', methods=['POST'])
def converse():
    args = request.get_json(force=True)
    bot_name = args['botname']
    user_question = str(args['query']).lower()
    bot = Bot(bot_name)
    status = 200
    try:
        response = bot.chat(user_question)
    except Exception as e:
        response = str(e)
    return jsonify({"data":{'version':'1.0','msg':response, 'status':status}}), status




@app.route('/test', methods=['GET'])
def test_func():
    return jsonify({'value':'ok'}), 200

if __name__=='__main__':
    app.run(host='0.0.0.0', port='5000', debug=True)