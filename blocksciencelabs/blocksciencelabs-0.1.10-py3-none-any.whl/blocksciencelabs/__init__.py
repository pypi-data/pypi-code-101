import client
import common

import pandas as pd
import functools, pickle, operator

def fetch_results(simulation_id, conn):
  select_jobs = f"SELECT * FROM job WHERE simulation_id = {simulation_id};"

  jobs = pd.read_sql_query(select_jobs, conn)

  select_job_results = f"SELECT * FROM job_result WHERE job_id IN ({jobs.to_numpy()});"

  job_results = pd.read_sql_query(select_job_results, conn)

  serialized_results = job_results['data'] \
      .transform(lambda x:  pickle.loads(bytes.fromhex(x))) \
      .to_list()

  results = pd.DataFrame(functools.reduce(operator.iconcat, serialized_results, []))

  return results