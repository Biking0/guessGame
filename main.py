
#聚享游疯狂28竞猜，自动投注
# 2018/09/21 15:17 
#运行前设置好账号密码，风险控制即运行后至少剩多少豆子。需要自己输入验证码进行登录，之后可以完全自动运行


from selenium import webdriver
import time
import datetime
import random
import re

#控制盈利频率，下注数小于6，停止下注
get=6

#控制下注倍率
beishu=2

zhu1=1
zhu2=2

#控制损失
zong=493500

buytime="2018-08-28 21:45:45"
browser = webdriver.Chrome("D:\softInstall\chromedriver.exe")
ti=0.001

#上5期数据存放
span=[]

browser.get("http://www.juxiangyou.com/login/index")

# handles = browser.window_handles


#设置用户名、密码
browser.find_element_by_id("account").send_keys("username")
browser.find_element_by_id("password").send_keys("password")

# code=input("输入验证码：\n")
# browser.find_element_by_id("code").send_keys(code)

time.sleep(20)


#拿到上期5个
def data():

    browser.get("http://www.juxiangyou.com/fun/play/crazy28/index")
    time.sleep(7)

    #出现偏离值，等待4分钟
    # try:
    #     a=int(browser.find_element_by_xpath("html/body/div[3]/div[1]/div[2]/div[1]/div[3]/div[2]/table/tbody/tr[6]/td[3]/span[2]").text)
    # except:
    #     print("偏离检测数据出错")
    #     return
    # if a<9 or a>18: 
    #     ran=random.randint(30,120)
    #     print("偏离等待,秒",ran)
        
    #     time.sleep(ran)
    #     return


    #随机边界值，6,11
    for i in range(random.randint(6,8),random.randint(8,11)):
        # span.append(browser.find_element_by_xpath("html/body/div[3]/div[1]/div[2]/div[1]/div[3]/div[2]/table/tbody/tr["+str(i)+"]/td[3]/span[2]").text)
        path="html/body/div[3]/div[1]/div[2]/div[1]/div[3]/div[2]/table/tbody/tr["+str(i)+"]/td[3]/span[2]"
        # print(path)
        try:
            span.append(browser.find_element_by_xpath(path).text)
        except:
            print("旧数据获取错误")
            continue

    # for i in range(len(span)):
    #     print(span[i],type(span[i]))
    
flag=False

#投注页面
def buy(qihao):
    #出现偏离，停止下注
    if len(span)==0: return


    global flag
    #下注页面
    browser.get("http://www.juxiangyou.com/fun/play/crazy28/jctz?id="+qihao)

    time.sleep(2)

    #牺牲一个做随机值，模型优化,现在没用
    # suiji=random.randint(6,21)
    a=[6,7,8,19,20,21]
    suiji=a[random.randint(0,5)]

    #大小区间随机值
    b=[0,1,2,3,4,5,6]
    c=b[random.randint(0,6)]

    if c>4:
       
        for i in range(len(a)):
            path="html/body/div[3]/div[1]/div[2]/div[1]/div[3]/div[2]/div[2]/div[1]/div[2]/ul["+str(a[i]+1)+"]/li[5]/input"
            browser.find_element_by_xpath(path).send_keys(zhu1)
        
        try:
            browser.find_element_by_xpath("html/body/div[3]/div[1]/div[2]/div[1]/div[3]/div[2]/div[2]/div[2]/div[2]/a").click()
        except :
            print("确认报错")
        span.clear()
        return 

    else:
        count=0
        flag=True
        #高频下注,大于55,9-19,10-18
        for i in range(10,18):
            
            for j in range(len(span)):
                if i == int(span[j]):               
                    flag=True                
                    break
            
            if flag is True:
                # print(78)
                flag=False
                continue
            
            print(i)
            if i==suiji: continue
    
            
            path="html/body/div[3]/div[1]/div[2]/div[1]/div[3]/div[2]/div[2]/div[1]/div[2]/ul["+str(i+1)+"]/li[5]/input"
            # print("path---:",path)

            #分段加倍,9,10,17,18
            zhu=1
            if i==11 or i==17:
                zhu=zhu2
            # else:
            #     zhu=zhu2
            #     print("注加倍")

            browser.find_element_by_xpath(path).send_keys(zhu*beishu)
            count+=1

            # global zhu
            # if count>8:
            #     zhu=zhu2
      
        #控制频率
        if count<get: 
            span.clear()
            return

    
    
    # browser.find_element_by_xpath("html/body/div[3]/div[1]/div[2]/div[1]/div[3]/div[2]/div[2]/div[1]/div[2]/ul["+str(suiji+1)+"]/li[5]/input").send_keys(1)
    # print("随机值:",suiji)


    suiji_min=random.randint(5,9)
    suiji_max=random.randint(18,21)

    print("suiji_min",suiji_min)
    print("suiji_max",suiji_max)

    browser.find_element_by_xpath("html/body/div[3]/div[1]/div[2]/div[1]/div[3]/div[2]/div[2]/div[1]/div[2]/ul["+str(suiji_min+1)+"]/li[5]/input").send_keys(1)
    browser.find_element_by_xpath("html/body/div[3]/div[1]/div[2]/div[1]/div[3]/div[2]/div[2]/div[1]/div[2]/ul["+str(suiji_max+1)+"]/li[5]/input").send_keys(1)

    time.sleep(7)
    #确认下注

    try:
        browser.find_element_by_xpath("html/body/div[3]/div[1]/div[2]/div[1]/div[3]/div[2]/div[2]/div[2]/div[2]/a").click()
    except :
        print("确认报错")
    span.clear()
while(True):

    print("加载结果页面")
    #结果页面
    browser.get("http://www.juxiangyou.com/fun/play/crazy28/index")
    
    time.sleep(10)

    #豆数量
    dou=browser.find_element_by_xpath("html/body/div[3]/div[1]/div[3]/div[1]/div[2]/p[1]/span").text
    
    dou_str=re.findall(r"\d+",str(dou))

    dou_int=int(dou_str[0]+dou_str[1])

    print("豆子总量：",dou_int)
    if dou_int<zong:
        break

    try:
        #获取倒计时
        open=browser.find_element_by_xpath("html/body/div[3]/div[1]/div[2]/div[1]/div[3]/div[1]/div[1]/div[1]/div[2]/p[1]/span[2]").text
    except:
        print("倒计时获取出错")

    # open=browser.find_element_by_class_name("clr-red J_carry28Time second").text
    if open==" "  or open=='': continue
    if int(open)<70 and int(open)>30:
        # a=input("输入任意字符开始下注：")
        print("开始下注")
        data()
        path="html/body/div[3]/div[1]/div[2]/div[1]/div[3]/div[2]/table/tbody/tr[5]/td[1]"
        qihao=browser.find_element_by_xpath(path).text
        buy(qihao)
        print("考虑下注，等待下次下注,18秒")
        time.sleep(20)
    

    
    
    

    
    

        




   


