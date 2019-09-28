# coding: utf-8

import json
import time
from selenium import webdriver

import os.path
from googleapiclient.discovery import build
from google.oauth2.service_account import Credentials


SPREADSHEET_ID = '12vLBLJXKzCuTHk4H8v2qjkY2A4mVTnsxwprxNBrYgrs'
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


def get_sheets_service():
  creds = Credentials.from_service_account_file('credentials.json')
  return build('sheets', 'v4', credentials=creds)


def read_sheet(service):
  range = 'Test!A1:A2'

  sheet = service.spreadsheets()
  result = sheet.values().get(spreadsheetId=SPREADSHEET_ID, range=range).execute()

  values = result.get('values', [])

  if not values:
    print('No data found.')
  else:
    print('Name')
    for row in values:
      print('%s' % (row[0]))


def lambda_handler(event, context):
  service = get_sheets_service()
  read_sheet(service)
