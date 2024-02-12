import datetime

input_list = input().split()
date = datetime.date(int(input_list[0]), int(input_list[1]), int(input_list[2]))

input_list = input()

date = date + datetime.timedelta(float(input_list))

date_list = str(date).split("-")
date_list2 = list()

for i in date_list:
    date_list2.append(int(i))

print(*date_list2)
