import sys


def main():
    while True:
        sys.stdout.write("$ ")
        line = input().split()
        if line[0] == "exit":
            exit(int(line[1]))
        elif line[0] == "echo":
            if len(line) == 0:
                print()
            else:
                print(" ".join(line[1:]))
        else:
            print(f"{line[0]}: not found")


if __name__ == "__main__":
    main()
