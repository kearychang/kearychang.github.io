import os

with os.open(file="file.txt") as f:
    print(os.fstat(f))