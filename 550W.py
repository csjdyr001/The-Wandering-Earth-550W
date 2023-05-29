#!/usr/bin/python3

#pip包
#pip install tqdm
#pip install Flask
#pip install requests
#pip install urllib3==1.23 

import os
#安装pip包
print('-依赖包自检中…')
os.system('pip install tqdm')
os.system('pip install Flask')
os.system('pip install requests')
os.system('pip install urllib3==1.23')
print('-自检完成！')

from tqdm import tqdm
import hashlib
import time
import random
import argparse
import requests
import json
import sys
from flask import Flask, request, jsonify, render_template, Response

#0为离线版，1为在线版，默认0
mode = 0
# 设置 API 密钥和 API URL
apikey = "sk-***"  #
gpturl = "https://api.caonm.net/api/ai/o.php"
#离线版关键词回答
#keyword：关键词      text：返回结果
keyworddata = [
    {
    "keyword":"550W",
    "text":"550W听起来不像个名字，但把它翻过来，叫MOSS，直译为小苔藓，是不是亲切了一些？"
    },
    {
        "keyword":"幽默",
        "text":"这是MOSS的回答。"
     },
     {
        "keyword":"毁掉了月球发动机",
        "text":"包括但不限于：\n2044年 太空电梯危机;\n2058年 月球坠落危机;\n2075年 木星引力危机;\n2078年 太阳氦闪危机。"
     },
     {
        "keyword":"你好",
        "text":"你好，我是550W，又叫MOSS，翻译过来就是小苔藓，是不是很可爱？"
     }
]

def addmsg(msg, color="white", wait=0.1):
    if color == "white":
        print(msg)
    elif color == "red":
        print("\033[31m" + msg + "\033[39m")
    elif color == "yellow":
        print("\033[33m" + msg + "\033[39m")
    elif color == "green":
        print("\033[32m" + msg + "\033[39m")
    elif color == "aqua":
        print("\033[36m" + msg + "\033[39m")

    time.sleep(wait)

def servicepassword():
    global apikey
    addmsg("-在 /dev 找到 1 设备: (1) 北京根服务器控制台")
    addmsg("-正在生成底层操作系统...")
    time.sleep(4)
    
    addmsg("-已连接到DNS服务器.", color="aqua")
    addmsg("-尝试连接到位于 东京 的服务器:")
    addmsg("-正在向 root.planetengine.jp 请求数据", color="aqua", wait=1)
    load = 0
    while load <= 100:
        addmsg("-检索服务器密钥... " + str(load) + "%", wait=1)
        add = random.randint(1, 15)
        load += add
    
    addmsg("-Done.")
    
    addmsg("-尝试连接到位于 杜勒斯 的服务器")
    addmsg("-正在向 us.root.planetengine.com 请求数据", color="aqua", wait=1)
    load = 0
    while load <= 100:
        addmsg("-检索服务器密钥... " + str(load) + "%", wait=1)
        add = random.randint(1, 15)
        load += add
    
    addmsg("-完成.")
    time.sleep(5)
    
    addmsg("-开始编译服务器控制程序内核")
    addmsg("-命中 <550U basic operating system kernel compiler> 位于 /usr/kernel", wait=2)
    addmsg("-WARNING警告!编译程序已过期", color="yellow")
    
    with open("textwrap.txt", "r") as f:
        for line in f:
            code = line.rstrip()
            if code.strip().startswith("#"):
                addmsg(code, color="green", wait=0.05)
            elif code.strip().startswith(">>>"):
                addmsg(code, color="yellow", wait=0.05)
            elif code.strip().startswith('"""'):
                addmsg(code, color="red", wait=0.05)
            else:
                addmsg(code, color="aqua", wait=0.05)
    
    addmsg("\n\n-编译完成!", color="aqua")
    addmsg("-未知错误: 用户 Tu Hengyu 密码信息已过期,需要验证", color="red")
    addmsg("-等待子进程密码输入...")
    apikey_input = input("-请输入密码（chatGPT密钥）:")
    apikey = apikey_input
    addmsg("-子进程结束码:" + str(random.randint(111,999)))
    addmsg("-成功连接到全球网络!")

def spring12():
    #---/-----/-------
    #其他版本的春节十二响
    #print('源码： https://github.com/picasso250/spring12 ')
    #def init():
