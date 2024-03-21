import json
from difflib import get_close_matches
from difflib import SequenceMatcher

def get_database(file_path: str) -> dict:
    with open(file_path, 'r') as file:
        data: dict = json.load(file)
    return data

def save_database(file_path: str, data: dict):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent = 2)

def find_match(question: str, questions: list[str]) -> str | None:
    matches: list = get_close_matches(question, questions, n=1, cutoff= 0.4)
    return matches[0] if matches else None

def show_match(question: str, database: dict) -> str | None:
    for q in database["questions"]:
        if q["question"] == question:
            return q["answer"]
        
def bot(bot_name: str):
    database: dict = get_database("data_base.json")

    while True:
        user_input = input("You: ")

        if user_input.lower() == 'quit':
            break
        
        
        response: str | None = find_match(user_input, [x["question"] for x in database["questions"]])

        if SequenceMatcher(None, user_input, "What is your name?").ratio() > 0.7:
            print(f"{bot_name}: my name is {bot_name}, nice to meet you love <3")
        elif response:
            answer = show_match(response, database)
            print(f'{bot_name}: {answer}')
        else:
            print(f'{bot_name}: No has answer, plz tell ;-;')
            new_response = input('New Answer: ')

            database["questions"].append({"question": user_input, "answer": new_response})
            save_database('data_base.json', database)
            print(f'{bot_name}: okie, i\'ll remember this :)')


if __name__ == "__main__":
    print("Welcome to the wAIfu Interactive ChatBot!\n\n") 
    bot_name = input("Please enter the desired name of your waifu: ")
    print("\n")

    bot(bot_name)