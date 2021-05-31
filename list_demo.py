names = ["yanhua", "xukainan"]
print(names)
print(names[0])
print(names[-1])
names[0] = "lixiaodong"
print(names[0])
names.append("yanhua")
print(names)
names.insert(1,"dongge")
print(names)
del names[1]
print(names)
print(names.pop(0))
print(names)
names.remove("yanhua")
print(names)
nums = [1, 0, 8, 4, 3]
# 翻转列表
nums.reverse()
print(nums)

# 临时排序，不影响原始列表顺序
print(sorted(nums))
print(sorted(nums, reverse=True))
print(nums)

# 永久排序
nums.sort()
print(nums)
nums.sort(reverse=True)
print(nums)

# 数组长度
print(len(nums))

# for循环
for item in nums:
    print(item)
print("for end...")

# range
for item in range(1,5):
    print(item)

print("range end...")
# range 步长
even_nums = list(range(1, 10, 2))
for item in even_nums:
    print(item)

# 函数
print(max(even_nums))
print(sum(even_nums))

# 列表解析
squares = [value**2 for value in range(1,11)]
print(squares)

# 切片
players = ['charles', 'michael', 'eli']
print(players[0:1])
print(players[2:])
print(players[-1:])
# 复制列表
new_players = players[:]
print(new_players)
new_players = players[-1:]
print(new_players)


# 元祖 ： 不可变的列表
dimensions = (200, 50)
print(dimensions[0])
# dimensions[0] = 250 报错, 虽然不可以修改，但是可以重新定义
dimensions = (250, 50)
print(dimensions[0])
