import os

if not os.path.exists('OS'):
    os.mkdir('OS')

# 2. Create a file inside the folder
file_path = os.path.join('OS', "sample.txt")
with open(file_path, "w+") as f:
    f.write("Hello, this is a test file!")
    f.seek(0)
    print(f.read())
print(f"📄 File '{file_path}' created.")