# Average algorithm

Compute the average of one column in several CSV files. Aggregate the results in one output CSV file `results.csv`.

## Usage
1. Extract input data from the tarball
```shell
tar -xvf input.tar.gz
```

2. Submit the job
```shell
sbatch qcg_job.sh
```

3. Observe result in the `result` directory.

4. Look at the `qcg_job_v1.py` file. Can you spot a problem?

5. Compare `qcg_job_v1.py` to `qcg_job_v2.py` and `qcg_job_v3.py`


## Data source
https://www.ncdc.noaa.gov/ghcnd-data-access