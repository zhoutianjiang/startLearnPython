import multiprocessing
from time import sleep, ctime

# 设置哨兵问题
def consumer(input_q):
    print("Into consumer:", ctime())
    while True:
        # 处理项
        item = input_q.get()
        if item is None:
            break
        print("pull", item, "out of q")
    print("Out of consumer:", ctime())  #此句执行完成

def producer(sequence, output_q):
    print("Into producer:", ctime())
    for item in sequence:
        output_q.put(item)
        print("put", item, "into q")
    print("Out of producer:", ctime())


if __name__ == '__main__':
    q = multiprocessing.Queue()
    # 运行消费者进程
    cons_p = multiprocessing.Process(target=consumer, args=(q,))
    cons_p.start()

    sequence = [1,2,3,4]
    producer(sequence, q)

    q.put(None)
    cons_p.join()
