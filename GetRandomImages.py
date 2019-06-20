import urllib.request as req
import sys, time, random, datetime, os, threading, shutil

def DownloadC(width,height,index):
    try:
        print('\r'+'Loading...\n',end='',flush=True)
        for i in range(int(index)):
            url = r"https://picsum.photos/xxx/yyy"
            data = url.replace('xxx',width)
            data = data.replace('yyy',height)
            #print(data)
            if not os.path.exists('images'):
                os.makedirs('images')
            imgfilename = 'images/'+datetime.datetime.today().strftime('%d%m%Y-%H%M%S%f%p') + 'custom.jpg'
            req.urlretrieve(data+'.jpg',imgfilename)
            req.urlcleanup()
        print('\r'+'\nCompleted\n',end='',flush=True)
    except KeyboardInterrupt:
        print("\n[0] Force Exit Command Executed\n")
        req.urlcleanup()
        exit()
    except Exception as e:
        print("Unknown Error Exiting...")
        time.sleep(2)
        exit()

def Download(index):
    try:
        print('\r'+'Loading...\n',end='',flush=True)
        for i in range(int(index)):
            url = r"https://picsum.photos/xxx/yyy"
            size_x = [640, 800, 800, 960, 1024, 1024, 1152, 1280, 1280, 1280, 1366, 1400, 1440, 1440, 1600, 1600, 1680, 1856, 1920, 1920, 1920, 2048, 2560, 2560, 3840]
            size_y = [480, 576, 600, 648, 720, 720, 768, 768, 800, 900, 900, 960, 1050, 1050, 1080, 1080, 1200, 1200, 1392, 1440, 1440, 1536, 1600, 2160, 4320]
            data = url.replace('xxx',str(size_x[random.randint(0,len(size_x)-1)]))
            data = data.replace('yyy',str(size_y[random.randint(0,len(size_y)-1)]))
            #print(data)
            if not os.path.exists('images'):
                os.makedirs('images')
            imgfilename = 'images/'+datetime.datetime.today().strftime('%d%m%Y-%H%M%S%f%p') + '.jpg'
            req.urlretrieve(data+'.jpg',imgfilename)
            req.urlcleanup()
        print('\r'+'\nCompleted\n',end='',flush=True)
    except KeyboardInterrupt:
        print("\n[0] Force Exit Command Executed\n")
        req.urlcleanup()
        exit()
done = False
while not done:
    try:
        os.system('cls')
        menu = input("1. Download Image\n2. Remove all downloaded image\n3. Custom Resolution\n4. Exit\n>>> ")
        if int(menu) == 1:    
            print("insert 0 to cancel")
            index = input("How Many Pic : ")
            if int(index) == 0:
                continue
            Download(int(index))
            menu = 0
        elif int(menu) == 2:
            try:
                shutil.rmtree('./images')
                menu = 0
                print("All Images inside default folder deleted successfully")
                time.sleep(2)
            except OSError as e:
                #print ("Error: %s - %s." % (e.filename, e.strerror))
                print("[1] Error {}".format(e.strerror) + " or already removed")
                time.sleep(2)
        elif int(menu) == 3:
            print("insert 0 for cancel")
            w = input("Insert Width :\n>>> ")
            if int(w) == 0:
                continue
            h = input("Insert Height :\n>>> ")
            if int(h) == 0:
                continue
            many = input("How Many :\n>>> ")
            if int(many) == 0:
                continue
            DownloadC(w,h,many)
            menu = 0
        elif int(menu) == 4:
            print("Exit")
            done = True
            exit()
    except KeyboardInterrupt:
        print("[0] Force Exit Command Executed")
        exit()
    except Exception as e:
        exit()
        