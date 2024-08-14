import time


def washing1():
    time.sleep(3)  # 第一台洗衣机,
    print('washer1 finished')  # 洗完了


def washing2():
    time.sleep(8)
    print('washer2 finished')


def washing3():
    time.sleep(5)
    print('washer3 finished')


if __name__ == '__main__':
    start_time = time.time()
    washing1()
    washing2()
    washing3()
    end_time = time.time()
    print('总共耗时：{}'.format(end_time-start_time))