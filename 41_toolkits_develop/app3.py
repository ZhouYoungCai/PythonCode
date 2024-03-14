from selenium import webdriver  ###导入selenium库


def nbat():
    driver = webdriver.Chrome()  ####实例化浏览器
    option = webdriver.ChromeOptions()
    option.add_experimental_option("detach", True)
    driver = webdriver.Chrome(executable_path='C:\Python27/chromedriver.exe', options=option)

    ###写入NBA图文数据的网址
    driver.get(
        'https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&tn=baidu&wd=nba&oq=python&rsv_pq=c18baa0e00004f4f&rsv_t=9655EB0Ke9Xsp6M3b%2BNToueiabZBl8ljQrRtdyJjHiJMB3h%2Bop6ZTZ%2FYLvU&rqlang=cn&rsv_enter=1&rsv_dl=tb&rsv_sug3=7&rsv_sug1=7&rsv_sug7=100&rsv_sug2=0&rsv_btype=t&inputT=627&rsv_sug4=2425')  ###进入此网址

    ###页面最大化显示
    driver.maximize_window()