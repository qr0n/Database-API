import os
import json
from updates import logging
from flask import request

x = [f.name for f in os.scandir() if f.is_file()]
allowed_apps = ['Iron Cloud', "NoteCloud", "4162", "DisFrame", "The Nerd Group", "Demo", "xyz.ir0n.services"]


class render:
  @staticmethod
  def online():
    with os.scandir('/home/runner/db/base') as i:
      return [entry.name for entry in i]
  
  @staticmethod
  def scripts():
    with os.scandir('/home/runner/db/scripts') as o:
      return [entry.name for entry in o]

class db:
    @staticmethod
    def save(k, v, f):
        with open(f"base/{f}.json", "r") as E:
            lE = json.load(E)
            lE[k] = v
        with open(f"base/{f}.json", "w") as E:
            json.dump(lE, E)
            logging.send(md="re", content=f"[{f} | contents have updated(+1 key)]")
            return lE[k]

    @staticmethod
    def create_database(fn):
      with open(f"base/{fn}.json", "w") as E:
        E.write("{\n\n}")
        logging.send("re", content=f"[{fn} | created]")
        return f"base/{fn}.json has been made"

    @staticmethod
    def show(f):
      with open(f"base/{f}.json", "r") as E:
        lE = json.load(E)
        logging.send(md="fix", content=f"[{f} | contents have been veiwed]")
        return lE
    
    @staticmethod
    def index(k, f):
      with open(f"base/{f}.json", "r") as E:
        lE = json.load(E)
        logging.send(md="ini", content=f"[{f} | contents have been indexed]")
        try:
          return lE[k]
        except KeyError:
          return "404"

    @staticmethod
    def delete(k, f):
      with open(f"base/{f}.json", "r") as E:
        lE = json.load(E)
        del lE[k]
      with open(f"base/{f}.json", "w") as E:
        logging.send(md="css", content=f"[{f} | {k} has been deleted(-1 key)")
        json.dump(lE, E)

    @staticmethod
    def delete_database(fn):
      logging.send(md="css", content=f"[{fn} | deleted]")
      os.remove(f"base/{fn}.json")
      return "deleted"
    
    @staticmethod
    def fork(pack, id):
      with open(f"packages/{pack}.py", "r") as E:
        if id in allowed_apps:
          logging.send(md="re", content=f"[{pack} | uploading to {id}]")
          return E.read()
        else:
          logging.send(md="css", content=f"[{request.args.get('p')} | uploading terminated to {request.args.get('app_id')}]")
          with open(f"packages/README.py", "r") as E:
            return 
    # @staticmethod
    # def archive(fn):
    #   with open(f"base/{fn}.json", "r") as E:
    #     lE = json.load(E)
    #   with open(f"archived/{fn}.json", "w") as O:
    #       O.write(lE)
    #       return f"archived base/{fn}.json -> archived/{fn}.json"
    
    # @staticmethod
    # def unarchive(fn):
    #   with open(f"archived/{fn}.json", "r") as E:
    #     lE = json.load(E)
    #     with open(f'base/{fn}.json' "w") as O:
    #       O.write(lE)
    #       return f"unarchived archived/{fn}.json -> base/{fn}.json"