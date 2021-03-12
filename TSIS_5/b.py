import os

# print(os.getcwd())
# content = os.listdir('C:\\Users\\kanat\\Desktop\\')
# for i in content:
# 	print(i)


f = open('file2.txt', 'r', encoding = "utf-8");
data = f.read()

print(data)

'''
os.listdir(path) - list of files in cwd
os.getcwd() - current path


'''