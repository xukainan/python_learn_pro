alien_o = {'color':'red', 'point':5}
print(alien_o['color'])
alien_o['x_position'] = 1
print(alien_o['x_position'])
del alien_o['point']
print(alien_o)

# 遍历
for key, value in alien_o.items():
    print(key)

for key in alien_o.keys():
    print(key)

for value in alien_o.values():
    print(value)


for key in sorted(alien_o.keys(), reverse=True):
    print(key)

# 独一无二
for key in set(alien_o.keys()):
    print(key)
