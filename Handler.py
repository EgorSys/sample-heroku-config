import requests
import json
URL = "https://api.telegram.org/bot<485196249:AAGOPYcyVHFAefxo2p8JJeKQEQ_Y2C2RSSo>/getUpdates"

response = requests.get(URL)
updates = response.json()
def handle_message(message, nickname="user"):
    '''handles message: 
    @message - text of recieved message
    @nickname - nickname of sender

    @returns - text of response
    '''
    message = updates["response"][len(updates["response"])-1]["text"]
    nickname = updates["response"][len(updates["response"])-1]["nickname"]
    chatid = updates["response"][len(updates["response"])-1]["chat_id"]
    answer = requests.get("https://api.telegram.org/bot<485196249:AAGOPYcyVHFAefxo2p8JJeKQEQ_Y2C2RSSo>/sendMessage?chat_id=chatid&text=message")
    return answer

if __name__ == "__main__":
    # dirty python magic, will talk about on the next lesson
    # just ignore for now

    nick = input("Enter your nickname: ")

    while True:
        msg = input("Your message: ")
        ans = handle_message(msg, nick)
        print(ans)