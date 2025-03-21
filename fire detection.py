import cv2
import serial
import pywhatkit as kit
import time
ser = serial.Serial('COM6', 9600, timeout=1)
Alarm_Status = False
Email_Status = False
Fire_Reported = 0

MAXITER = 3
fire_cascade = cv2.CascadeClassifier(
    r"C:\Users\Sivansh\OneDrive\Desktop\Dawanal Rakshak\fire_cascade.xml"
)

vid = cv2.VideoCapture(0)

while True:
    # Value in ret is True # To read video frame
    _, frame = vid.read()
    # To convert frame into gray color
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # to provide frame resolution
    fire = fire_cascade.detectMultiScale(frame, 1.2, 5)

    ## to highlight fire with square
    for x, y, w, h in fire:
        cv2.rectangle(frame, (x - 20, y - 20), (x + w + 20, y + h + 20), (255, 0, 0), 2)
        roi_gray = gray[y : y + h, x : x + w]
        roi_color = frame[y : y + h, x : x + w]

        Fire_Reported += 1

    cv2.imshow("frame", frame)

    if Fire_Reported >= MAXITER:  # Iterations
        Fire_Reported = 0
        try:
            try:
                ser.write(b'F')
                print("Sent 'F' to Arduino")
            except:
                pass
            # Sending WhatsApp messages
            kit.sendwhatmsg_instantly("+917015182991", "There is a fire at the forest", 0, 0)
              # Replace +1234567890 with recipient's phone number
            time.sleep(2)
            print("F")
        except Exception as e:
            print("Error:", e)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cv2.destroyAllWindows()
vid.release()
