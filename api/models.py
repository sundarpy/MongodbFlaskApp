import mongoengine as db

class BankAccounts(db.EmbeddedDocument):
	account_id = db.StringField(max_length=16, required=True)
	name = db.StringField(max_length=120, required=True)
	address = db.StringField(max_length=120, default=None)

"""  Employee Document """

class Employee(db.Document):
    name = db.StringField(max_length=120, required=True)
    bank_account = db.EmbeddedDocumentField(BankAccounts, required=True)
    address = db.StringField(max_length=175, default=None)

""" Connect with Mongodb """    
db.connect('myapp')
