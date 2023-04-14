import os
import shutil

rootdir = input('Enter path of source folder: ').replace('/', '\\')
destdir = input('Enter path of destination folder: ').replace('/', '\\')

# Ask user to choose an option for the file name.
choice_text = "Please choose an option. Type:\n1 - Keep the original name;\n2 - Replace with the parent folder's name;\n3 - Replace with the 'parent folder name'_'original name':\n"
choice = input(choice_text)

for subdir, dirs, files in os.walk(rootdir):
    for file in files:
        if file.endswith('.jpg') or file.endswith('.png'):
            src_file = os.path.join(subdir, file)
            file_extension = os.path.splitext(file)[1]
            
            # Check the user's choice for renaming the file
            if choice == '2':
                new_file_name = subdir.split(os.sep)[-1] + file_extension
            elif choice == '3':
                new_file_name = subdir.split(os.sep)[-1] + '_' + os.path.splitext(file)[0] + file_extension
            else:
                new_file_name = file
            
            dst_file = os.path.join(destdir, new_file_name)
            shutil.copy(src_file, dst_file)
