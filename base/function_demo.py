def greet_someone():
    print("hello someone")
greet_someone()

# 除了位置实参，还有关键字参数
def test_param(name, age):
    print(name + " " + str(age))
test_param(age=18, name="xukainan")

# 传递任意数量的实参
def test_params(age = '18', *names):
    print(names)
    print(str(age))
test_params("1","2","3")

# 任意数量的关键字实参
def test_dic_params(first, **user_info):
    print(first)
    for key, value in user_info.items():
        print(key + value)

test_dic_params("first", name ='xukainan', age = '18')
