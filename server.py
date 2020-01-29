#-*-coding:utf-8-*-
# Author:Lu Wei

import socket,hashlib,os,struct,json

sk=socket.socket(type=socket.SOCK_STREAM)
ip_port=('127.0.0.1',9000)
sk.bind(ip_port)
sk.listen()

def login():
    pack_len=conn.recv(4)
    pack_size=struct.unpack('i',pack_len)[0]
    msg=conn.recv(pack_size).decode('utf-8')
    msg_dic=json.loads(msg)
    with open('user_info',mode='r',encoding='utf-8') as f :
        user,psd=f.read().split('|')
        if user==msg_dic['username'] and psd==msg_dic['password']:
            dic_info = {'login':True }
            dic_info_str=json.dumps(dic_info)
            size(dic_info_str)
            conn.send(dic_info_str.encode('utf-8'))
            return True
        else:
            dic_info = {'login': False}
            dic_info_str = json.dumps(dic_info)
            size(dic_info_str)
            conn.send(dic_info_str.encode('utf-8'))
            return False

def size(s):
    size = struct.pack('i', len(s))
    conn.send(size)

class func:
    def download(self):
        print('down')
        pass
    def update(self):
        pack_len = conn.recv(4)
        pack_size = struct.unpack('i', pack_len)[0]
        file_name = conn.recv(pack_size).decode('utf-8')
        with open(file_name,mode='wb') as f :
            data=conn.recv(1024)
            f.write(data)

if __name__=='__main__':
    while True:
        conn,addr=sk.accept()
        login_res=login()
        if login_res:
            pack_len = conn.recv(4)
            pack_size = struct.unpack('i', pack_len)[0]
            user_choice = conn.recv(pack_size).decode('utf-8')
            obj=func()
            getattr(obj,user_choice)()

            # if
            # while True:
            #     conn.close()
    sk.close()
