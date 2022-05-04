import os
from json import loads
from httpx import get
from updates import logging
class MD:
  @staticmethod
  def _read():
    with open("auth.txt", "r") as E:
      return {"str" : E.read(), "list" : E.readlines()}
  
  @staticmethod
  def _write(content):
    the = MD._read()
    with open("auth.txt", "w") as E:
      E.write(f"{the}\n{content}")

class auth:
  @staticmethod
  def check(name):
    logging.send(md='fix', content=f"[ {name} | Attempting verification ]")
    raw = get(f"https://replit.com/data/repls/@qr0n/{name}")
    data = loads(raw.text)
    if "XQCL1" or "IR7140" or "TaRAk" in data['fileNames']:
      logging.send(md='re', content=f"[ {name} | Passed verification ]")
      return True
    else:
      logging.send(md='css', content=f"[ {name} | Failed verification ]")
      return False