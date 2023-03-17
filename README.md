# nurse-button-diy

[![Python](https://img.shields.io/badge/Python-000000?logo=python&style=for-the-badge)](https://www.python.org)
[![Raspberry Pi](https://img.shields.io/badge/Raspberry%20Pi-A22846?logo=raspberrypi&style=for-the-badge)](https://www.raspberrypi.org)
[![Twilio](https://img.shields.io/badge/Twilio-000000?logo=twilio&style=for-the-badge)](https://www.twilio.com)

I repurposed an old [AIY Google Voice Kit (V1)](https://aiyprojects.withgoogle.com/voice-v1/) to make a simple nurse button. If the button is pressed, a text message is sent to designated recipients using [Twilio](https://www.twilio.com). The voice kit speaker and mic aren't used at all.

The `aiy/` code was taken from Voice Kit SD image.

## Development

### Assemble nurse button

Follow [this guide](https://aiyprojects.withgoogle.com/voice-v1/) to assemble the kit and install the Voice Kit image to your Raspberry Pi.

### Clone

From your Raspberry Pi, clone this repo.
```sh
git clone https://github.com/jtaavola/nurse-button-diy
```

### Install dependencies

```sh
pip3 install twilio python-dotenv
```

### Configure environment variables

Create a `.env` file at the root of the project to set the environment variables
```sh
# sid and auth token from https://console.twilio.com/
TWILIO_ACCOUNT_SID=<account_sid>
TWILIO_AUTH_TOKEN=<auth_token>
# phone numbers must be in E.164 format
TWILIO_FROM_NUMBER=+1234567890
# comma separate list of phone numbers to send the SMS to
TWILIO_TO_NUMBERS=+12345678901,+13456789012
```

### `python3 nurse_button.py`

Run the nurse button program. If you want this to run on startup, you can add a cron job.

Run
```sh
crontab -e
```

and add
```
@reboot python3 /path/to/nurse_button.py
```
