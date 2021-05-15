#!/usr/local/bin/python3

import cgi, json
import sys
import os

from src.micro_vadr_connect import MicroVaderConnect
from src.save_to_db import Saver

def main():
    try:
        print("Content-Type: application/json\n\n")

        form = cgi.FieldStorage()
        job_id = form.getvalue('job_id')

        mvc = MicroVaderConnect(
            """
            N/A, all that's needed for this is a job ID as sequence was submitted
            previously via web page
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
            svr = Saver()
            svr.save_sequence_results(
                mvc.job_id,
                results["vadr_status"],
                int(results["seq_length"]),
                results["model_used"]
            )
            svr.save_sequence_annotations(
                mvc.job_id,
                mvc.results.get("sequence_features", [])
            )

        else:
            results = {
                "job_id": str(job_id),
                "vadr_status": "JOB NOT FINISHED (please wait 10 more seconds and check status again)",
                "seq_length": "-",
                "model_used": "-",
                "sequence_features": []
            }

        print(json.dumps(results))
    except Exception as e:
        print(str(e))

if __name__ == '__main__':
    main()
