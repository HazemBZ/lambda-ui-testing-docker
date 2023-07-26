import os
import json
from selenium import webdriver


from pyvirtualdisplay import Display
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options as ChromeOptions



main_url = "https://google.com"

# br = os.environ['BROWSER'].lower()
# br_version = os.environ['BROWSER_VERSION']
# driver_version = os.environ['DRIVER_VERSION']


# if 'DISPLAY' in os.environ and os.environ['DISPLAY'] == ':25':
#     enable_display = True

enable_display = True

if enable_display:
    display = Display(visible=False, extra_args=[':25'], size=(2560, 1440)) 


## ===== Chrome part =====
chrome_options = ChromeOptions()

if not enable_display:
    chrome_options.add_argument('--headless')
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--disable-dev-tools")
chrome_options.add_argument("--no-zygote")
chrome_options.add_argument("--single-process")
chrome_options.add_argument("window-size=2560x1440")
chrome_options.add_argument("--user-data-dir=/tmp/chrome-user-data")
chrome_options.add_argument("--remote-debugging-port=9222")
chrome_options.binary_location = '/opt/chrome/' + "88.0.4324.150" + '/chrome'
# driver = webdriver.Chrome(executable_path='/opt/chromedriver/' + driver_version + '/chromedriver',
#                             options=chrome_options,
#                             service_log_path='/tmp/chromedriver.log')

driver = webdriver.Chrome(executable_path='/opt/chromedriver/' + "88.0.4324.96" + '/chromedriver',
                            options=chrome_options,
                            service_log_path='/tmp/chromedriver.log')

                            
def testcase():
    if driver:
        print('Started Chrome Driver')

    driver.get(main_url)

    WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, 'kp')))

# Take screenshot 
# browser.save_screenshot('screenie.png')




def lambda_handler(event, context):
    'Lambda Handler'
    # print('Inside Handler')
    print(event)
    browser = driver
    if not browser:
        return {
            "statusCode": 500,
            "headers": {
                "Content-Type": "application/json"
            },
            "body": json.dumps({ "message": "Unsupported browser: "  })
        }
    resp = {"message": "done"}

    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json"
        },
        "body": json.dumps({
            "message": resp['message']
        })
    }
