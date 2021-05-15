#!/usr/local/bin/python3

import cgi, json
import sys
import os

from src.micro_vadr_connect import MicroVaderConnect
from src.save_to_db import Saver

def main():
    try:
        print("Content-Type: application/json\n\n")

        content_len = int(os.environ["CONTENT_LENGTH"])
        req_body = sys.stdin.read(content_len)
        my_dict = json.loads(req_body)

        user_email = my_dict["param"]["user_email"].replace("user_email=","")
        sequence_name = my_dict["param"]["seq_name"].replace("sequence_name=","")
        sequence = my_dict["param"]["seq"].replace("sequence_dna=","")

        mvc = MicroVaderConnect(
            sequence_name,
            sequence
        )
        mvc.submit_sequence()

        svr = Saver()
        svr.save_run(mvc.job_id, user_email, sequence_name, sequence)

        results = {
            "user_email": user_email,
            "job_id": str(mvc.job_id),
        }
        print(json.dumps(results))
    except Exception as e:
        print(str(e))

if __name__ == '__main__':
    main()
