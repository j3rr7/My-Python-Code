from pytube import YouTube
from pytube import Playlist
import pytube

import os

def DHRes(url,path):
    #ytb = YouTube(url)
    #ytb = ytb.get('mp4', '720p')
    #yt = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
    #ytb.download()
    YouTube(url).streams.first().download(path)

def DCustRes(url,path):
    print(yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').asc().all())
    
    
url = input("URL : ")
#yt = YouTube(url)

#================= GET PATH
#============
print("Default is current directory")
#path = os.getcwd()
path = input("PATH : ")
if not path:
    path = os.getcwd()+'\\'
else:
    path = os.getcwd()+'\\'+path+'\\'
    if not os.path.exists(path):
        os.makedirs(path)
print(path)

print("1. Custom Resolution")
print("2. Highest Resolution")
print("3. Lowest Resolution")
ress = input(">>> ")

if ress == 1:
    print("1")
elif ress == 2:
    DHRes(url,path)
elif ress == 3:
    print("2")
else:
    exit()
    
    
    
    
    
    
    
#print("Get all possible data")
#print(yt.streams.all())
#
#print("Filter by Resolution Ascending")
#print(yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').asc().all())
#
#print("Get Best Possible Resolution")
#print(yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first())
#print(yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').asc().last())
#
#print("Get Lowest Possible Resolution")
#print(yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().last())
#print(yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').asc().first())

#print("1. 1080p \n2. 720p\n3. 480p\n4. 360p\n5. 240p\n6. ")
#
#quality = input(">>> ")

#====================== Get Caption
#============
#print(yt.captions.all())
#caption = yt.captions.get_by_language_code('en')
#caption.xml_captions
#print(caption.generate_srt_captions())



