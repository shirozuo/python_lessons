import time


class Loggable:
    def log(self, msg):
        print(str(time.ctime()) + ": " + str(msg))
# ^^^ Remove the top code to test the solution on the website ^^^


class LoggableList (Loggable, list):
    def append(self, __object):
        super().append(__object)
        self.log(__object)


test_string = "Hello World!"
test_string2 = "I'm second test string!"
test_string3 = 31
test_string4 = time.ctime()
test_string5 = id(LoggableList.__class__)

new_loggable_list = LoggableList()
new_loggable_list.append(test_string)
print(new_loggable_list)
new_loggable_list.append(test_string2)
print(new_loggable_list)
new_loggable_list.append(test_string3)
print(new_loggable_list)
new_loggable_list.append(test_string4)
print(new_loggable_list)
new_loggable_list.append(test_string5)
print(new_loggable_list)
