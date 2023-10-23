#!/bin/bash
#SBATCH --nodes=2
#SBATCH --ntasks-per-node=128
#SBATCH --time=00:05:00
#SBATCH --partition=rome
module load 2022
module load QCG-PilotJob/0.13.1-foss-2022a

python3 qcg_job.py

