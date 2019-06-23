import os, json, time, requests, hashlib, shutil,threading

def MD5():
    url = 'https://helloacm.com/api/random'
    data = requests.get(url).json()
    hash_object1 = hashlib.md5(data.encode())
    #print(hash_object1.hexdigest())
    newdata = hash_object1.hexdigest()
    if not os.path.exists('result'):
        os.makedirs('result')
    with open('result/md5.txt','a') as op:
        op.write(str(newdata) + ' : ' + str(data) + '\n')
        op.close()
        
def SHA256():
    url = 'https://helloacm.com/api/random'
    data = requests.get(url).json()
    hash_object2 = hashlib.sha256(data.encode())
    #print(hash_object2.hexdigest())
    newdata = hash_object2.hexdigest()
    if not os.path.exists('result'):
        os.makedirs('result')
    with open('result/sha256.txt','a') as out:
        out.write(str(newdata) + ' : ' + str(data) + '\n')
        out.close()
        
def remove():
    shutil.rmtree('result')

menu = input("1. Start\n2. DeleteData\n3. Exit\n>>> ")
if int(menu) == 1:    
    much = input("End = ctrl + c")
    try:
        i=0
        while i < 100000:
            thread1 = threading.Thread( target=MD5 , daemon=True )
            thread2 = threading.Thread( target=SHA256 , daemon=True )
            thread1.start()
            thread2.start()
            i+=1
            #print("Running...")
            #os.system('cls')
            #time.sleep(0.2) #safe
            #time.sleep(0.1) #fast
            time.sleep(0.25)
        print("Completed")
    except Exception as e:
        print("Err")
elif int(menu) == 2:
    try:
        remove()
    except OSError as i:
        print("Error [", i.strerror,"]")
elif int(menu) == 3:
    exit()
#print(hashlib.algorithms_available)
#print(hashlib.algorithms_guaranteed)



