from ctypes import *
import os
import time
import shutil


PATH = 'C:/Users/sami/Downloads'
FDEST = 'C:/Users/sami/Downloads/pdf_files'
BDEST = 'D:/PDF_LIBRARY'
BOOKS = []
so_file = 'C:/Users/sami/my_functions.so'
messagebox = CDLL(so_file)

class File_handling():
    def __init__(self, path, dest, category, name, time):
        self.path = path
        self.dest = dest
        self.category = category
        self.name = name
        self.time = time
        
    def pdf_file_handling(self):
        shutil.move(self.path, self.dest)
    
    def book_handling(self):
        shutil.move(self.path, self.dest)
        
    def logging(self):
        with open('pdf_logs.txt', 'a') as logfile:
            logfile.write(f'{self.time} - Name: {self.name} - Category: {self.category} - Final_Dest: {self.dest}\n')



while True:
    download_dir = os.listdir(path=PATH)
    for file in download_dir:
        if file.endswith('.pdf'):
            msg_str = f'[+] "{file}" -> is downloaded. Should it be copied into the library?'
            response = messagebox.messagebox(msg_str.encode('utf-8'))
            if response == 1:
                gripper = File_handling(PATH+'/'+file, BDEST+'/'+file, 'BOOK', file, str(time.ctime()))
                gripper.book_handling()
                gripper.logging()
                continue
            elif response != 1:
                reaper = File_handling(PATH+'/'+file, FDEST+'/'+file, 'PDF_FILE', file, str(time.ctime()))
                reaper.pdf_file_handling()
                reaper.logging()
                continue
    