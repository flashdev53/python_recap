def log_reader(path):
    with open(path, "r") as f:
        for line in f:
            yield line.strip()

for line in log_reader("system.log"):
    print(line)
