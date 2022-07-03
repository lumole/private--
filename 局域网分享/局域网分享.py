import http.server
import socketserver
import easygui
import os
import socket
import pyperclip

def SetUpSever(port=8000):
    handler = http.server.SimpleHTTPRequestHandler
    httpd = socketserver.TCPServer(("", port),RequestHandlerClass=handler)
    httpd.serve_forever()

def Getdir():
    dir = easygui.diropenbox("选择要分享的文件夹")
    return dir

def Setdir(dir):
    os.chdir(dir)
    print("分享目录已设定成功")

def GetHostIP(port):
    # hostname = socket.gethostname()
    # local_ip = socket.gethostbyname(hostname)
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
    finally:
        s.close()
        webip = ip + ':' + str(port)
        print("获取到本地ip:", webip)
        return webip
    # return local_ip
def clip(port):
    pyperclip.copy(GetHostIP(port))
    print("已将地址复制到剪贴板")

def main(port=8000):
    Setdir(Getdir())
    clip(port)
    SetUpSever(port)

main()