
from dotenv import dotenv_values
from more_itertools import bucket
from pyqiwip2p import QiwiP2P
from dotenv import load_dotenv
import os

load_dotenv()
secret_key = os.getenv('secret_qiwi_key')


p2p = QiwiP2P(auth_key=secret_key)#, alt='example.com'

def create_bill(amount, lifetime, comment):
  #amount=amount
  bill = p2p.bill(amount=1, lifetime=lifetime, comment=comment)
  return bill

def _check_bill_status(bill_id):
  try:

    pay_url = str(p2p.check(bill_id=str(bill_id)).pay_url)
    status = str(p2p.check(bill_id=str(bill_id)).status)
    bill_id = str(p2p.check(bill_id=str(bill_id)).bill_id)
  except Exception as e:
    return False

  if status == 'PAID':
    return True
  return False
