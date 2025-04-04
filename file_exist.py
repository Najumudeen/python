import os

for filename in os.listdir("/Users/zayan/Python350"):
    if filename.startswith("scribe.py"):
        print(f"found {filename}")