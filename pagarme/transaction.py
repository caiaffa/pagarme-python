# coding=utf-8
from action import Action
from exception import RequiredParameters


class Transaction(Action):

	def create(self, data):
		if not data.get('amount', None):
			raise RequiredParameters('Transaction amount not informed')
		elif not data.get('payment_method', None) or data.get('card_hash', None):
			raise RequiredParameters('Transaction payment_method or card_hash not informed')
		url = self.api.get_url(['transactions'])
		return super(Transaction, self).create(url, data)

	def find(self, id):
		url = self.api.get_url(['transactions', id])
		return super(Transaction, self).search(url)

	def list(self, data={}):
		url = self.api.get_url(['transactions'])
		return super(Transaction, self).list(url, data)

	def create_key(self, data):
		if not data.get('encryption_key', None):
			raise RequiredParameters('Transaction encryption_key not informed')
		url = self.api.get_url(['transactions', 'card_hash_key'])
		return super(Transaction, self).list(url, data)

	def split_rule(self, id):
		url = self.api.get_url(['transactions', id , 'split_rules'])
		return super(Transaction, self).list(url)

	def refund(self, id):
		url = self.api.get_url(['transactions', id , 'refund'])
		return super(Transaction, self).refund_post(url)