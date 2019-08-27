import os
import logging
from api import app
from flask import Flask, jsonify, request
from flask_restful import Resource, Api
import json
from .models import Employee, BankAccounts

app = Api(app)

# Get an instance of a logger
logger = logging.getLogger(__name__)
logging.basicConfig(filename='logfile.log', level=logging.DEBUG, format='%(asctime)s : %(levelname)s : %(message)s')


class HomeView(Resource):

	""" GET Method of Home-Page"""

	def get(self):
		return jsonify({"INFO": "Hey, Here I have Created a two End Points. GET Method and Post Method", "GET": "http://127.0.0.1:5000/employee", "POST": "http://127.0.0.1:5000/employee"})

class EmployeeView(Resource):

	""" GET Method of Employee"""

	def get(self):
		employee_details = []
		for item in Employee.objects.order_by('-id'):
			details, account = dict(), dict()
			details['ID'] = str(item['id'])
			details['Name'] = item['name']
			details['Address'] = item['address']
			if item['bank_account'] is not None:
				account['Account_id'] = item['bank_account']['account_id']
				account['Name'] = item['bank_account']['name']
				account['Address'] = item['bank_account']['address']
				details['BankAccounts'] = account
			else:
				details['Name'] = None
			employee_details.append(details)
		response = jsonify({"employee_details" : employee_details})
		response.status_code = 200
		logger.info("Get list of Employee Details")
		return response

	""" POST Method of Employee"""

	def post(self):
		try:
			data = json.loads(request.data) 
			logger.debug("Employee Payload is {}".format(data))
			if data:
				emp_bank_detail = Employee(name=data['name'], address=data['address'], bank_account=BankAccounts(account_id=data["bank_account"]["account_id"], name=data["bank_account"]["name"], address=data["bank_account"]["address"]))
				emp_bank_detail.save()
				logger.debug("{}".format(emp_bank_detail.to_json(indent=4)))
				response = jsonify({'result' : "Success!"})
				response.status_code = 201
				return response
			else:
				raise ValueError("Invalid Payload!")
		except Exception as e:
			logger.error(str(e), exc_info=True)
			response = jsonify({"failure reason is " : str(e)})
			response.status_code = 400
			return response

app.add_resource(HomeView, '/')
app.add_resource(EmployeeView, '/employee')	
