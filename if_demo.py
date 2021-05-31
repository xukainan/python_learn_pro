cars = ['audi', 'bmw', 'subaru']
for car in cars:
    if car == 'bmw':
        print(car.upper())

# 多个条件
ages = [18, 19, 30, 25, 60]
#确定列表不为空
if ages:
    print("ages is not empty")
for age in ages:
    if age>20 and age<=30:
        print(age)
    if age < 20 or age > 50:
        print("or" + str(age))
if 19 in ages:
    print("19 in ages...")
elif 20 in ages:
    print("20 in ages...")

if 60 not in ages:
    print("not in")
else:
    print("in")

