import asyncio

async def greet(name):
    print("Hello, " + name)
    await asyncio.sleep(2)
    print("Goodbye, " + name)

async def main():
    task1 = asyncio.create_task(greet("liu"))
    task2 = asyncio.create_task(greet("yao"))

    await task1
    await task2


if __name__ == "__main__":
    asyncio.run(main())