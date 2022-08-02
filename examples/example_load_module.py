from dynamic_plugins import get_extensions

def main():
    functions = get_extensions("demo-", sub_package="setup",symbols="hello_world")

    for fn in functions:
        fn()

if __name__ == '__main__':
    main()
