import csv
with open('next.csv','w',newline='') as file:
    columnames=['id','name','age']
    record=csv.DictWriter(file,columnames)
    record.writeheader()
    data=[
        {'id':1,'name':'suresh','age':22},
        {'id':2,'name':'ramesh','age':21},
        {'id':3,'name':'mahesh','age':29},
    ]
    record.writerows(data)

    with open('next.csv','r',newline='') as file:
        records=csv.DictReader(file)
        for i in records:
            print(i)