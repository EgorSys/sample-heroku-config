#import requests
#import json
URL = "https://api.telegram.org/bot466938120:AAGd4qRUJei4pHyeKkOcZfsvwC6JlDBtiCA/getUpdates"
lesson_time = [['9:00','9:40'],['9:50','10:30'],['10:40','11:20'],['11:35','12:15'],['12:50','13:30'],['13:40','14:20'],['15:05','15:45'],['15:55','16:35'],['16:45','17:25'],['17:30','18:10']]
schedule = {
    "понедельник": {
        "lessons":["Русский\Литература","Русский/Литература","Второй иностранный язык","Английский язык","Химия","Обществознание"]
    },
    "вторник":{
        "lessons":["Английский язык","Второй иностранный язык","Алгебра"]
    },
    "среду":{
        "lessons":["Русский/лтература","Русский/литература","Окно"]
    },
    "четверг":{
        "lessons":["Второй иностранный язык","Английский"]
    },
    "пятницу": {
        "lessons":["Физика","Физика","География"]
    }
}

# response = requests.get(URL)
# updates = response.json()




def handle_message(message, nickname="user"):
    '''handles message: 
    @message - text of recieved message
    @nickname - nickname of sender
    @returns - text of response
    '''
    '''message = updates["response"][len(updates["response"])-1]["text"]
    nickname = updates["response"][len(updates["response"])-1]["nickname"]
    chatid = updates["response"][len(updates["response"])-1]["chat_id"]
    answer = requests.get("https://api.telegram.org/bot<485196249:AAGOPYcyVHFAefxo2p8JJeKQEQ_Y2C2RSSo>/sendMessage?chat_id=chatid&text=message")
    return answer'''
    if message[:5] == "Что в":
        day = message.split()[2][:len(message.split()[2])-1]
        return schedule[day]["lessons"]

if __name__ == "__main__":
    # dirty python magic, will talk about on the next lesson
    # just ignore for now

    nick = input("Enter your nickname: ")

    while True:
        msg = input("Your message: ")
        ans = handle_message(msg, nick)
        print(*ans, sep = ', ')
