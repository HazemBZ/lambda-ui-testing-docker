import os
import json
from selenium import webdriver


from pyvirtualdisplay import Display
from pyvirtualdisplay.smartdisplay import SmartDisplay
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service



enable_display = True
error = ''

try:

    ## ===== Chrome part =====
    chrome_options = ChromeOptions()

    service = Service(executable_path='/opt/driver/chromedriver')

    if not enable_display:
        chrome_options.add_argument('--headless')
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--single-process")
    chrome_options.binary_location = '/opt/chrome/chrome-linux/chrome'
    chrome_options.add_argument("--no-zygote")
    chrome_options.add_argument("--single-process")

    print('## {DISPLAY}: ', os.environ['DISPLAY'])
    print('#==== Starting emu display')
    display = Display(visible=False, extra_args=[':25'], size=(800, 800))
    display.start()
    print('#==== Starting chrome Driver')
    driver = webdriver.Chrome(service=service, options=chrome_options)
    print('#==== Stopping emu display')
    display.stop()

except Exception as e:
    error = e
    print(e)





def lambda_handler(event, context):
    global error
    'Lambda Handler'
    print('#===> Inside Handler')
    print(event)

    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json"
        },
        "body": json.dumps({
            "message": "finished executing",
            "error": str(error)
        })
    }
