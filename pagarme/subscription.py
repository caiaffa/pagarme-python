# coding=utf-8
from action import Action
from exception import RequiredParameters


class Subscription(Action):

	def create(self, data):
		if not data.get('plan_id', None):
			raise RequiredParameters('Subscription create plan_id not informed')
		elif not data.get('card_hash', None) and not data.get('card_id', None):
			raise RequiredParameters('Subscription create card_hash  or card_id not informed')
		elif not data.get('customer', None) :
			raise RequiredParameters('Subscription create customer not informed')
		elif not data['customer'].get('email', None) :
			raise RequiredParameters('Subscription create email not informed')
		url = self.api.get_url(['subscriptions'])
		return super(Subscription, self).create(url, data)

	def create_ticket(self, data):
		data['payment_method'] = 'boleto'
		if not data.get('plan_id', None):
			raise RequiredParameters('Subscription create plan_id not informed')
		elif not data.get('customer', None) :
			raise RequiredParameters('Subscription create customer not informed')
		elif not data['customer'].get('email', None) :
			raise RequiredParameters('Subscription create email not informed')
		url = self.api.get_url(['subscriptions'])
		return super(Subscription, self).create(url, data)

	def create_split(self, data):
		if not data.get('plan_id', None):
			raise RequiredParameters('Subscription create plan_id not informed')
		elif not data.get('customer', None) :
			raise RequiredParameters('Subscription create customer not informed')
		elif not data['customer'].get('email', None) :
			raise RequiredParameters('Subscription create email not informed')
		url = self.api.get_url(['subscriptions'])
		return super(Subscription, self).create(url, data)

	def find(self, id):
		url = self.api.get_url(['subscriptions', id])
		return super(Subscription, self).search(url)

	def list(self, data={}):
		url = self.api.get_url(['subscriptions'])
		return super(Subscription, self).list(url, data)

	def change(self, id, data={}):
		if not data.get('payment_method', None):
			raise RequiredParameters('Subscription change payment_method not informed')
		url = self.api.get_url(['subscriptions', id])
		return super(Subscription, self).change(url, data)

	def cancel(self, id, data={}):
		url = self.api.get_url(['subscriptions', id, 'cancel'])
		return super(Subscription, self).refund_post(url, data)