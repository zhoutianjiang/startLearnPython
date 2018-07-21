# 利用time延时函数，生成两个函数
# 利用多线程调用
# 计算总运行时间
# 练习带参数的多线程并更名为thread
import time
# 导入多线程包并更名为thread
import _thread as thread

def loop1(in1):
    # ctime得到当前时间
    print("Start loop 1 at：", time.ctime())
    # 把参数打印出来
    print("我是参数 ", in1)
    # 睡眠多长时间，单位是秒
    time.sleep(4)
    print("End loop 1 at：", time.ctime())

def loop2(in1, in2):
    # ctime得到当前时间
    print("Start loop 2 at：", time.ctime())
    # 把参数in1和in2打印出来，代表使用
    print("我是参数 ", in1, "和参数 ", in2)
    # 睡眠多长时间，单位是秒
    time.sleep(2)
    print("End loop 2 at：", time.ctime())

def main():
    print("Starting at：", time.ctime())
    # 启动多线程的意思是用多线程去执行某个函数
    # 启动多线程函数为start_new_thread
    # 参数两个，一个是需要运行的函数名，第二是函数的参数作为元组使用，为空则使用空元组
    # 注意：如果函数只有一个参数，需要参数后有一个逗号
    thread.start_new_thread(loop1, ("王老大", ))
    thread.start_new_thread(loop2, ("王大鹏", "王小鹏"))
    print("All done at：", time.ctime())

if __name__ == '__main__':
    main()
    while True:
        time.sleep(1)