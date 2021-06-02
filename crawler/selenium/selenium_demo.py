from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains
from selenium.common.exceptions import NoSuchElementException


import time

browser = webdriver.Chrome()  # 声明浏览器对象 Selenium 支持非常多的浏览器，如 Chrome、Firefox、Edge 等，还有 Android、BlackBerry 等手机端的浏览器。
try:
    '''
    browser.get('https://www.baidu.com')
    input = browser.find_element_by_id('kw')
    #input_second = browser.find_element_by_css_selector('#q') CSS 选择器
    #input_third = browser.find_element_by_xpath('//*[@id="q"]')  XPath
    #input_first = browser.find_element(By.ID, 'q')   find_element 它需要传入两个参数：查找方式 By 和值。
    # find_elements  多个节点
    input.send_keys('Python')
    input.send_keys(Keys.ENTER)
    wait = WebDriverWait(browser, 10)
    wait.until(EC.presence_of_element_located((By.ID, 'content_left')))
    print(browser.current_url)
    print(browser.get_cookies())
    print(browser.page_source)
    '''
    '''
    find_elements_by_id 
    find_elements_by_name 
    find_elements_by_xpath 
    find_elements_by_link_text 
    find_elements_by_partial_link_text 
    find_elements_by_tag_name 
    find_elements_by_class_name 
    find_elements_by_css_selector
    

    browser.get('https://www.taobao.com')
    lis = browser.find_elements_by_css_selector('.service-bd li')
    print(lis)
    browser.close()
    
    '''

    '''
    #输入文字时用 send_keys 方法，清空文字时用 clear 方法，点击按钮时用 click 方法
    browser.get('https://www.taobao.com')
    input = browser.find_element_by_id('q')
    input.send_keys('iPhone')
    time.sleep(1)
    input.clear()
    input.send_keys('iPad')
    button = browser.find_element_by_class_name('btn-search')
    button.click()
    '''

    '''
    #实现一个节点的拖拽操作（动作链）

    url = 'http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable'
    browser.get(url)
    browser.switch_to.frame('iframeResult')
    source = browser.find_element_by_css_selector('#draggable')
    target = browser.find_element_by_css_selector('#droppable')
    actions = ActionChains(browser)
    actions.drag_and_drop(source, target)
    actions.perform()
    '''

    '''
    #执行 JavaScript Selenium API 并没有提供实现某些操作的方法，比如，下拉进度条。但它可以直接模拟运行 JavaScript
    browser.get('https://www.zhihu.com/explore')
    browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')
    browser.execute_script('alert("To Bottom")')
    '''

    '''
    #获取属性、文本值
    url = 'https://dynamic2.scrape.center/'
    browser.get(url)
    logo = browser.find_element_by_class_name('logo-image')
    print(logo)
    print(logo.get_attribute('src'))
    input = browser.find_element_by_class_name('logo-title')
    print(input.text)
    #ID、位置、标签名、大小
    print(input.id)
    print(input.location)
    print(input.tag_name)
    print(input.size)
    '''

    '''
    #切换 Frame Selenium 打开页面后，默认是在父级 Frame 里面操作，而此时如果页面中还有子 Frame，Selenium 是不能获取到子 Frame 里面的节点的。这时就需要使用 switch_to.frame 方法来切换 Frame。
    url = 'http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable'
    browser.get(url)
    browser.switch_to.frame('iframeResult')
    try:
        logo = browser.find_element_by_class_name('logo')
    except NoSuchElementException:
        print('NO LOGO')
    browser.switch_to.parent_frame()
    logo = browser.find_element_by_class_name('logo')
    print(logo)
    print(logo.text)
    '''

    '''
    #延时等待 在 Selenium 中，get 方法会在网页框架加载结束后结束执行，此时如果获取 page_source，可能并不是浏览器完全加载完成的页面，如果某些页面有额外的 Ajax 请求，我们在网页源代码中也不一定能成功获取到。所以，这里需要延时等待一定时间，确保节点已经加载出来。
    #隐式等待 定了一个固定时间
    browser.implicitly_wait(10)
    browser.get('https://dynamic2.scrape.center/')
    input = browser.find_element_by_class_name('logo-image')
    print(input)
    #显式等待 它指定要查找的节点，然后指定一个最长等待时间。如果在规定时间内加载出来了这个节点，就返回查找的节点；如果到了规定时间依然没有加载出该节点，则抛出超时异常
    browser.get('https://www.taobao.com/')
    wait = WebDriverWait(browser, 10)
    input = wait.until(EC.presence_of_element_located((By.ID, 'q'))) #在 10 秒内如果 ID 为 q 的节点（即搜索框）成功加载出来，就返回该节点；如果超过 10 秒还没有加载出来，就抛出异常。
    button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.btn-search'))) #如果 10 秒内它是可点击的，也就代表它成功加载出来了，就会返回这个按钮节点；如果超过 10 秒还不可点击，也就是没有加载出来，就抛出异常。
    print(input, button)
    #引入 WebDriverWait 这个对象，指定最长等待时间，然后调用它的 until() 方法，传入要等待条件 expected_conditions。比如，这里传入了 presence_of_element_located 这个条件，代表节点出现，其参数是节点的定位元组，也就是 ID 为 q 的节点搜索框。
    '''

    '''
    #前进后退
    browser.get('https://www.baidu.com/')
    browser.get('https://www.taobao.com/')
    browser.get('https://www.python.org/')
    browser.back()
    time.sleep(1)
    browser.forward()
    browser.close()
    '''

    '''
    #Cookies
    browser.get('https://www.zhihu.com/explore')
    print(browser.get_cookies())
    browser.add_cookie({'name': 'name', 'domain': 'www.zhihu.com', 'value': 'germey'})
    print(browser.get_cookies())
    browser.delete_all_cookies()
    print(browser.get_cookies())
    '''

    '''
    #选项卡管理
    browser.get('https://www.baidu.com')
    browser.execute_script('window.open()')
    print(browser.window_handles)
    browser.switch_to.window(browser.window_handles[1])
    browser.get('https://www.taobao.com')
    time.sleep(1)
    browser.switch_to.window(browser.window_handles[0])
    browser.get('https://python.org')
    '''

    #反屏蔽




finally:
    browser.close()