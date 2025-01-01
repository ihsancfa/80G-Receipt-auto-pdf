import os
import keyboard
import pyautogui
import sys
import time
import pytesseract #Optical Character Recognition (OCR)
from PIL import Image #  (Pillow): This library is used for image manipulation

folderpath = r"C:\Users\admin\OneDrive\Desktop\TallyPrime.lnk"
os.startfile(folderpath)

time.sleep(3)

keyboard.write('TRUST 24-25') 

keyboard.press('enter')

time.sleep(1)

# verify company befor check ledgers
try:
    # Locate password field and check if it's the only match
    company = pyautogui.locateCenterOnScreen(
        r"##########\80G Receipt auto pdf\company.png",
        confidence=0.8
    )
except Exception as e:
    print(f"Error: {str(e)}. Company Quitting.")
    sys.exit()

pyautogui.press('D')
time.sleep(1)
pyautogui.press('A')
time.sleep(1)
pyautogui.press('L')
time.sleep(1)
pyautogui.write('Donation Received')
time.sleep(1)
pyautogui.press('enter')
time.sleep(1)
# verify Ledger
try:
    # Locate password field and check if it's the only match
    Ledger = pyautogui.locateCenterOnScreen(
        r"##########\80G Receipt auto pdf\company.png",
        confidence=0.8
    )
except Exception as e:
    print(f"Error: {str(e)}.Ledger Quitting.")
    sys.exit()

time.sleep(1)
pyautogui.hotkey('alt', 'f2')
time.sleep(1)
pyautogui.write('1/4/2024')
pyautogui.press('enter')
pyautogui.write('31/3/2025')
pyautogui.press('enter')

time.sleep(1)

for num in range(6899, 6929):  # Adjust the range as needed
    # Step 1: Open the find dialog
    pyautogui.hotkey('ctrl', 'f')
    time.sleep(1)

    pyautogui.press('backspace')
    time.sleep(.5)
    pyautogui.write('Voucher Number')
    time.sleep(.5)
    pyautogui.press('enter')
    time.sleep(.5)
    pyautogui.write('equal to')
    time.sleep(.5)
    pyautogui.press('enter')
    time.sleep(.5)


    pyautogui.write(str(num))  # Convert num to a string and type it in the find dialog
    pyautogui.press('enter')  # Press enter to search for the number
    time.sleep(1)

    # Step 2: Close any popups or dialogs that appear
    pyautogui.press('enter')  # Press enter to close the found popup if applicable
    time.sleep(0.5)
    pyautogui.press('tab')
    time.sleep(1)

    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # Path to tesseract executable # Adjust the path if necessary
    screenshot = pyautogui.screenshot(region=(130, 70, 500, 200)) # This captures a screenshot of the entire screen and stores it in the screenshot variable.
    screenshot_text = pytesseract.image_to_string(screenshot) # Convert screenshot to text using OCR
    

    # Check if the number 6652 is in the extracted text
    if str(num) in screenshot_text:
        print(f" {num} - Number found! Continuing the code...") # Continue with the rest of your code here
    
    else:
        print(f"{num} - Number not found. Exiting...")  # Quit the code or exit
        print("Extracted Text from Screenshot:", screenshot_text)
        sys.exit()
                
    # Step 3: Open the print dialog
    pyautogui.hotkey('ctrl', 'p')
    time.sleep(1)

    # Step 4: Press 'P' to select a print option (if needed)
    pyautogui.press('P')
    time.sleep(1)

    # Step 5: Create the dynamic file path
    path = f"T:\\My Drive\\000 ihsan\\02 Courses\\003GIT\\MYProject\\80G Receipt auto pdf\\Receipt\\{num}"
    time.sleep(1)

    # Step 6: Type the file path
    pyautogui.write(path)
    time.sleep(1)

    # Step 7: Press 'Enter' to confirm the file path
    pyautogui.press('enter')
    time.sleep(2)

    # Step 8: Press 'Esc' key to close any dialogs
    pyautogui.press('esc')  # Corrected the key to 'esc'
    time.sleep(0.5)
    pyautogui.press('esc')
    time.sleep(0.5)
    pyautogui.press('esc')
    time.sleep(0.5)
    pyautogui.press('esc')
    


