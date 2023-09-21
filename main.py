from tkinter import filedialog
from tkinter import *
import os,shutil,glob,time
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import selenium

def get_folder_path():
    root = Tk()
    root.withdraw()
    folder_selected = filedialog.askdirectory()
    return folder_selected

def add_telegram_portable_exe_to_all_folders(parentFolder):
    print("* Copying telegram.exe to parent folders.")
    exe_path = os.path.join(os.getcwd(),'core','Telegram.exe')
    all_tele_folders = glob.glob("{}/*/".format(parentFolder))
    for folder in all_tele_folders:
        if not os.path.exists(os.path.join(folder,'Telegram.exe')):
            shutil.copy(exe_path,os.path.join(folder,'Telegram.exe'))
    return all_tele_folders

def get_all_telegrams(parent_folder_path=None):
    if not parent_folder_path:
        parent_folder_path = get_folder_path()
    all_tele_folders = glob.glob("{}/*/".format(parent_folder_path))
    return all_tele_folders
    
class BOT:

    def __init__(self,telegram_folder_path) -> None:
        self.telegram_folder_path = telegram_folder_path
        self.driver = None
    
    def load_driver(self):
        if self.driver:return
        options = Options()
        options.binary_location = os.path.join(self.telegram_folder_path,'Telegram.exe')
        # options.add_argument("user-data-dir={}".format(os.path.join(self.telegram_folder_path,'tdata')))
        # you may need some other options
        # options.add_argument("--remote-debugging-port=8888")  # this
        # options.add_argument('--no-sandbox')
        # options.add_argument('--no-default-browser-check')
        # options.add_argument('--no-first-run')
        # options.add_argument('--disable-gpu')
        # options.add_argument('--disable-extensions')
        # options.add_argument('--disable-default-apps')
        self.driver = webdriver.Chrome(options=options)

    def quit_driver(self):
        try:
            self.driver.quit()
        except Exception as e:
            pass


    def drive(self):
        self.load_driver()
        time.sleep(10)
        # self.quit_driver()
        print("here")


        while 1:pass



def main():
    # step 1
    print("* Geting Parent Folder.")
    parent_folder_path = get_folder_path()

    # step 2
    all_tele_folders = add_telegram_portable_exe_to_all_folders(parent_folder_path)

    for tele_folder in all_tele_folders:
        print("* Current folder -> ",tele_folder)
        bot = BOT(tele_folder)
        bot.drive()




if __name__ == "__main__":
    os.system('cls')

    main()
    
    print("\n... BOT JOB DONE...\n")
    while 1:pass
