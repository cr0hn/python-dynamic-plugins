from dynamic_plugins import get_modules

def main():
    functions = get_modules("demo-", entrypoint_module="setup", entrypoint_function="hello_world")

    for fn in functions:
        fn()

if __name__ == '__main__':
    main()
