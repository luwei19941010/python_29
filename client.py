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
        dir_size=sk.recv(4)
        dir_size=struct.unpack('i',dir_size)[0]
        rec_dir=json.loads(sk.recv(dir_size).decode('utf-8'))
        for i in rec_dir:
            print(rec_dir.index(i)+1,i)
        num=int(input('download num:'))
        down_name=rec_dir[num-1]
        size(down_name)
        sk.send(down_name.encode('utf-8'))
        file_size_pack=sk.recv(4)
        file_len_pack=struct.unpack('i',file_size_pack)[0]
        sum=0
        with open(down_name,mode='wb') as f :
            while sum<file_len_pack:
                data=sk.recv(1024)
                f.write(data)
                f.flush()
                sum=sum+len(data)

    def update(self):
        path=input('file path:')
        file_name=os.path.basename(path)
        size(file_name)
        sk.send(file_name.encode('utf-8'))
        file_size=os.path.getsize(path)
        file_size_pack = struct.pack('i',file_size)
        sk.send(file_size_pack)

        with open(path,mode='rb') as f:
            while file_size>0:
                if file_size>=1024:
                    data=f.read(1024)
                    sk.send(data)
                else:
                    sk.send(f.read(file_size))
                file_size=file_size-1024

if __name__=='__main__':
    while True:
        login_status=login()
        if login_status:
            print('login ok')
            while True:
                    inp=input('input download or update:')
                    size(inp)
                    sk.send(inp.encode('utf-8'))
                    obj=func()
                    getattr(obj,inp)()

        else:
            print('login fail')
