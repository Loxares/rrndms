import time
import random
import uuid

print("Please enter your bitcoin wallet:")
input()
time.sleep(7)
print("Welcome Loxares, will start shortly!")
time.sleep(6)
print(".__                                            \r\n|  |   ________________  ___  ___ ____   ______\r\n|  |  /  _ \\_  __ \\__  \\ \\  \\/  // __ \\ /  ___/\r\n|  |_(  <_> )  | \\// __ \\_>    <\\  ___/ \\___ \\ \r\n|____/\\____/|__|  (____  /__/\\_ \\\\___  >____  >\r\n                       \\/      \\/    \\/     \\/ ")
print("Please wait till wallet mining starts (may take a while)")
time.sleep(30)
print("Loading..")
time.sleep(7)

for i in range(999999999999999999):
    address = str(uuid.uuid4())[:35]
    balance = random.random() * 10

    print(f"Bitcoin Address: {address} | Balance: ${balance}")
