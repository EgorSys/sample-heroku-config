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
    if message[:5] == "Что в":
        day = message.split()[2][:len(message.split()[2])-1]
        return schedule[day]["lessons"]
    if message[:20] == "Когда заканчивается ":
        if messgage[22] == " ":
            endtime = lesson_time[int(messgage[21])][1]
        else:
            endtime = lesson_time[int(message[20:22])][1]
        return 'в '+str(endtime)
    if message[:16] == "Сколько уроков в":
        day = message.split()[3]
        number = len(schedule[day][lessons])
        return number
    if message[:6] == "Когда " and int(message[6]) < 10:
        starttime = lesson_time[int(message.split()[1]])][0]
        return 'в '+str(starttime)

if __name__ == "__main__":
    # dirty python magic, will talk about on the next lesson
    # just ignore for now

    nick = input("Enter your nickname: ")

    while True:
        msg = input("Your message: ")
        ans = handle_message(msg, nick)
        if msg[:5] == "Что в":
            print(*ans, sep = ', ')
        else:
            print(ans)
