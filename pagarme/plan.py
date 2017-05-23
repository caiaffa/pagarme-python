# coding=utf-8
from action import Action
from exception import RequiredParameters


class Plan(Action):

	def create(self, data):
		if not data.get('amount', None):
			raise RequiredParameters('Plan amount not informed')
		elif not data.get('days', None) :
			raise RequiredParameters('Plan days not informed')
		elif not data.get('name', None) :
			raise RequiredParameters('Plan name not informed')
		url = self.api.get_url(['plans'])
		return super(Plan, self).create(url, data)

	def find(self, id):
		url = self.api.get_url(['plans', id])
		return super(Plan, self).search(url)

	def list(self, data={}):
		url = self.api.get_url(['plans'])
		return super(Plan, self).list(url, data)

	def change(self, id, data={}):
		url = self.api.get_url(['plans', id])
		return super(Plan, self).change(url, data)



