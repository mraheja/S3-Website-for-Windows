import fileinput


holder = '<ENTER NAME>'

print("No uppercase characters!")
name = input("Enter name for your project! ")

with fileinput.FileInput("sync.bat", inplace=True) as file:
    for line in file:
        print(line.replace(holder, name), end='')

with fileinput.FileInput("open.bat", inplace=True) as file:
    for line in file:
        print(line.replace(holder, name), end='')
		
with fileinput.FileInput("init.bat", inplace=True) as file:
    for line in file:
        print(line.replace(holder, name), end='')
		
with fileinput.FileInput("bucket.json", inplace=True) as file:
    for line in file:
        print(line.replace(holder, name), end='')