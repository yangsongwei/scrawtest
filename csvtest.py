import csv
import pandas

with open('data.csv', 'w') as csvfile:
    fieldnames = ['id', 'name', 'age']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({'id': '10001', 'name': 'Mike', 'age': 20})
    writer.writerow({'id': '10002', 'name': 'Bob', 'age': 22})
    writer.writerow({'id': '10003', 'name': 'Jordan', 'age': 21})


# with open('data.csv','r',encoding='utf-8') as file:
#     reader=csv.reader(file)
#     for i in reader:
#         print(i)

data=pandas.read_csv('data.csv')
print(data.items)

