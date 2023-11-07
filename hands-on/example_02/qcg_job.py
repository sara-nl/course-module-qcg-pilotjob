from glob import glob
import os
import sys
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

# aggregate results in one CSV file
jobs.add(name="aggregate",
         script='cat average_*.csv | sort',
         stdout='result.csv',
         stderr='aggregate.err',
         after=job_names)

print("-- submit jobs")
manager.submit(jobs)
print("-- wait for all jobs")
manager.wait4all()
print("-- done")
manager.finish()
print("-- finished")
