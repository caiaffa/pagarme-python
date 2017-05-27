# coding=utf-8
from action import Action
from exception import RequiredParameters


class Subscription(Action):

	def create(self, data):
		if not data.get('amount', None):
			raise RequiredParameters('Plan create amount not informed')
		elif not data.get('days', None) :
			raise RequiredParameters('Plan create days not informed')
		elif not data.get('name', None) :
			raise RequiredParameters('Plan create name not informed')
		url = self.api.get_url(['plans'])
		return super(Subscription, self).create(url, data)

	def find(self, id):
		url = self.api.get_url(['subscriptions', id])
		return super(Subscription, self).search(url)

	def list(self, data={}):
		url = self.api.get_url(['subscriptions'])
		return super(Subscription, self).list(url, data)

	def change(self, id, data={}):
		url = self.api.get_url(['subscriptions', id])
		return super(Subscription, self).change(url, data)

	def cancel(self, id, data={}):
		url = self.api.get_url(['subscriptions', id, cancel])
		return super(Subscription, self).refund_post(url, data)