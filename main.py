"""Created by Ostap Kutyanskyy 22.09.18"""
import json

# data = {
#
# }
#
# with open("translation.json") as file:
#     dict = json.load(file)
#
# dict.update(data)
#
# with open("translation.json", "w") as file:
#     json.dump(dict, file, indent=4, ensure_ascii=False)
#
# file = open("translation.json", "r")
#
# with open("translation.json", "r") as read_file:
#     x = json.load(read_file)
# print(x["kek"])
from typing import List


def inputTranslate():
    print("Enter a word and a translation via space")
    isActive = True
    words = []
    while isActive:
        tr = input()
        tr = tr.strip()
        if tr == "exit":
            isActive = False
        else:
            tr = tr.split(" ")
            if "" in tr:
                for i in tr:
                    tr.remove("")
            print(tr)
            words.append(tr)
    print(words)

    dict = {}
    for i in words:
        dict[i[0].lower()] = i[1].lower()

    with open("translation.json", "r") as file:
        data = json.load(file)

    data.update(dict)

    with open("translation.json", "w") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)


isActive = True

while isActive:
    command = input("Enter help for more info : ")
    if command.strip() == "translate":
        str = ""
        result = []
        noTr = []
        message = input("Enter your sentance : ").strip()
        if "," in message:
            message = message.split(",")
            for i in range(len(message)):
                message[i] = message[i].strip().split(" ")
        else:
            message = message.split(" ")

        print(message)
        with open("translation.json", "r") as file:
            data = json.load(file)

        for i in message:
            if any(isinstance(i, list) for k in message):
                for j in i:
                    if j.lower() in data:
                        str = data[j.lower()]
                        result.append(str)
                        continue
                result.append(",")
            elif i.lower() in data:
                result.append(data[i.lower()])

            else:
                noTr.append(i)

        if noTr:
            print("There is no translate to these words: ")
            for i in noTr:
                print(i)
            command = input("Enter \"add\" to add translation : ")
            while 1:
                if command == "add":
                    inputTranslate()
                    break
                elif command == 'exit':
                    break
                else:
                    command = input("Enter \"add\" to add translation")
                    continue
        else:
            str = ""
            translation = []
            for i in range(len(result)):
                if result[i] == ".":
                    str += result[i] + " "
                    translation.append(str.strip())
                    str = " "
                    continue
                else:
                    str += result[i] + " "
            translation.append(str)
            for i in translation:
                if i[0] == " ":
                    print(i[1].upper() + i[2:],end="")
                else:
                    print(i.capitalize(), end="")
            print("\n")




    elif command.strip() == "help":
        print("""
Available commands :
1) help 
2) translate
3) exit
""")
    elif command.strip() == "exit":
        exit()
    else:
        print("WRONG_COMMAND")
        continue