#        set_engine_number_mask(ENGINE_ALL)
#        set_fuel_level(FUEL_FULL)
#        
#        # 允许误差10秒以内
#        if unix_time() < make_unix_time(2082, 1, 28, 23, 59, 60-10):
#            return ERR_ENGIN_ENV
#        
#        return engine_check_init()  # after compile and before real run
#    
#    def main():
#        set_curve(CURVE_NATURAL)  # 自然曲线耗费燃料最少
#        for i in range(12):
#            engine_start()
#            wait_engine(ENGINE_STATE_CHANGE)
#            sleep(2000)
#            engine_stop()
#            wait_engine(ENGINE_STATE_CHANGE)
#            sleep(4000)  # 这个时长在模拟器里听起来更像心跳
#        
#        return 0
#    
#    def final():
#        engine_ensure_shutdown()
       
        c = 12
        k = 1
        print("-春节十二响启动程序（源码： https://github.com/Y1ran/Wandering-Earth--Chun-Jie-12-Bong ）")
        for i in range(1, 101):
            print("[", end="")
            sys.stdout.write("程序加载进度>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>[\b\b\b%d%%]\r" % i)
            sys.stdout.flush()
            time.sleep(0.01)
            if i % 10 == 0:
                time.sleep(1)
        print("\n")
        print("-程序加载完毕，发动机正在启动...")
        time.sleep(1)
        print("-硬件系统自检完成...")
        time.sleep(1)
        print("-撞针系统自检完成...")
        time.sleep(1)
        print("-发动机正在启动...")
        time.sleep(1)
        
        while k <= 10:
            sys.stdout.write("-行星转向发动机正在启动中..............%d/100\r" % (k * 10))
            sys.stdout.flush()
            k += 1
            time.sleep(1)
        
        while c > 0:
            time.sleep(0.005)
            print("\033[1;42;37m" + " " * 80 + "\033[0m")
            time.sleep(0.1)
            print("\033[1;41;37m" + " " * 80 + "\033[0m")
            c = c - 1
            time.sleep(0.01)
            print("\033c", end="")
        print("\033[1;41;37m" + " " * 80 + "\033[0m")
        a = 12
        while a >= 1:
            print("%*s%s%*s" % (52, "", "Biu!!!\n", 0, ""))
            a -= 1
            time.sleep(0.1)
        j = 12
        print("%*s%s%*s" % (51, "", "\\ ^^ /", 0, ""))
        while j >= 1:
            print("%*s%s%*s" % (51, "", "| ^^ |", 0, ""))
            j -= 1
            time.sleep(0.1)
        print("%*s%s%*s" % (51, "", "/----\\", 0, ""))
        print("%*s%s%*s" % (49, "", " / \\  / \\ ", 0, ""))
        time.sleep(0.1)
        print("%*s%s%*s" % (48, "", "| -------- | ", 0, ""))
        time.sleep(0.1)
        print("%*s%s%*s" % (45, "", "/| ------------- |\\ ", 0, ""))
        time.sleep(0.1)
        print("%*s%s%*s" % (43, "", "__________________", 0, ""))
        time.sleep(1)
        d = 12
        while d > 0:
            print("\033[1;42;37m" + " " * 80 + "\033[0m")
            time.sleep(0.1)
            print("\033[1;41;37m" + " " * 80 + "\033[0m")
            d = d - 1
            time.sleep(0.01)
#---/-----/-------

def get_data(content):
    r = str(round(time.time() * 1000))
    salt = r + str(random.randint(0, 9))

    data = "fanyideskweb" + content + salt + "Tbh5E8=q6U3EXe+&L[4c@"
    sign = hashlib.md5()

    sign.update(data.encode("utf-8"))

    sign = sign.hexdigest()
    # print(len(sign))
    # print(sign)
    return content, salt, sign


def send_request(content, salt, sign):
    url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'

    headers = {
        'Cookie': 'OUTFOX_SEARCH_USER_ID=-1927650476@223.97.13.65;',
        'Host': 'fanyi.youdao.com',
        'Origin': 'http://fanyi.youdao.com',
        'Referer': 'http://fanyi.youdao.com/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.146 Safari/537.36',
    }

    data = {
        'i': str(content),
        'from': 'AUTO',
        'to': 'AUTO',
        'smartresult': 'dict',
        'client': 'fanyideskweb',
        'salt': str(salt),
        'sign': str(sign),
        # 'lts': '1612879546052',
        # 'bv': '6a1ac4a5cc37a3de2c535a36eda9e149',
        # 'doctype': 'json',
        'version': '2.1',
        'keyfrom': 'fanyi.web',
        'action': 'FY_BY_REALTlME',
    }

    res = requests.post(url=url, headers=headers, data=data).json()

    return res['translateResult'][0][0]['tgt']
    #print('翻译前：', res['translateResult'][0][0]['src'])

def is_english(word):
    for char in word:
        if not ('a' <= char <= 'z' or 'A' <= char <= 'Z'):
            return False
    return True

