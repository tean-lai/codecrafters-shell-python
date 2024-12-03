import sys


def main():
    while True:
        sys.stdout.write("$ ")
        line = input().split()
        if line[0] == "exit":
            exit(int(line[1]))
        else:
            print(f"{line[0]}: not found")


if __name__ == "__main__":
    main()
