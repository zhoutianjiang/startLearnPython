# 环境
- xubuntu 16.04
- anaconda
- pycharm
- python 3.6
- https://www.cnblogs.com/jokerbj/p/7460260.html
- http://www.dabeaz.com/python/UnderstandingGIL.pdf

# 多线程 vs 多进程
- 程序：一堆代码以文本形式存入一个文档
- 进程：程序运行的一个状态
    - 包含地址空间、内存、数据栈等
    - 每个进程由自己完全独立的运行环境，多进程共享数据是一个问题
- 线程
    - 一个进程的独立运行片段，一个进程可以有多个线程
    - 轻量化的进程
    - 一个进程的多个线程间共享数据和上下文运行环境
    - 共享互斥问题
- 全局解释器锁（GIL）
    - Python代码的执行是由python虚拟机进行控制
    - 在主循环中只能有一个控制线程在执行
    
- Python包
    - thread：有问题，不好用，python3改成了_thread
    - threading：同行的包
    - 案例 01.py 顺序执行，耗时比较长
    - 案例 02.py 改用多线程，缩短总时间，使用_thread
    - 案例 03.py 多线程，传参数
    
- threading的使用
    - 直接利用threading.Thread()生成Thread实例
        1. t = threading.Thread(target=xxx, args=(xxx,))
        2. t.start()：启动多线程
        3. t.join()：等待多线程执行完成
        4. 案例 04.py
        5. 案例 05.py：加入join后跟案例04.py比较异同
        - 守护线程-daemon
            - 如果在程序中将子线程设置成守护线程，则子线程会在主线程结束的时候自动退出
            - 一般认为，守护线程不重要或者不允许离开主线程独立运行
            - 守护线程案例能否有效跟环境相关
            - 案例06.py非守护线程
            - 案例07.py守护线程
        - 线程常用属性
            - threading.currentThread：返回当前线程变量
            - threading.enumerate：返回一个包含正在运行的线程的list，正在运行的线程指的是线程启动后，结束前
            - threading.activeCount：返回正在运行的线程的数量，效果跟len(threading.enumerate)相同
            - threading.setName：给线程设置名字
            - threading.getName：得到线程的名字
            - 案例 08.py
        - 直接继承自threading.Thread
            - 直接继承Thread
            - 重写run函数
            - 类实例可以直接运行
            - 案例 09.py
            - 案例 10.py。工业风案例
- 共享变量
    - 共享变量：当多个线程同时访问一个变量的时候，会产生共享变量的问题
    - 案例 11.py
    - 解决变量：锁，信号灯
    - 锁（Lock）：
        - 是一个标志，表示一个线程在占用一些资源
        - 使用方法
            - 上锁
            - 使用共享资源，放心的用
            - 取消锁，释放锁
        - 案例 12.py 
        - 锁谁：哪个资源需要多个线程共享，锁哪个
        - 理解锁：锁其实不是锁住谁，而是一个令牌
    - 线程安全问题：
        - 如果一个资源/变量，他对于多线程来讲，不用加锁也不会引起任何问题，则称为线程安全
        - 线程不安全变量类型：list，set，dict
        - 线程安全变量类型：queue
    - 生产者消费者问题
        - 一个模型，可以用来搭建消息队列
        - queue是一个用来存放变量的数据结构，特点是先进先出，内部元素排队，可以理解成一个特殊的list
        - 案例 13.py
    - 死锁问题，案例 14.py
    - 锁的等待时间问题，  案例 15.py
    - threading.Semaphore 
        - 允许一个资源最多有几个多线程同时使用
        - 案例 16.py
    - threading.Timer
        - 案例 17.py
        - Timer是利用多线程，在指定时间后启动一个功能
        
    - 可重入锁threading.Rlock()
        - 一个锁，可以被一个线程多次使用
        - 主要解决递归调用的时候，需要申请锁的情况
        - 案例 18.py
