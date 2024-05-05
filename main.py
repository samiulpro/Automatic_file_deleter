import os

file_path = '/Users/samiulislamsami/Downloads'
file_list = os.listdir(file_path)
sele_file = []

for fn in file_list:
    if fn.endswith('.png'):
        sele_file.append(fn)
        print(f"(*) File added: {fn}")

sele_file_list = []

for selec in sele_file:
    fn_with_path = file_path +'/'+ selec
    sele_file_list.append(fn_with_path)

response = input("Do you want to delete these items? Y/N ?").capitalize()
if response == 'Y' or response == 'YES':
    for path in sele_file_list:
        if os.path.isfile(path):
            os.remove(path)
            print(f'[+] Succesfully Deleted: {path}')

        else:
            print(f"(-) ERROR {path} -> This file does not exist")

else:
    print('No files deleted. Exited cleanly')
    quit()
