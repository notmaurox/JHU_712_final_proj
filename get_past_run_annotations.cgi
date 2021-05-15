#!/usr/local/bin/python3

import cgi, json
import sys
import os

from src.save_to_db import Saver

def main():
    try:
        print("Content-Type: application/json\n\n")

        form = cgi.FieldStorage()
        run_id = form.getvalue('run_id')

        svr = Saver()
        results = svr.get_past_run_annotations(run_id)
        print(json.dumps(results))
    except Exception as e:
        print(str(e))

if __name__ == '__main__':
    main()
