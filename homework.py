#-*-coding:utf-8-*-
# Author:Lu Wei

# 1.文件的上传、下载
# 2.结合用户认证
#
# 要求：
# 1.tcp协议粘包的问题，使用struct模块解决粘包问题
# 2.传递的所有的信息都尽量是json格式
# 3.再server端用上反射
import os

path = input('file path:')
file_name = os.path.basename(path)
print(file_name)