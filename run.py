import ConfigParser
from postmates import PostMates

API_KEY = 'api_key'
CUSTOMER_ID = 'customer_id'
BASE_URL = 'base_url'
VERSION = 'version'
SECTION1 = 'Section1'

config = ConfigParser.RawConfigParser()
config.read('projectconfig.cfg')

apiKey = config.get(SECTION1,API_KEY)
customerId = config.get(SECTION1,CUSTOMER_ID)
baseURL = config.get(SECTION1,BASE_URL)
version = config.get(SECTION1,VERSION)


# Some examples

postMates = PostMates(customerId, apiKey, baseURL, version)

pickupAddress="20 McAllister St, San Francisco, CA"
dropoffAddress="101 Market St, San Francisco, CA"

deliveryQuote = postMates.postDeliveryQuote(pickupAddress,dropoffAddress)
print deliveryQuote.getExpires()

print postMates.getDeliveries()
