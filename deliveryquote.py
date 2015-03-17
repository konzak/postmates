
class DeliveryQuote:

	KIND = 'kind'
	FEE = 'fee'
	CREATED = 'created'
	EXPIRES = 'expires'
	CURRENCY = 'currency'
	DURATION = 'duration'
	DROPOFF_ETA = 'dropoff_eta'
	ID = 'id'

	def __init__(self,data,pickupAddress, dropoffAddress):
		self.kind = data.get(self.KIND)
		self.fee = data.get(self.FEE)
		self.created = data.get(self.CREATED)
		self.expires = data.get(self.EXPIRES)
		self.currency = data.get(self.CURRENCY)
		self.duration = data.get(self.DURATION)
		self.dropoffETA = data.get(self.DROPOFF_ETA)
		self.id = data.get(self.ID)
		self.pickupAddress = pickupAddress
		self.dropoffAddress = dropoffAddress

	def getKind(self):
		return self.kind
	
	def getFee(self):
		return self.fee

	def getCreated(self):
		return self.created
 
	def getExpires(self):
		return self.expires

	def getCurrency(self):
		return self.currency

	def getDuration(self):
		return self.duration

	def getDropoffETA(self):
		return self.dropoffETA

	def getId(self):
		return self.id

	def getDropoffAddress(self):
		return self.dropoffAddress

	def getPickupAddress(self):
		return self.pickupAddress
