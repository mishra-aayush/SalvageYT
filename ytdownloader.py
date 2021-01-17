from __future__ import unicode_literals
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from webdriver_manager.firefox import GeckoDriverManager
import youtube_dl
import json

def user_input():
    # Channel ID: to be dealt with later
    global channelid
    channelid = 1

    #Reading the JSON file
    try:
        with open('usernames.json', 'r') as openfile: 
            json_object = json.load(openfile)
    except:
        print('No channels were recenetly opened')
        json_object = {}

    # Printing the 5 or less recenetly used channels
    else:
        print('Recently viewed channels: ')
        counter = 0
        for channel in json_object.keys():
            print(channel)
            counter += 1
            if counter == 5:
                break

    # Taking user input
    print('Enter the username of the channel: ')
    channelname = input()
    input_name = {}
    input_name[channelname] = channelid
    input_name.update(json_object)

    # Writing into JSON file
    with open("usernames.json", "w") as outfile: 
        json.dump(input_name, outfile) 

    # Return channel name
    return channelname

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
    downloader(user_input())

if __name__=="__main__":
    main()
