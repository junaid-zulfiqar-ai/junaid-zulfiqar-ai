def response(hey_bob):
    cleaned_speech = hey_bob.strip()
    if not cleaned_speech:
        return "Fine. Be that way!"
    is_yelling = cleaned_speech.isupper()
    is_question = cleaned_speech.endswith('?')
    if is_yelling and is_question:
        return "Calm down, I know what I'm doing!"
    elif is_yelling:
        return "Whoa, chill out!"
    elif is_question:
        return "Sure."
    else:
        return "Whatever."

