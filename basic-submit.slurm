#!/bin/bash

#SBATCH --job-name=DCGAN
#SBATCH --partition=Leo
#SBATCH --time=24:00:00
#SBATCH --mem=64GB
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=8
#SBATCH --gres=gpu:1

# Load python distribution and CUDA
module load anaconda3/2020.11
module load cuda/11.2

# Activate local venv
conda activate py36
echo $CONDA_DEFAULT_ENV

# Bash command to run python script
python -m DCGAN.py
