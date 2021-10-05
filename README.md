# ITCS8224_Fall_2021
DCGAN optimization with skip-connection

## Get Start
#### Download and install anaconda3
```
curl -O https://repo.anaconda.com/archive/Anaconda3-2021.05-Linux-x86_64.sh
bash Anaconda3-2021.05-Linux-x86_64.sh
```
Use ```sorce ~/.bashrc``` to refresh then can use ```conda```

#### Use conda to install cuda(cudatoolkit) and tensorflow(tensorflow-gpu)
```
conda create -n py36 python=3.6
conda activate py36
conda install cudatoolkit
conda install tensorflow-gpu
```

### Run HelloWorld code
```
conda activate py36
python HelloWorld.py
conda deactivate
```

#### Submit job to cluster
```
sbatch basic-submit.slurm
```

Get msg:
```
Submitted batch job 1234567
```

Check status
```
squeue -j 1234567
```

```ST```=```PD``` indicates Pending

## Source for this course
environment: ```/projects/biomedimaging/biomedenv```

## Implementation ideas
Stack Res blocks to network
