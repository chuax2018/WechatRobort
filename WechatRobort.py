import itchat
import requests
import socket

url = "http://www.tuling123.com/openapi/api"
key = "720b8495c39f40ac92284c5d6b3d1dd7"


def isNetOK(testserver):
    s = socket.socket()
    s.settimeout(3)
    try:
        status = s.connect_ex(testserver)
        if status == 0:
            s.close()
            return True
        else:
            return False
    except Exception as e:
        return False


def isNetChinaOK(testserver=('www.baidu.com', 443)):
    isOK = isNetOK(testserver)
    return isOK


@itchat.msg_register("Text")
def text_reply(msg):
    if msg["Text"] in ["在", "在？", "在吗？", "你好", "你好？"]:
        return "[9:00~18:00] 许工工作中...\n接下来由AI助手接管您的聊天！"
    else:
        return get_reply(msg["Text"])


def get_reply(msg):
    print(msg)
    repson = requests.post(url + "?key=" + key + "&info=" + msg).json()
    print(repson)
    return repson.get("text")


def run_wechat_robot():
    if not isNetChinaOK():
        print("Error: Net connection is invalid! Quit!")
        return

    itchat.auto_login(hotReload=True)
    #itchat.login()
    itchat.run()


run_wechat_robot()