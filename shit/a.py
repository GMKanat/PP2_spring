import os
class Work_with_files:
    def safe_delete(self,target):
        if os.path.isfile(target):
            os.remove(target)
    def safe_rename(self,target):
        if os.path.isfile(target):
            second_name = input()
            os.rename(target,second_name)
    def add_content(self,target):
        if os.path.isfile(target):
            append_str = input()
            with open(target,'a') as file:
                file.write(append_str)
    def parent(self,target):
        if os.path.isfile(target):
            NEW_ULR = os.path.abspath(os.path.join(target,os.pardir))
            return NEW_ULR
class Work_with_directories:
    def safe_rename(self,target):
        if os.path.isdir(target):
            first_name,second_name = map(str,input().split())
            os.rename(first_name,second_name)
    def count_files(self,target):
        a = [file for file in target if os.path.isfile(file)]
        print(f"Number of files: {len(a)}")
    def count_dirs(self,target):
        a = [dirr for dirr in target if os.path.isdir(dirr)]
        print(f"Number of dir: {len(a)}")
    def list_content(self,target):
        for content in os.listdir(target):
            content_name = os.path.join(target,content)
            if os.path.isdir(content_name):
                print(f"DIR -> {content_name}")
            if os.path.isfile(content_name):
                print(f"FILE -> {content_name}")
    def add_file(self,target):
        tst = input()
        with open(os.path.join(target,tst),'x') as file:
            file.write('')
    def add_directory(self,target):
        n_dir = input()
        if os.path.isdir(n_dir):
            os.mkdir(n_dir)

BASE_ULR = 'C:\\Users\\Арман\\Documents\\git_tutorial\\work\\os'
for target in os.listdir(BASE_ULR):
    files = Work_with_files()
    dirs = Work_with_directories()
    target_name = os.path.join(BASE_ULR,target)
    if os.path.isfile(target_name):
        func = input()
        if func == 'del':
            files.safe_delete(target_name)
        if func == 'rname':
            files.safe_rename(target_name)
        if func == 'a':
            files.add_content(target_name)
        if func == 'par':
            files.add_content(target_name)