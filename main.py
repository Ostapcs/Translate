"""Created by Ostap Kutyanskyy 22.09.18"""
import json

# data = {
#     "loh": "лох",
#     "fuck": "кек",
#     "shit": "c++"
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


def inputTranslate():
    print("Enter a word and a translation via space")
    isActive = True
    words = []
    while isActive:
        command = input()
        if command == "exit":
            isActive = False
        else:
            command = command.split(" ")
            if "" in command:
                for i in command:
                    command.remove("")
            print(command)
            words.append(command)
    print(words)

    dict= {}
    for i in words:
        dict[i[0]] = i[1]

    with open("translation.json","r") as file:
        data = json.load(file)

    data.update(dict)

    with open("translation.json", "w") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)



message = input("Enter your sentance : ")
message.split(" ")
print(message)
with open("translation.json", "r") as file:
    data = json.load(file)
print (data)
# for i in data:
#     for j in message:
#         if data[i] !=
