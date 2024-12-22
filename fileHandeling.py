file_path = "file.txt"
with open(file_path, "w") as file:
    file.write("Hi this is my first text file..")

with open(file_path, "r") as file:
    content = file.read()
    print(content)

with open(file_path,"a") as file:
    file.write("This is Rakib.")

with open(file_path, "r") as file:
    content = file.read()
    print(content)

with open(file_path, "r") as file:
    content = file.readlines()
    for line in content:
        print(line.strip())