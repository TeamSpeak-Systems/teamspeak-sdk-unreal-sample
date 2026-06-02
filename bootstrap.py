import subprocess
import sys


def main():
    print("*** git submodule update ***")
    subprocess.run(["git", "submodule", "update", "--init", "--recursive"], check=True)
    print("*** plugin bootstrap (fetch SDK) ***")
    subprocess.run([sys.executable, "bootstrap.py"], cwd="Plugins", check=True)
    print("done")


if __name__ == "__main__":
    main()
