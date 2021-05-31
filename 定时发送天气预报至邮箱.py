import smtplib,schedule
from email.mime.text import MIMEText
from email.header import Header
import requests,time
from bs4 import BeautifulSoup
account = '964939308@qq.com'
password = 'wrqejcjhwsctbaja'
receiver = input('请输入收件人的邮箱：')

def weather_spider():
    headers={'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
    url='http://www.weather.com.cn/weather/101280601.shtml'
    res=requests.get(url,headers=headers)
    res.encoding='utf-8'
    soup=BeautifulSoup(res.text,'html.parser')
    tem1= soup.find(class_='tem')
    weather1= soup.find(class_='wea')
    temp=tem1.text
    weather=weather1.text
    return temp,weather
def send_email(temp,weather):
    mailhost='smtp.qq.com'
    qqmail = smtplib.SMTP_SSL(mailhost)
    qqmail.connect(mailhost,465)
    qqmail.login(account,password)
    content= '今天的天气：'+temp+weather
    message = MIMEText(content, 'plain', 'utf-8')
    subject = '为小殷宁专属定制的天气预报'
    message['Subject'] = Header(subject, 'utf-8')
    try:
        qqmail.sendmail(account, receiver, message.as_string())
        print ('邮件发送成功')
    except:
        print ('邮件发送失败')
    qqmail.quit()

def job():
    print('开始一次任务')
    temp,weather = weather_spider()
    send_email(temp,weather)
    print('任务完成')

schedule.every().day.at("14:03").do(job)       #部署每10分钟执行一次job()函数的任务
while True:
    schedule.run_pending()
    time.sleep(1)