import os

os.system("cls")


class Messenger:
    def __init__(self, user, password):
        self.user = user
        self.input_message = []  # sizga kelgan xabarlar
        self.output_message = []  # siz yuborgan xabarlar
        self.status = ""
        self.password = password

    def Send_message(self, new_user):
        message = input("type a message >>> ")
        new_user.output_message.append(message)
        self.input_message.append(message)
        self.status = "Yuborilgan"

    def read_message(self, new_user):
        new_user.status = "O'qilgan"
        print(new_user.input_message)

    def send_file(self):
        with open('file.txt', 'w') as f:
            f.write("Ok")
        self.status = "Yuborildi"
        print("File "+self.status)

    def read_file(self):
        self.status = "O'qilgan"
        print(os.path.exists("file.txt"))

    def delete(self):
        self.input_message.clear()
        self.output_message.clear()
        with open('file.txt', 'w') as f:
            f.write("")
        self.status = "O'chirilgan"
        print(self.status)

user1 = Messenger("Tohirjon", 1)
user2 = Messenger("Muhammadali", 1)

user1.Send_message(user2)
print(user1.status)
user2.read_message(user1)
user1.send_file()
print(user1.status)
user2.read_file()
print(user2.status)
user2.delete()
