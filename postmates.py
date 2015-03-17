import requests
from requests.auth import HTTPBasicAuth
from deliveryquote import DeliveryQuote
import json

class PostMates:
    DELIVERY = "delivery"
    PICKUP_ADDRESS = "pickup_address"
    DROPOFF_ADDRESS = "dropoff_address"

    FILTER = 'filter'
    ONGOING = 'ongoing'

    GET = "get"
    POST = "post"

    CREATE_DELIVERY_POST_PARAMS = set([
        'manifest',
        'pickup_name',
        'pickup_address',
        'pickup_phone_number',
        'dropoff_name',
        'dropoff_address',
        'dropoff_phone_number'
    ])

    GET_DELIVERY_QUOTE_PARAMS = set([
        'pickup_address',
        'dropoff_address'
    ])

    def __init__(self,customerId,apiKey,baseUrl, version):
        self.customerId = customerId
        self.apiKey = apiKey
        self.baseUrl = baseUrl
        self.version = version
        self.auth = (self.apiKey,'')


    def postDeliveryQuote(self, pickupAddress, dropoffAddress):
        params = {
            self.PICKUP_ADDRESS : pickupAddress,
            self.DROPOFF_ADDRESS : dropoffAddress
        }
        url = "customers/"+self.customerId+"/delivery_quotes"
        data = self.__makeRequest(url,params,self.POST)

        return DeliveryQuote(data,pickupAddress, dropoffAddress)

    def getDeliveries(self,ongoing = False):
        params = {}
        if ongoing:
            params = {
                            self.FILTER : self.ONGOING,
            }
        url = "customers/"+self.customerId+"/deliveries"

        data = self.__makeRequest(url, params, self.GET)
        return data['data']


    def __makeRequest(self,url,params = {},type="get"):
        fullUrl = self.baseUrl + '/' + self.version +  '/' + url

        if type == self.GET:
            response = requests.get(fullUrl, params = params,auth=self.auth)
        elif type == self.POST:
            response = requests.post(fullUrl, params, auth=self.auth)
        try:
                response.raise_for_status()
        except requests.exceptions.HTTPError as e:
            print e.response.status_code
        return json.loads(response.text)
