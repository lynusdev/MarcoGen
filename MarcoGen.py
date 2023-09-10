import requests
import string
import random

uid = input("Enter user id: ")

def get_stats(uid):
    response = requests.get(f"https://www.marcophono.com/app/checkuseraccount.php?uid={uid}")
    return response.text

def gen_premis(uid, amount):
    requests.get(f"https://www.marcophono.com/app/updatepremis.php?uid={uid}&premis={amount}")
    print(f"Generated {amount} premis!")

def gen_coins(uid):
    new_uid = f"Az{''.join(random.choices(string.ascii_uppercase + string.digits, k=24))}"
    pcode = new_uid[0:9].upper()
    pcode
    requests.get(f"https://www.marcophono.com/app2/statcode.php?u={new_uid}")
    requests.get(f"https://www.marcophono.com/app2/asktarget.php?uid={new_uid}")
    requests.get(f"https://www.marcophono.com/app/checkuseraccount.php?uid={new_uid}&app=ADE")
    requests.get(f"https://www.marcophono.com/app/checkpcode.php?pcode={pcode}&uid={uid}")
    requests.get(f"https://www.marcophono.com/app/updatecoins.php?uid={uid}&p=20")
    balance = requests.get(f"https://www.marcophono.com/app/checkuseraccount.php?uid={uid}").text.split(";")[1]
    print("Generated 20 coins!")
    return balance

def gen_szenes(uid):
    requests.get(f"https://www.marcophono.com/app/updateszenes.php?uid={uid}&szenes=audio22:audioM105:audio25:audioM5:audio47:audioM42:audioM43:audioM46:audioM41:audio2:audio24:")
    print(f"Unlocked szenes!")

gen_szenes(uid)
gen_premis(uid,400000000)
input("Done!")