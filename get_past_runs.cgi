#!/usr/local/bin/python3

import cgi, json
import sys
import os

from src.save_to_db import Saver

def main():
    try:
        print("Content-Type: application/json\n\n")

        form = cgi.FieldStorage()
        user_email = form.getvalue('user_email')

        svr = Saver()
        results = svr.get_user_jobs(user_email)
        print(json.dumps(results))
    except Exception as e:
        print(str(e))

if __name__ == '__main__':
    main()
