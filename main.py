#6d9a1d57ab714bf8fc6319165714b87950af510c
def main_wrapper():
    print(f"function's name is {main_wrapper().__name__}")
    print("hello")


if __name__ == "__main__":
    main_wrapper()