import sys
import os
from PIL import Image

image_file = sys.argv[1]
new_file = sys.argv[2]
cd
if __name__ == '__main__':
    # os.wal extract all the directories and files also files and directories in the directories
    for dirpath, dirnames, filenames in os.walk(f'./{image_file}'):
        print('Current path :', dirpath)
        print('Directories: ', dirnames)
        print('Files: ', filenames)
        print('\n\n')
        #we check wheather saving location is available or not
        if os.path.isdir(f'./{new_file}')!= True:
            os.mkdir(f'./{new_file}')

        else:
            pass
        # we loop in the files variable and create paths of the files and save
        for image_name in filenames:
            image = Image.open(f'./{image_file}/{image_name}')
            # below splitext function split file type so we can replace .jpg with .png
            name = os.path.splitext(f'./{new_file}/{image_name}')
            print(name[0])
            image.save(f'{name[0]}.png')
