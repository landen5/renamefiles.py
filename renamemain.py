import os

print('Please enter the name of the folder')
folder = input()
print('Please enter the new name of the file')
name = input()
print('Please enter the extension, i.e., .jpg, .png, etc.')
extension = input()

path = 'D:/' + str(folder)
files = os.listdir(path)

i = 1

for file in files:
    os.rename(os.path.join(path, file), os.path.join(path, str(name)+str(i)+str(extension)))
    i = i+1
