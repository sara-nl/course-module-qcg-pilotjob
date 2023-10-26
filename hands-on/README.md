# Hands-on QCG Pilotjob
Guide for the hands-on exercises

## Structure of QCG pilot jobs on Snellius
QCGPilot jobs on Snellius require 3 sets of files.
    1. **Slurm job Script** &rarr; Loads the QCG environment and runs the QCG
       python script.
    2. **QCG python script** &rarr; Invokes job manager that aggregates all
       your jobs along with resources, conditions based on which jobs need to
       be invoked.
    3. **Executable** &rarr; This is the main application that one wants to
       invoke.

Flow of invoking: *Slurm job Script*&rarr;*QCG python script*&rarr;*Executable*

This is the order in which the executable ultimately gets invoked.

The job script allocates the total resources that you want to allocate for your
job. This also loads the QCGPilot module and other modules required within the
node. Please note that within Snellius the environment in the login nodes does
not get transferred by defaultto the allocated compute nodes. You will have to
load the modules again within the Slurm job script. The job script also moves
the necessary files needed for the execution from the home file system to the
scratch file system and once the calculations are complete, copies the relevant
files back to the submit directory. This is also very essential since, your
home filesystem is only meant for storage, the I/O on the compute nodes need to
occur within the scratch file system which is a part of the GPFS (General
Parallel File System).

QCG python script invokes a job manager within the Slurm allocation. This
manager manages your multiple small jobs based on the resources provided to it.
This script mainly assimilates the different jobs along with different
parameters that you need to provide for the embarrassingly parallel
workflow. Parameters can be different input arguments that you provide to the
same end application executable. Each job will produce its, own output and
error file and can also include its own unique modules that are extra on top of
general modules that are already loaded.

The status of each job can be found in the file named
*nl-agent-{hostname}.log*. For more detailed diagnostics and explanation
regarding each job and also the available logs please refer to the
[documentation](https://qcg-pilotjob.readthedocs.io/en/develop/logs.html).
