import json
from bot_logic import BotLogic
from difflib import get_close_matches
from difflib import SequenceMatcher


        
def bot(bot_name: str):
    database: dict = BotLogic.get_database("data_base.json")

    while True:
        user_input = input("You: ")

        if user_input.lower() == 'quit':
            break
        
        
        response: str | None = BotLogic.find_match(user_input, [x["question"] for x in database["questions"]])

        if SequenceMatcher(None, user_input, "What is your name?").ratio() > 0.7:
            print(f"{bot_name}: my name is {bot_name}, nice to meet you love <3")
        elif response:
            answer = BotLogic.show_match(response, database)
            print(f'{bot_name}: {answer}')
        else:
            print(f'{bot_name}: No has answer, plz tell ;-;')
            new_response = input('New Answer: ')

            database["questions"].append({"question": user_input, "answer": new_response})
            BotLogic.save_database('data_base.json', database)
            print(f'{bot_name}: okie, i\'ll remember this :)')


if __name__ == "__main__":
    print("Welcome to the wAIfu Interactive ChatBot!\n\n")

    bot_name = input("Please enter the desired name of your waifu: ")
    print("\n")

    bot(bot_name)