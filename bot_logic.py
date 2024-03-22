import json
from difflib import get_close_matches

class BotLogic:
    @staticmethod
    def get_database(file_path: str) -> dict:
        with open(file_path, 'r') as file:
            data: dict = json.load(file)
        return data
    
    @staticmethod
    def save_database(file_path: str, data: dict):
        with open(file_path, 'w') as file:
            json.dump(data, file, indent = 2)

    def find_match(question: str, questions: 'list[str]') -> str | None:
        matches: list = get_close_matches(question, questions, n=1, cutoff= 0.6)
        return matches[0] if matches else None

    def show_match(question: str, database: dict) -> str | None:
        for q in database["questions"]:
            if q["question"] == question:
                return q["answer"]