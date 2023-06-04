#  You can experiment here, it won’t be checked
# class River:
#     # list of all rivers
#     all_rivers = []
#
#     def __init__(self, name, length):
#         self.name = name
#         self.length = length
#         # add current river to the list of all rivers
#         River.all_rivers.append(self)
#
#
import time
current_time = time.gmtime()



class Robot:
    def greet(self):
        print("I am a robot")


class Android(Robot):
    def greet(self):
        super().greet()
        print("I am an android")


class PersonalAssistant(Robot):
    def greet(self):
        super().greet()
        print("I am a personal assistant")


class AssistantAndroid(Android, PersonalAssistant):
    def greet(self):
        super().greet()


a = AssistantAndroid()
a.greet()
print(AssistantAndroid.__mro__)
