# ITCS8224_Fall_2021
Medical Image Segmentation

## References
[This link is a report for DL model](https://crfm.stanford.edu/report.html) 

1. Section 2.2 provides CV related information
2. Section 3.1 provides Health related information

## Topic
[This link is the paper for ATTENTION](https://arxiv.org/abs/1706.03762)

## TODOs
1. Collect related work for transformers/attention-based network
2. Apply optimization

## Notes
1. Adapt transformer from NLP to CV: The inputs include linear projection of image patches and their location information; The location information is simplified to (fairly small) constants
3. Parallism of model training: Dependency of decoder part needs to be handled; For now force teaching and masking are most common solutions

## Related work


## Source for this course

#### Python envs
environment and data path: 
```/projects/biomedimaging/```

src:
```/BraTS2021```

#### Submit job to cluster
```
sbatch submit.slurm
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
