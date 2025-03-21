import json
import os

BASE_DIR = os.path.dirname(os.path.realpath(__file__))

PROS = {
    "helpful": ["helpful", "useful", "good for learning", "educational"],
    "design": ["cute", "nice design", "visually appealing"],
    "potential": ["potential", "improves", "growth"],
    "engaging": ["fun", "enjoyable", "immersive", "consistent"],
}

CONS = {
    "bugs_issues": ["bug", "issue", "glitch", "crash", "unresolved"],
    "repetitive": ["repetitive", "boring", "same activities"],
    "slow_performance": ["slow", "loading", "lag", "freeze"],
    "difficulty": ["hard", "difficult", "unclear", "confusing"],
    "grammar": ["misspelled", "spelling", "typo"],
}


def review_parser():
    page = 1
    pros = {key: 0 for key in PROS.keys()}
    cons = {key: 0 for key in CONS.keys()}

    while os.path.exists(f"{BASE_DIR}/reviews/page{page}.json"):
        file_path = f"{BASE_DIR}/reviews/page{page}.json"
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
            for review in data["data"]:
                review_lower = review["text"].lower()
                for key, words in PROS.items():
                    if any(word in review_lower for word in words):
                        pros[key] += 1
                for key, words in CONS.items():
                    if any(word in review_lower for word in words):
                        cons[key] += 1
        page += 1

    return pros, cons


print(review_parser())
