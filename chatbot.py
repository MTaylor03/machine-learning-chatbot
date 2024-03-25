from flask import Flask, request, render_template, jsonify
from bot_logic import BotLogic

app = Flask(__name__)

# Load the database
database = BotLogic.get_database("data_base.json")


@app.route('/') # Render index.html with default bot name
def index():
    return render_template('index.html', bot_name="Bot")

@app.route('/send-message', methods=['POST']) # Using POST method, message is sent
def send_message():
    user_input = request.json['message']

    if user_input.lower() == 'quit':
        return jsonify({"message": "Goodbye!"})  
        
    response = BotLogic.find_match(user_input, [x["question"] for x in database["questions"]])

    if response:
        answer = BotLogic.show_match(response, database)
    else:
        answer = "no has answer, plz tell ;-;"

    return jsonify({"message": answer})

@app.route('/add-response', methods=['POST']) # Using POST method, response is added to json file
def add_response():
    user_input = request.json['question']
    new_response = request.json['answer']
    
    database["questions"].append({"question": user_input, "answer": new_response})
    BotLogic.save_database('data_base.json', database)

    return jsonify({"message": "okie, i\'ll remember this :)"})

if __name__ == "__main__":
    app.run(debug = True)