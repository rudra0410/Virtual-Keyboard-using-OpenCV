import cv2
from cvzone.HandTrackingModule import HandDetector
from time import sleep
import numpy as np

# Setup webcam
cap = cv2.VideoCapture(0)
cap.set(3, 1280)  # Set width
cap.set(4, 720)   # Set height

# Initialize hand detector
detector = HandDetector(detectionCon=1)

keys = [
    ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', '='],
    ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', '[', ']', '\\'],
    ['A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', ';', "'"],
    ['Z', 'X', 'C', 'V', 'B', 'N', 'M', ',', '.', '/', ],
    [' ']
]  
        
final_text = ""

class Button():
    def __init__(self,pos,text,size=[60,60]):
        self.pos = pos
        self.size = size
        self.text = text
    
    def draw(self, img):
        x, y = self.pos
        width, height = self.size
        
        # Create a transparent overlay
        overlay = img.copy()
        
        # Draw a filled rectangle with rounded corners
        rect_color = (234, 229, 219)
        border_color = (255, 255, 255)  # White border
        alpha = 0.5  # Transparency level

        # Draw a rounded rectangle
        radius = 10  # Radius for the rounded corners
        thickness = -1  # Filled rectangle
        cv2.rectangle(overlay, (x + radius, y), (x + width - radius, y + height), rect_color, thickness)
        cv2.rectangle(overlay, (x, y + radius), (x + width, y + height - radius), rect_color, thickness)
        cv2.circle(overlay, (x + radius, y + radius), radius, rect_color, thickness)
        cv2.circle(overlay, (x + width - radius, y + radius), radius, rect_color, thickness)
        cv2.circle(overlay, (x + radius, y + height - radius), radius, rect_color, thickness)
        cv2.circle(overlay, (x + width - radius, y + height - radius), radius, rect_color, thickness)

        # Blend the overlay with the original image
        cv2.addWeighted(overlay, alpha, img, 1 - alpha, 0, img)

        # Draw the border around the button
        cv2.rectangle(img, (x, y), (x + width, y + height), border_color, 2)

        # Get the size of the text
        text_size = cv2.getTextSize(self.text, cv2.FONT_HERSHEY_PLAIN, 3, 3)[0]
        text_x = x + (width - text_size[0]) // 2
        text_y = y + (height + text_size[1]) // 2

        # Draw the button text
        cv2.putText(img, self.text, (text_x, text_y), cv2.FONT_HERSHEY_PLAIN, 3,(128,0,0), 3)
        
        return img
        

#create a list for all keyboard keys
buttonList = []

for i in range(len(keys)):
    for j,key in enumerate(keys[i]):   
        buttonList.append(Button([80*j+70,80*i+70], key , size=(60, 60) if key != ' ' else (350, 60)))

while True:
    # Read frame from webcam
    success, img = cap.read()

    # Find hands in the image
    img = detector.findHands(img)  # With draw
    # # Flip the image horizontally (mirror effect)
    # img = cv2.flip(img, 1)
    
    lmList , bboxInfo = detector.findPosition(img)
    # img = drawAll(img , buttonList)
        # Draw all the buttons
    for button in buttonList:
        button.draw(img)

    if lmList:
        for button in buttonList:
            x, y = button.pos
            width, height = button.size
            
            if x < lmList[8][0] < x + width and y < lmList[8][1] < y + height:
                
                cv2.rectangle(img, (x, y), (x + width, y + height), (0, 255, 255), cv2.FILLED)
                text_size = cv2.getTextSize(button.text, cv2.FONT_HERSHEY_PLAIN, 3, 3)[0]
                text_x = x + (width - text_size[0]) // 2
                text_y = y + (height + text_size[1]) // 2
                cv2.putText(img, button.text, (text_x, text_y), cv2.FONT_HERSHEY_PLAIN, 3, (255, 255, 255),3)
                l, _ , _ = detector.findDistance(4,16,img,draw=False)
                print(l)
                
                #when click button
                if l < 25:
                    cv2.rectangle(img, (x, y), (x + width, y + height), (0, 2, 2), cv2.FILLED)
                    text_size = cv2.getTextSize(button.text, cv2.FONT_HERSHEY_PLAIN, 3, 3)[0]
                    text_x = x + (width - text_size[0]) // 2
                    text_y = y + (height + text_size[1]) // 2
                    cv2.putText(img, button.text, (text_x, text_y), cv2.FONT_HERSHEY_PLAIN, 3, (255, 255, 255),3)
                    
                    final_text += button.text
                    sleep(0.5)
    
    # Final Output Text Box
    cv2.rectangle(img, (70,500), (700,600), (234, 229, 219), cv2.FILLED)
    cv2.putText(img, final_text, (80,575 ), cv2.FONT_HERSHEY_PLAIN, 4,(128,0,0),4)
     
    # Show the image
    cv2.imshow("Image", img)
    cv2.waitKey(1)
