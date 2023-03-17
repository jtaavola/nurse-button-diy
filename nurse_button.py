#!/usr/bin/env python3

import aiy.voicehat
import time
import os
from dotenv import load_dotenv
from twilio.rest import Client

load_dotenv()

account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token  = os.environ['TWILIO_AUTH_TOKEN']
to_numbers = os.environ['TWILIO_TO_NUMBERS'].split(',')
from_number = os.environ['TWILIO_FROM_NUMBER']

def main():
  button = aiy.voicehat.get_button()
  led = aiy.voicehat.get_led()

  client = Client(account_sid, auth_token)
  while True:
    button.wait_for_press()
    print('button was pressed')
    for number in to_numbers:
      message = client.messages.create(
        to=number, 
        from_=from_number,
        body="The nurse button has been pressed.")
    # pulse the LED for 10 sec
    led.set_state(aiy.voicehat.LED.PULSE_SLOW)
    time.sleep(10)
    led.set_state(aiy.voicehat.LED.OFF)
    # rate limit
    time.sleep(60)

if __name__ == '__main__':
  main()