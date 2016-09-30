import os
import shutil
if __name__ == '__main__':
    print(os.getcwd())
    os.chdir(os.path.join(os.getcwd(),'message'))
    print(os.getcwd())
    print(os.listdir(os.getcwd()))
    loquequierocrear = os.path.join(os.getcwd(),'pepe')
    if not os.path.exists(loquequierocrear):
         os.mkdir(loquequierocrear)

    for filename in os.listdir(os.getcwd()):
        if not filename == 'pepe':
            shutil.copy(os.path.join(os.getcwd(), filename), os.path.join(loquequierocrear,filename))
