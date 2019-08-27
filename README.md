_____________________________________

""" BASED ON THE CODING PROBLEM """
_____________________________________

____________________________________________________

FOLLOWING TECHNOLOGIES ARE USED HERE THIS APPLICATION!
____________________________________________________

Python 3.6.8
Flask 1.1.1
Mongodb 3.6.3

____________________________

# virtualenv -p python3 ven

# source ven/bin/activate
_____________________


# Install Prerequisites:
______________________

# requirements.txt

# pip install -r requirements.txt

# python run.py


______________________

# TWO API'S ARE CREATED:
______________________

# Home Page ( http://127.0.0.1:5000 ) > compatible(Browser)

# 1.GET to List ( http://127.0.0.1:5000/employee ) > compatible(Browser)
# 2.POST to Add Record ( http://127.0.0.1:5000/employee ) > compatible(Postman)

________________

# SAMPLE PAYLOAD:
________________


{
	"name": "Sundar",
    "address": "Sundar,  #57, Vee Vee Residency, Devarachikkanahalli",
    "bank_account": {
        "account_id": "1000065218216572",
        "name": "HDFC BANK",
        "address": "HDFC BANK, Kormangala, 560076"
    }
}
_______________________________________________________________________________

# Logger File is Added.