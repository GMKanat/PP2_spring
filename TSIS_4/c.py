import os
import shutil
# with open('file2.txt', 'a') as f:
#   f.write('hello python')


# with open('file2.txt', 'w') as f:
#   f.write('hello python 2')

# with open('file3.txt', 'x') as f:
#   f.write('hello python 2')


# with open('file3.txt', 'r') as f:
#   text = f.read()

# with open('file3.txt', 'w') as f:
#   f.write(str(len(text)))

# with open('file4.txt', 'x') as f:
#   f.write('hello python 2')

# file_path = 'file4.txt'
# if os.path.exists(file_path):
#   os.remove(file_path)


# print(os.path.isfile('file2.txt'))
# print(os.path.isfile('dir1'))

# print(os.path.isdir('dir1'))
# print(os.path.isdir('file2.txt'))


# if os.path.exists('dir1'):
#   os.rmdir('dir1')

# file_path = 'file2.txt'
# if os.path.exists(file_path):
#     os.remove(file_path)

def create_dir(path):
    if not os.path.exists(path):
        os.mkdir(path)
create_dir('kana')

print(os.getcwd())
# os.chdir('kana')
# os.mkdir('kakakak')   
# print(os.listdir('.'))
os.mkdir('dir1')
os.mkdir('dir')
with open('dir1/text.txt', 'x') as f:
  f.write('hello python 2')
          
shutil.move('dir1/text.txt', 'dir')