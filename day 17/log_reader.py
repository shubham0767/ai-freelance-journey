print("=" * 45)
print("Log File Reader")
print("=" * 45)


def read_logs(filename):
    try:
        with open (filename,"r")as file:
            for line in file:
                yield line.strip()

    except FileNotFoundError:
        print("Error:File not found")

for log in read_logs("logs.txt"):
    print(log)