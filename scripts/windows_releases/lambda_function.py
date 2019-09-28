# coding: utf-8

import json
import time
from selenium import webdriver

WINDOWS_RELEASE_INFORMATION_URL = 'https://docs.microsoft.com/ja-jp/windows/release-information/'

def get_release_info():
  options = webdriver.ChromeOptions()
  options.binary_location = './bin/headless-chromium'
  options.add_argument('--headless')
  options.add_argument('--disable-gpu')
  options.add_argument('--window-size=1920,1080')
  options.add_argument('--single-process')
  options.add_argument('--ignore-certificate-errors')
  options.add_argument('--homedir=/tmp')

  driver = webdriver.Chrome('./bin/chromedriver', chrome_options=options)
  driver.get(WINDOWS_RELEASE_INFORMATION_URL)
  time.sleep(5)
  title = driver.title

  driver.close()

  return title


def lambda_handler(event, context):
  return get_release_info()
