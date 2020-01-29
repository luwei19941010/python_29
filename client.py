#-*-coding:utf-8-*-
# Author:Lu Wei

import os,socket,struct,json
sk=socket.socket(type=socket.SOCK_STREAM)
ip_port=('127.0.0.1',9000)
sk.connect(ip_port)

def login():
    username=input('username:')
    password=input('password:')
    dic_info={'username':username,'password':password}
    dic_info_str=json.dumps(dic_info)
    size(dic_info_str)
    sk.send(dic_info_str.encode('utf-8'))
    pack_size=sk.recv(4)
    send_size=struct.unpack('i',pack_size)[0]
    res=sk.recv(send_size).decode('utf-8')
    login_res=json.loads(res)
    return login_res['login']

def size(s):
    size = struct.pack('i', len(s))
    sk.send(size)

class func:
    def download(self):
        print('down')
        pass
    def update(self):
        path=input('file path:')
        file_name=os.path.basename(path)
        size(file_name)
        sk.send(file_name.encode('utf-8'))
        with open(path,mode='rb') as f:
            data=f.read()
            sk.send(data)

if __name__=='__main__':
    while True:
        login_status=login()
        if login_status:
            print('login ok')
            inp=input('input download or update:')
            size(inp)
            sk.send(inp.encode('utf-8'))
            obj=func()
            getattr(obj,inp)()

        else:
            print('login fail')
