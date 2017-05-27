# coding=utf-8
from action import Action
from exception import RequiredParameters


class Customer(Action):

	def create(self, data):
		if not data.get('document_number', None):
			raise RequiredParameters('Customer document_number not informed')
		elif not data.get('name', None):
			raise RequiredParameters('Customer name not informed')
		elif not data.get('email', None):
			raise RequiredParameters('Customer email not informed')
		
		elif not data.get('address', None):
			raise RequiredParameters('Customer address not informed')
		elif not data['address'].get('zipcode', None):
			raise RequiredParameters('Customer zipcode not informed')
		elif not data['address'].get('street', None):
			raise RequiredParameters('Customer street not informed')
		elif not data['address'].get('street_number', None):
			raise RequiredParameters('Customer street_number not informed')
		elif not data['address'].get('neighborhood', None):
			raise RequiredParameters('Customer neighborhood not informed')

		elif not data.get('phone', None):
			raise RequiredParameters('Customer phone not informed')
		elif not data['phone'].get('ddd', None):
			raise RequiredParameters('Customer ddd not informed')
		elif not data['phone'].get('number', None):
			raise RequiredParameters('Customer number not informed')
		url = self.api.get_url(['customers'])
		return super(Customer, self).create(url, data)

	def find(self, id):
		url = self.api.get_url(['customers', id])
		return super(Customer, self).search(url)

	def list(self, data={}):
		url = self.api.get_url(['customers'])
		return super(Customer, self).list(url, data)