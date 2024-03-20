import json
from difflib import get_close_matches

def get_database(file_path: str) -> dict:
    with open(file_path, 'r') as file:
        data: dict = json.load(file)
    return data

def save_database(file_path: str, data: dict):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent = 2)

def find_match(question: str, questions: list[str]) -> str | None:
    matches: list = get_close_matches(question, questions, n=1, cutoff= 0.6)
    return matches[0] if matches else None

def show_match(question: str, database: dict) -> str | None:
    for q in database["questions"]:
        if q["question"] == question:
            return q["answer"]
        
def bot():
    database: dict = get_database("data_base.json")

    while True:
        user_input = input("You: ")

        if user_input.lower() == 'quit':
            break
        
        response: str | None = find_match(user_input, [x["question"] for x in database["questions"]])

        if response:
            answer = show_match(response, database)
            print(f'wAIfu: {answer}')
        else:
            print('wAIfu: No has answer, plz tell ;-;')
            new_response = input('New Answer: ')

            database["questions"].append({"question": user_input, "answer": new_response})
            save_database('data_base.json', database)
            print('wAIfu: okie, i\'ll remember this :)')


if __name__ == "__main__": 
    bot()