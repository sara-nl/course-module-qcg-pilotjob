#!/bin/bash
#SBATCH --nodes=1
#SBATCH --ntasks=16
#SBATCH --time=01:00:00
#SBATCH --partition=rome
module load 2022
module load QCG-PilotJob/0.13.1-foss-2022a

# copy input data and scripts to working directory
cp -r $SLURM_SUBMIT_DIR/. $TMPDIR/
cd $TMPDIR

# execute jobs
python3 qcg_job.py

# copy result back to submission directory
mkdir -p $SLURM_SUBMIT_DIR/results
cp result.csv  $SLURM_SUBMIT_DIR/results/

# archive the logdata for the reference
tar -c --exclude="input" --exclude="result" . > $SLURM_SUBMIT_DIR/results/log.${SLURM_JOB_ID}.tar
gzip $SLURM_SUBMIT_DIR/results/log.${SLURM_JOB_ID}.tar



