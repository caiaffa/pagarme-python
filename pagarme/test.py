from transaction import Transaction
from plan import Plan
from card import Card
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


