spam = True
def handle_response(message) -> str:
    global spam
    p_message = message.content.lower()
    author_id = str(message.author.id)

    if p_message == "/help":
        return """
`/help - Displays this message.
/test - Tests if this bot works or not.
* More commands coming in the future *`
"""
    elif p_message == "/test":
        return "This bot is working."

    elif p_message == "/spam":
        if author_id == '985091468840550400':
            spam = True
            return f"""Spam :)
Spam :)
Spam :)
Spam :)
Spam :)
Spam :)
Spam :)
Spam :)
Spam :)
Spam :)
Spam :)
Spam :)"""
        else:
            return "You do not have permission to use this command."
    elif p_message == "stop":
        if author_id == "985091468840550400":
            spam = False
            return "Stopping spam. Please wait. Spam will stop in a few seconds."
    elif p_message == f"""spam :)
spam :)
spam :)
spam :)
spam :)
spam :)
spam :)
spam :)
spam :)
spam :)
spam :)
spam :)""":
        if spam:
            if author_id == "1158334648871559250":
                return f"""Spam :)
Spam :)
Spam :)
Spam :)
Spam :)
Spam :)
Spam :)
Spam :)
Spam :)
Spam :)
Spam :)
Spam :)"""
        else:
            return "Spam stopped."