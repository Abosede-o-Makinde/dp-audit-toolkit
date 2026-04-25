# Input validation

def validate_response(response):
    return response.lower() in ['yes', 'no']

def validate_scores(scores):
    for score in scores.values():
        if not (0 <= score <= 100):
            raise ValueError("Score out of range")