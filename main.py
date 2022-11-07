from pathlib import Path

data_dir = Path("Dummy-Repo") / "README.md"

# check file existence
print(f"Is submodule readme available? {data_dir.exists()}")

# print the content to cmd
print("Content: ")
with open(data_dir) as input_file:
    print(input_file.read())