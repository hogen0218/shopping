
import multiprocessing
import os

base_dir = os.path.dirname(os.path.abspath(__file__))
# unix:file_path 使用socket方式
bind = "127.0.0.1:8008"
#socket_file = os.path.join(base_dir,'mysocket','mysock.sock')
#bind = "unix:{}".format(socket_file)
# 2-4 x $(NUM_CORES) range
workers = multiprocessing.cpu_count() * 2 + 1
#worker_class= "gevent"
# port = 8002
backlog = 2048  # 就是设置允许挂起的连接数的最大值
# timeout默认值：30
# reload 默认值：False 重载 更改代码的时候重启workers， 只建议在开发过程中开启。
reload = False
# daemon以守护进程形式来运行Gunicorn进程。默认值：False
daemon = False
# accesslog 设置访问日志存放的地方
# 默认值：None
# accesslog = '/opt/logs/modu_movie/access.log'
accesslog = os.path.join(base_dir, 'log', 'gunicorn', 'access.log')
# errorlog 设置错误日志的存放地址
# errorlog = '/opt/logs/modu_movie/error.log'
errorlog = os.path.join(base_dir, 'log', 'gunicorn', 'error.log')



#   在terminal里输入  gunicorn -c gunicorn.conf.py movies.wsgi