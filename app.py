import os
import platform


def main():
    user = os.environ.get('USER', 'Unknown User')
    system = platform.system()
    
    try:
        distro = platform.freedesktop_os_release().get('PRETTY_NAME', 'Linux')
    except AttributeError:
        distro = "Linux (unknown Distro)"

    cwd = os.getcwd()

    print(f"--- DevOps Python Report ---")
    print(f"User:  {user}")
    print(f"System:  {system}")
    print(f"Distribution:  {distro}")
    print(f"Current Directory: {cwd}")


if __name__ == "__main__":
    main()




