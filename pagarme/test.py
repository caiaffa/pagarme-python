from transaction import Transaction
from plan import Plan
from card import Card
from bank_account import BankAccount
from customer import Customer
import pprint

###
# Transaction 1551520,
###
#pprint.pprint (Transaction().split_rule(1551520))

###
# Card
###
# create pprint.pprint (Card().create(data={'card_hash':'580404_I1BCMNhpekqfLbsbjQSSviDNYexbKPgp9S6Dc+/jL32jsrilaxJJ8GA8hvaRpAgkgaB8ogM6llxQktNRxwVwcJPxS7vZQJbKNoByOMvUe9he2HUmWdIid2vrMP3Hr1ap+xFTEvdetKLlC/6+dnlCZrha7Fodo6WrwH98A5s0ahOPfUslRZkUprGwwdTvSmVXOl642jVnhvNsYrsuEphuERo4Ut1ZSz86md/O8xCSlEcNyo8Wg7JVzo/A0cniR3RMUA9ggZ3NDkJz8psOytlWjsSr1PFY7tf2ijnSldN0CxMJMcvL5zeretwqO+rUWCN1tW+ZKnnxYrZ1qH2/L9maUg=='}))
# find pprint.pprint (Card().find('card_cj2zaz3jj00x5d76e5i95ujrk'))

###
# Plan
###
# create pprint.pprint(Plan().create(data={'amount':'500','days':'30','name':'Plano Teste'}))
# find pprint.pprint (Plan().find('160811'))
# list pprint.pprint (Plan().list())
# change pprint.pprint (Plan().change(160811, data={'name':'plano felipe'}))

###
# Bank_account
###
# create
'''
data = {
	'bank_code':'341',
	'agencia':'0932',
	'conta':'58054',
	'conta_dv':'1',
	'document_number':'35146484252',
	'legal_name':'Luis',
}
pprint.pprint(BankAccount().create(data))
'''
# find pprint.pprint (BankAccount().find('17482546'))
# list pprint.pprint (BankAccount().list())
'''
###
# Customer
###

address = {
	'street':'Rua teste',
	'street_number': '101',
	'neighborhood': 'teste',
	'zipcode':'25845000',
}

phone = {
	'ddd':'24',
	'number':'999887766',
}

data = {
	'document_number':'18152564000105',
	'name':'cliente teste',
	'email':'teste@teste.com',
	'address':address,
	'phone':phone,
}
pprint.pprint(Customer().create(data))
'''
# find pprint.pprint (Customer().find('191762'))
# list pprint.pprint (Customer().list())
