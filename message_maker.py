def getReply(message):
    message = message.lower().strip() 
    answer = ""

    if "latest transaction" or "recent transaction" in message:
        answer  = "here is your latest transaction"
    elif "near me" in message:
        answer = "the closest food bank near you is 2 miles away."
    else:
        answer = "please try another question?"
    return answer
