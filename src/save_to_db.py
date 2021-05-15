import cgi, json
import os
import mysql.connector

class Saver:

    def __init__(self):
        self.conn = mysql.connector.connect(
            user="mchavez8",
			password="mchavez8mysql123",
			host="localhost",
			database="mchavez8_chado"
		)
        self.curs = self.conn.cursor()

    def __del__(self):
        self.conn.commit()
        self.conn.close()
    
    def save_run(self, run_id, email, seq_name, seq):
        qry = """
          INSERT INTO user_run VALUES (
            %s, %s, %s, %s
          )
        """
        self.curs.execute(
            qry,
            [run_id, email, seq_name, seq]
        )

    def save_sequence_results(self, run_id, vadr_status, seq_length, model_used):
        qry = """
            INSERT INTO sequence_results
                (run_id, vadr_status, seq_length, model_used) 
            VALUES (
                %s, %s, %s, %s
            )
        """
        self.curs.execute(
            qry,
            [run_id, vadr_status, seq_length, model_used]
        )

    def save_sequence_annotations(self, run_id, annotations_list):
        qry = """
            INSERT INTO sequence_features
                (run_id, feature_type, feature_name, feature_start, feature_end, seq_coords, alerts)
            VALUES 
        """
        annotation_as_sql = []
        for item in annotations_list:
            item_as_str = f'({run_id}, \"{item.get("type")}\", \"{item.get("name")}\", {item.get("start")}, {item.get("end")}, \"{item.get("seq_coords")}\", \"{item.get("alerts")}\")'
            annotation_as_sql.append(item_as_str)
        qry = qry + ",".join(annotation_as_sql)
        self.curs.execute(qry)
    
    def get_user_jobs(self, user_email):
        user_email = user_email.replace("@", "%40")
        qry = """
            SELECT * FROM user_run INNER JOIN sequence_results ON user_run.run_id=sequence_results.run_id
            WHERE user_user_email=%s;
        """
        self.curs.execute(
            qry,
            [user_email]
        )
        results = {
            "email": user_email,
            "past_jobs": []
        }
        for item in self.curs:
            results["past_jobs"].append(
                {
                    "id": item[0],
                    "seq_name": item[2],
                    "sequence": item[3],
                    "sequence_length": item[7],
                    "vadr_status": item[6]
                }
            )
        return results



if __name__ == "__main__":
    svr = Saver()
    # run_id = 8
    # svr.save_run(run_id, "test_usr", "test_name", "test_seq")
    # svr.save_sequence_results(run_id, "stat", 20, "mod")
    # svr.save_sequence_annotations(run_id,
    #     [{'type': 'gene', 'name': 'ORF1ab', 'start': '266', 'end': '21555', 'seq_coords': '266..21555:+', 'alerts': '-'}]
    # )
    svr.get_user_jobs("mauro.antoine.chavez%40gmail.com")