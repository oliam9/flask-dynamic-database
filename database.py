from sqlalchemy import create_engine, text
import os

db_connection_string = os.environ['DB_CONNECTION_STRING']

engine = create_engine(db_connection_string)

def load_jobs_from_db():
  with engine.connect() as conn:
      result = conn.execute(text("select * from jobs"))
      jobs = []
      for row in result.all():
          jobs.append(dict(row._mapping))
      return jobs

def load_job_from_db(id):
    with engine.connect() as conn:
        result = conn.execute(text("select * from jobs where id = :val"), {"val": id})
        rows = result.mappings().all()
        if len(rows) == 0:
            return None
        else:
            return dict(rows[0])

def add_application_to_db(job_id, data):
  with engine.connect() as conn:
    query = text("INSERT INTO applications (job_id, full_name, email, education, work_experience) VALUES (:job_id, :full_name, :email, :education, :work_experience)")
      
    conn.execute(query, 
                 job_id=job_id,
                 full_name=data['full_name'],
                 email=data['email'],
                 education=data['education'],
                 work_experience=data['work_experience'])