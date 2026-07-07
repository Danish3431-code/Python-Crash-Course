# RULE BASED CHAT BOT

print("Hello, welcome to AI Chat Bot")
print("Ask me your Question?")

#memory for chat-bot
response={
    "hello":"Hello!, how can i help you:",
    "how are you":"I am fine , Thankyou:",
    "motivate me":"keep going , every bug of your project makes you a better:",
    "happy":"great to hear that:",
    "what are functions":"go and learn it from the rishab mishra python youtube playlist:"
}

#fuction to get response from chatbot
def getresponsefrombot(userQuestion):
    userQuestion=userQuestion.lower()
    for eachKey in response:
        if eachKey in userQuestion:
            return response[eachKey]
    
    return "i am not able to tell you"

#Take user input
while True:
    userInput=input("please ask the question:")
    reply=getresponsefrombot(userInput)

    print("Bot Response: ",reply)

    if "bye" in userInput.lower():
        print("ok good bye")
        break
    


