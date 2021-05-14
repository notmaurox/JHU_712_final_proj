#!/usr/local/bin/python3

import cgi, json
import sys
import os
import mysql.connector
from src.micro_vadr_connect import MicroVaderConnect

def main():
    print("Content-Type: application/json\n\n")

    content_len = int(os.environ["CONTENT_LENGTH"])
    req_body = sys.stdin.read(content_len)
    my_dict = json.loads(req_body)

    user_email = my_dict["param"]["user"].replace("user_email=",""),
    sequence_name = my_dict["param"]["seq_name"].replace("sequence_name=",""),
    sequence = my_dict["param"]["seq"].replace("sequence_dna=",""),

    mvc = MicroVaderConnect(
        sequence_name[0],
        sequence[0]
    )

    mvc.submit_sequence()

    results = {
        "job_id": str(mvc.job_id),
        "vadr_status": str(mvc.job_id),
        "seq_length": str(mvc.job_id),
        "model_used": str(mvc.job_id)
    }

    print(json.dumps(results))


if __name__ == '__main__':
    main()
