import re

import csv

f = open('213.txt', encoding = 'utf-8')
data = f.read()

name = re.search(r"Филиал ТОО.+", data)
binn = re.search(r"БИН\s(\d{12})", data)

title = re.findall(r"\d+\.\n(.+)", data)
count = re.findall(r"(\d)\,0{3}", data)
unit = re.findall(r"x\s(.+)\,0{2}", data)
total = re.findall(r"Стоимость\n(.+),0{2}", data)

date = re.search(r"(\d\d.\d\d.\d{4}\s\d\d.\d\d.\d\d)", data)
address = re.search(r"г\..+", data)

print(name.group())
print(binn.group())
for i in range(len(title)):
    print("1. Title: " + title[i])
    print("2. Count: " + count[i])
    print("3. Unit price: " + unit[i])
    print("4. Total price: " + total[i])
print(date.group())
print(address.group())
print(binn.group(1))



with open('names.csv', 'w', newline='') as csvfile:
    fieldnames = ['Title', 'Count', 'Unit price', 'Total price']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    # writer.writerow({'first_name': 'Baked', 'last_name': 'Beans', 'Bagdat': '18'})
    for i in range(len(title)):
    	writer.writerow({'Title': f'{title[i]}', 'Count': f'{count[i]}', 'Unit price': f'{unit[i]}', 'Total price': f'{total[i]}'})