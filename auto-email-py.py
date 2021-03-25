from email.mime.text import MIMEText
from email.header import Header
from smtplib import SMTP_SSL
import requests
import json
import argparse





#sender_qq为发件人的qq号码
sender_qq = ''
#pwd为qq邮箱的授权码
pwd = ''
#收件人邮箱receiver
receiver='' 
mail_content = ''
#邮件标题
mail_title = ''

def send_mail(sender_qq='',pwd='',\
    receiver='',mail_title='',mail_content=''):
    content = get_content()
    mail_content = content['content']
    mail_title = content['origin']
    # qq邮箱smtp服务器
    host_server = 'smtp.qq.com'
    sender_qq_mail = sender_qq+'@qq.com'

    #ssl登录
    smtp = SMTP_SSL(host_server)
    #set_debuglevel()是用来调试的。参数值为1表示开启调试模式，参数值为0关闭调试模式
    smtp.set_debuglevel(1)
    smtp.ehlo(host_server)
    smtp.login(sender_qq, pwd)

    msg = MIMEText(mail_content, "plain", 'utf-8')
    msg["Subject"] = Header(mail_title, 'utf-8')
    msg["From"] = sender_qq_mail
    msg["To"] = receiver
    smtp.sendmail(sender_qq_mail, receiver, msg.as_string())
    smtp.quit()

def get_content():
    url="https://v1.jinrishici.com/all.json"

    r = requests.get(url)

    result = json.loads(r.content)

    return result    
    
def rang_send_email(count):
    for i in range(count):
     send_mail(sender_qq=sender_qq,pwd=pwd,\
     receiver=receiver,mail_title=mail_title,\
     mail_content=mail_content)


parser = argparse.ArgumentParser()
parser.description='please enter two parameters a and b ...'
parser.add_argument("-a", "--inputA", help="this is parameter a", dest="argA", type=str)
parser.add_argument("-b", "--inputB", help="this is parameter b", dest="argB", type=str)
parser.add_argument("-c", "--inputC", help="this is parameter c", dest="argC", type=str)
args = parser.parse_args()
sender_qq = args.argA
pwd = args.argB
receiver = args.argC

rang_send_email(1)
