from glob import glob
import os
from qcg.pilotjob.api.job import Jobs
from qcg.pilotjob.api.manager import LocalManager

job_names = []

# scan input directory for CVS files
for filename in glob(os.path.join("input/*.csv"), recursive = False):
    # determine the job name and append it to the list
    job_names.append(os.path.basename(filename))

# create the QCG manager
manager = LocalManager()
jobs = Jobs()
jobs_1 = Jobs()


for jname in job_names:
    # loop over all jobs
    print("submit {}".format(jname))
    jobs.add(name=jname,
             exec='python3',
             args=["average.py", os.path.join("input", jname)],
             stdout='average_{}'.format(jname),
             stderr='job.{}.err'.format(jname),
             modules=["2022", "Python/3.10.4-GCCcore-11.3.0"],
             iteration=1
             )

print("submit jobs")
job_ids = manager.submit(jobs)
print("wait for all jobs")
manager.wait4(job_ids)
job_status = manager.status(job_ids)
print("Job status ")
all_comp_finished = (all([job_status.get('jobs').get(x).get('data').get('status')=='SUCCEED'
                          for x in job_ids]) and
                     any([job_status.get('jobs').get(x).get('data').get('status')=='SUCCEED'
                          for x in job_ids]))

print("All computations finished = ", all_comp_finished)

# Execute the aggregate job if all computations finished correctly.
if(all_comp_finished):
    # aggregate results in one CSV file
    jobs_1.add(name="aggregate",
               script='cat average_*.csv | sort',
               stdout='result.csv',
               stderr='aggregate.err',
               after=job_names)
    print("submit jobs aggregate")
    manager.submit(jobs_1)
else:
    print("Not all jobs have finished correctly, therefore aggregate will not be calculated.")

print("wait for all jobs")
manager.wait4all()
print("done")
manager.finish()
print("finished")
