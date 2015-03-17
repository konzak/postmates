import ConfigParser


print "Please enter your API key."
apiKey = raw_input().strip()

print "Please enter you customer ID"
customerId = raw_input().strip()

config = ConfigParser.RawConfigParser()

config.add_section('Section1')
config.set('Section1', 'api_key', apiKey)
config.set('Section1', 'customer_id', customerId)
config.set('Section1', 'base_url', 'https://api.postmates.com')
config.set('Section1', 'version', 'v1')

with open('projectconfig.cfg', 'wb') as configfile:
    config.write(configfile)
