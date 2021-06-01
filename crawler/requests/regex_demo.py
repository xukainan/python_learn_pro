import re

# content = 'Hello 123 4567 World_This is a Regex Demo'
# print(len(content))
# result = re.match('^Hello\s\d\d\d\s\d{4}\s\w{10}', content)
# print(result)
# print(result.group()) #group 方法可以输出匹配的内容
# print(result.span()) #span 方法可以输出匹配的范围

#可以将数字部分的正则表达式用 () 括起来，然后调用了 group(1) 获取匹配结果。
# content = 'Hello 1234567 World_This is a Regex Demo'
# result = re.match('^Hello\s(\d+)\sWorld', content)
# print(result)
# print(result.group())
# print(result.group(1))
# print(result.span())

#通用匹配符
# content = 'Hello 123 4567 World_This is a Regex Demo'
# result = re.match('^Hello.*Demo$', content)
# print(result)
# print(result.group())
# print(result.span())

# 贪婪与非贪婪
# content = 'Hello 1234567 World_This is a Regex Demo'
# result = re.match('^He.*(\d+).*Demo$', content)
# print(result)
# print(result.group(1))
# 奇怪的事情发生了，我们只得到了 7 这个数字，这是怎么回事呢？
# 这里就涉及一个贪婪匹配与非贪婪匹配的问题了。在贪婪匹配下，.* 会匹配尽可能多的字符。正则表达式中 .* 后面是 \d+，也就是至少一个数字，并没有指定具体多少个数字，因此，.* 就尽可能匹配多的字符，这里就把 123456 匹配了，给 \d+ 留下一个可满足条件的数字 7，最后得到的内容就只有数字 7 了。
# content = 'Hello 1234567 World_This is a Regex Demo'
# result = re.match('^He.*?(\d+).*Demo$', content)
# print(result)
# print(result.group(1))


#修饰符
# content = '''Hello 1234567 World_This
# is a Regex Demo
# '''
# # result = re.match('^He.*?(\d+).*?Demo$', content)
# result = re.match('^He.*?(\d+).*?Demo$', content, re.S)  #修饰符的作用是匹配包括换行符在内的所有字符。
# print(result.group(1))


#转义匹配
# content = '(百度) www.baidu.com'
# result = re.match('\(百度 \) www\.baidu\.com', content)
# print(result)


#search match 方法是从字符串的开头开始匹配的，一旦开头不匹配，那么整个匹配就失败了。
# content = 'Extra stings Hello 1234567 World_This is a Regex Demo Extra stings'
# # result = re.match('Hello.*?(\d+).*?Demo', content)
# result = re.search('Hello.*?(\d+).*?Demo', content)
# print(result)


#findall 获取search的所有匹配内容
# html = '''<div id="songs-list">
# <h2 class="title">经典老歌</h2>
# <p class="introduction">
# 经典老歌列表
# </p>
# <ul id="list" class="list-group">
# <li data-view="2">一路上有你</li>
# <li data-view="7">
# <a href="/2.mp3" singer="任贤齐">沧海一声笑</a>
# </li>
# <li data-view="4" class="active">
# <a href="/3.mp3" singer="齐秦">往事随风</a>
# </li>
# <li data-view="6"><a href="/4.mp3" singer="beyond">光辉岁月</a></li>
# <li data-view="5"><a href="/5.mp3" singer="陈慧琳">记事本</a></li>
# <li data-view="5">
# <a href="/6.mp3" singer="邓丽君">但愿人长久</a>
# </li>
# </ul>
# </div>'''
# results = re.findall('<li.*?href="(.*?)".*?singer="(.*?)">(.*?)</a>', html, re.S)
# print(results)
# print(type(results))
# for result in results:
#     print(result)
#     print(result[0], result[1], result[2])


#sub 借助它来修改文本。比如，想要把一串文本中的所有数字都去掉，如果只用字符串的 replace 方法，那就太烦琐了，这时可以借助 sub 方法。
# content = '54aK54yr5oiR54ix5L2g'
# content = re.sub('\d+', '', content)
# print(content)


#compile 这个方法可以将正则字符串编译成正则表达式对象，以便在后面的匹配中复用。
content1 = '2019-12-15 12:00'
content2 = '2019-12-17 12:55'
content3 = '2019-12-22 13:21'
pattern = re.compile('\d{2}:\d{2}')
result1 = re.sub(pattern, '', content1)
result2 = re.sub(pattern, '', content2)
result3 = re.sub(pattern, '', content3)
print(result1, result2, result3)