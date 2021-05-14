#!/usr/local/bin/python3

import cgi, json
import sys
import os
import mysql.connector
from src.micro_vadr_connect import MicroVaderConnect

def main():
    print("Content-Type: application/json\n\n")

    form = cgi.FieldStorage()
    job_id = form.getvalue('job_id')

    mvc = MicroVaderConnect(
        """
        this literally doesnt matter I am just doing this bc I couldnt get 
        fucking ajax to wait for my python script to finish before moving
        on so I had to split the microservice interactions with seperate calls
        instead of just waiting for the job to finish before continuing on with
        the ajax sucess body
        """,
        "see above"
    )
    mvc.job_id = job_id
    mvc.get_results()

    if mvc.results:
        results = {
            "job_id": str(job_id),
            "vadr_status": mvc.results.get("VADR_status", "JOB NOT FINISHED"),
            "seq_length": mvc.results.get("seq_length", "JOB NOT FINISHED"),
            "model_used": mvc.results.get("model_used", "JOB NOT FINISHED"),
            "sequence_features": mvc.results.get("sequence_features", [])
        }
    else:
        results = {
            "job_id": str(job_id),
            "vadr_status": "JOB NOT FINISHED (please wait 10 more seconds and check status again)",
            "seq_length": "-",
            "model_used": "-",
            "sequence_features": []
        }

    print(json.dumps(results))

if __name__ == '__main__':
    main()
