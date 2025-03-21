from os import getenv,path,startfile
from time import sleep
from datetime import datetime
from pyautogui import locateOnScreen, hotkey, typewrite, click, press
import traceback
filepath_active = r"C:\Users\sushi\OneDrive\Desktop\Dawanal\identifier.png"
# filepath_identifier = "dependency\\whatsapp_identifier.png"
# filepath_open = "dependency\\whatsapp_open.png"
# filepath_image = "dependency\\whatsapp_image.png"
# filepath_attach = "dependency\\whatsapp_attach.png"
# filepath_send = "dependency\\whatsapp_send.png"
# filepath_notfound = "dependency\\whatsapp_notfound.png"

class SendWhatsAppMsg():
    def send_message(self, message):
        try:
            hotkey('win')
            sleep(0.5)
            typewrite('WhatsApp')
            sleep(1)
            press("Enter")
            try:
                while(locateOnScreen(filepath_active,confidence = 0.5)):
                    sleep(0.5)
            except:
                sleep(1)
                hotkey('ctrl','n')
                sleep(0.5)
                typewrite(message[1])
                sleep(1)
                hotkey('tab')
                sleep(0.5)
                press('Enter')
                sleep(1)
                typewrite(message[0])
                sleep(1)
                press('Enter')
            


        except Exception as e:
            print(traceback.format_exc())
            print(str(e))
            try:
                with open('logs.log','a') as f:
                    f.write(str(datetime.now())+"  "+str(e)+"\n")
            except:
                f = open('logs.log','w')
                f.write(str(datetime.now())+"  "+str(e)+"\n")
        
