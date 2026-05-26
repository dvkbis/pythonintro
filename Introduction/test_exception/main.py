from test import test_exception

if __name__ == '__main__':
    try:
        test_exception()
    except Exception as e:
        print(f"{e}")