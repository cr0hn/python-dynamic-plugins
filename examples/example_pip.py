from dynamic_plugins import list_installed_packages

def main():

    for package_name, package_version in list_installed_packages().items():
        print(f"{package_name} {package_version}")

if __name__ == '__main__':
    main()
