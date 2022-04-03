def clean_message(body):
    return body['event']['text'].lower().strip()