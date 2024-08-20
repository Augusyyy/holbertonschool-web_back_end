from time import sleep

def greet(name):
    print("Hello, " + name)
    sleep(2)  # 模拟一个耗时的操作
    print("Goodbye, " + name)


# 运行主函数
if __name__ == "__main__":
    greet("liu")
    greet("yao")