from paypal import PayPalConfig
from paypal import PayPalInterface

WTF_CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'

config = PayPalConfig(API_USERNAME = "seoyun.h.lee-facilitator_api1.gmail.com",
                      API_PASSWORD = "8F9Z896JXZBLZ296",
                      API_SIGNATURE = "Aa5fNoo4pUWlz9y7We5CVXiFH3cdAjFDX0jzONVR9BvON3NrwbUh2Ulh",
                      DEBUG_LEVEL=0)

interface = PayPalInterface(config=config)