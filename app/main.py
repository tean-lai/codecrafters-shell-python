import sys


def main():
    builtins = ["echo", "exit", "type"]
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
        elif line[0] == "type" and line[1] in builtins:
            print(f"{line[1]} is a shell builtin")
        else:
            print(f"{line[0]}: not found")


if __name__ == "__main__":
    main()
