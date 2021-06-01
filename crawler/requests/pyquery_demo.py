html = '''
<div>
    <ul>
         <li class="item-0">first item</li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
         <li class="item-1 active"><a href="link4.html">fourth item</a></li>
         <li class="item-0"><a href="link5.html">fifth item</a></li>
     </ul>
 </div>
'''
from pyquery import PyQuery as pq
# doc = pq(html)
# print(doc('li'))


# doc = pq(url='https://cuiqingcai.com')
# print(doc('title'))

#还可以传本地文件
# doc = pq(filename='demo.html')
# print(doc('li'))

#css 选择器
# doc = pq(html)
# print(doc('#container .list li'))
# print(type(doc('#container .list li')))

# 子节点
# doc = pq(html)
# items = doc('.list')
# print(type(items))
# print(items)
# # lis = items.children() #子节点
# lis = items.find('li')  #所有子孙节点
# print(type(lis))
# print(lis)


# 父节点
# doc = pq(html)
# items = doc('.list')
# container = items.parent()
# print(type(container))
# print(container)


# 兄弟节点
# doc = pq(html)
# li = doc('.list .item-0.active')
# print(li.siblings())

# 获取属性
# doc = pq(html)
# a = doc('.item-0.active a')
# print(a, type(a))
# #print(a.attr('href'))  #调用 attr 方法，只会得到第 1 个节点的属性。
# a = doc('a')
# for item in a.items():
#     print(item.attr('href'))


# 获取文本
# doc = pq(html)
# a = doc('.item-0.active a')
# print(a)
# print(a.text())


# 节点操作 ： addClass 和 removeClass
# doc = pq(html)
# li = doc('.item-0.active')
# print(li)
# li.removeClass('active')
# print(li)
# li.addClass('active')
# print(li)


# 节点操作
# doc = pq(html)
# li = doc('.item-0.active')
# print(li)
# li.attr('name', 'link')
# print(li)
# li.text('changed item')
# print(li)
# li.html('<span>changed item</span>')
# print(li)


#remove
# doc = pq(html)
# wrap = doc('.wrap')
# print(wrap.text())


#伪类选择器
#CSS 选择器之所以强大，还有一个很重要的原因，那就是它支持多种多样的伪类选择器，例如选择第一个节点、最后一个节点、奇偶数节点、包含某一文本的节点等
doc = pq(html)
li = doc('li:first-child')
print(li)
li = doc('li:last-child')
print(li)
li = doc('li:nth-child(2)')
print(li)
li = doc('li:gt(2)')
print(li)
li = doc('li:nth-child(2n)')
print(li)
li = doc('li:contains(second)')
print(li)