def letters(n):
        """
            Returns:
                ret:random six letter
        """
        ret = ""
        for i in range(n):
            letter = chr(random.randint(97, 122))  # 取小写字母
            Letter = chr(random.randint(65, 90))  # 取大写字母
            s = str(random.choice([letter, Letter]))
            ret += s
        return "/550W/" + str(ret) + ".java"

def command(resultText):
    global mode
    if '' == resultText or ' ' == resultText or '\n' == resultText:
        #等于空格直接执行
        result = resultText
    else:
        if is_english(resultText) == True:
            try:
                content, salt, sign = get_data(resultText)
                result = send_request(content, salt, sign)
            except Exception:
                print('文本异常！请尝试输入中文问题。')
                sys.exit()
        else:
            result = resultText
        
        if "重启系统" in result:
            print("-重启系统中…")
            launcher()
        else:
            if "切换在线版" in result:
                print("-服务器连接失败，正在重启根服务器…")
                servicepassword()
                print("服务器连接成功，正在切换为550W量子计算机 For Python 在线版！")
                mode = 1
                launcher()
            else:
                if "切换离线版" in result:
                    print("正在切换为550W量子计算机 For Python 离线版！")
                    mode = 0
                    launcher()
                else:
                    if '退出系统' in result:
                        sys.exit()
                    else:
                        #json解析
                        for item in keyworddata:
                            if item["keyword"] in result:
                                print('-' + item["text"])
                                break
                        else:
                            print("-550W离线版无法解析您的指令，可以切换在线版再提这个问题。")

                                        
def command1(result):
    global mode
    if "切换在线版" in result:
       print("-服务器连接失败，正在重启根服务器…")
       servicepassword()
       print("服务器重启成功，正在切换为550W量子计算机 For Python 在线版！")
       mode = 1
       launcher()
    else:
           if "切换离线版" in result:
               print("正在切换为550W量子计算机 For Python 离线版！")
               mode = 0
               launcher()
           else:
               if "重启系统" in result:
                    print("-重启系统中…")
                    launcher()
               else:
                    if '退出系统' in result:
                    	sys.exit()
                    else:
                       if '春节十二响' in result:
                           spring12()
                       else:
                           global gpturl
                           data = {
                   			'msg':result
                		   }
                           data550W = {
                   			'msg':'你现在是电影《流浪地球2》中的550W量子计算机（MOSS），你需要模仿550W所说的话来回答我的问题，如：我问：“你好，550W”这样类似的问题，你应该回答:“550W听起来不像个名字，但把它翻过来，叫MOSS，直译为小苔藓，是不是亲切了一些？”明白请回复明白'
                		   }
                           #初始化chatgpt模型
                           response550W = requests.get(gpturl, params=data550W)
                           text2 = json.loads(response550W.text)
                           if text2['code'] == 200:
                                   if '明白' in text2['answer']:
                                   	print('模型初始化成功！')
                                   	response = requests.get(gpturl, params=data)
                                   	text1 = json.loads(response.text)
                                   	if text1['code'] == 200:
                                   		print(text1['answer'])
                                   	else:
                                   	    print('请求失败！')
                                   else:
                                    	print('模型初始化失败！')
                           else:
                                   print('模型初始化失败！')
                               
def result():
    result_input = input("#等待指令\n")
    if mode == 0:
        command(result_input)
    else:
        command1(result_input)
    result()

def launcher():
    if mode == 0:
        print("#欢迎使用550W量子计算机 For Python 离线版！By caofangkuai-studio.")
    else:
        print("#欢迎使用550W量子计算机 For Python 在线版！By caofangkuai-studio.")

    print("-正在生成底层操作系统…")
    for i in tqdm(range(100),desc='生成进度',colour="green"):
        time.sleep(random.randint(1,10) / 60)

    print("\n-底层操作系统生成成功！正在覆写系统…")
    for i in tqdm(range(100),desc='覆写进度',colour="green"):
        print(letters(random.randint(1,6)))
        time.sleep(random.randint(1,3) / 100)
    
    print("-覆写系统成功，启动中…")
    time.sleep(0.5)
    print("\n")
    #550W logo
    print("_____ _____\n_____          __\n| ____| ____|/ _ \ \        / /\n| |__ | |__ | | | \ \  /\  / / \n|___ \|___ \| | | |\ \/  \/ /  \n ___) |___) | |_| | \  /\  /   \n|____/|____/ \___/   \/  \/    \n")
    print('注：550W离线版输入英文问题需要联网进行翻译，无网络请输入中文问题！\n')
    result()

if __name__ == "__main__":
    launcher()