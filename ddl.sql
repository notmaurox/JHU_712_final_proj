mysql -u mchavez8 -h localhost -p

SET PASSWORD FOR 'mchavez8'@'localhost' = 'mchavez8mysql123';

CREATE TABLE user_run(
    run_id INT PRIMARY KEY NOT NULL,
    user_user_email VARCHAR(120) NOT NULL,
    sequence_name VARCHAR(300) NOT NULL,
    sequence_DNA VARCHAR(50000) NOT NULL,
)

CREATE TABLE sequence_features(
    feature_id INT PRIMARY KEY NOT NULL,
    run_id INT NOT NULL,
    feature_type VARCHAR(200) NOT NULL,
    feature_name VARCHAR(200),
    feature_start INT NOT NULL,
    feature_end INT NOT NULL,
    seq_coords VARCHAR(120) NOT NULL,
    alerts VARCHAR(700) NOT NULL,
    FOREIGN KEY (run_id) REFERENCES user_run (run_id)
        ON DELETE CASCADE ON UPDATE CASCADE
)

CREATE TABLE sequence_results(
    feature_id INT PRIMARY KEY NOT NULL,
    run_id INT NOT NULL,
    vadr_status VARCHAR(10) NOT NULL,
    seq_length INT NOT NULL,
    model_used VARCHAR(50) NOT NULL,
    FOREIGN KEY (run_id) REFERENCES user_run (run_id)
        ON DELETE CASCADE ON UPDATE CASCADE
)