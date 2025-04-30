import csv
file = open ('mydata.xlsx', 'w')
file = csv.writer(file)
file.writerow(['Name','Age','Employment Number'])
n = int(input('How many records you want to insert:'))
for i in range(n):
    name = input(f'{i+1}. Enter name')
    age = input(f'{i+1}. Enter age')
    enroll = input(f'{i+1}. Enter Enrollment number')
    file.writerow([name,age,enroll])
    print()
print('All records inserted successfully')



   