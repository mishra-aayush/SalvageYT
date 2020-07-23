from __future__ import unicode_literals
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from webdriver_manager.firefox import GeckoDriverManager
import youtube_dl
def downloader(username):
    options = Options()
    options.add_argument('-headless')
    driver = webdriver.Firefox(executable_path=GeckoDriverManager().install(),options=options)
    page_link ='https://www.youtube.com/'+username+'/videos' 
    driver.get(page_link)
    URL = driver.find_element_by_id("video-title") 
    download = URL.get_attribute("href")
    print(URL.get_attribute("aria-label"))
    choice = input("Print y to download above video or n to not\n")
    if choice=="n":
        driver.quit()
        return
    driver.quit()
    ydl_opts = {}
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([download])
def main():
    with open('usernames.txt','r') as reader:
        l= reader.readlines()
    for user in l:
        downloader(user)
if __name__=="__main__":
    main()
