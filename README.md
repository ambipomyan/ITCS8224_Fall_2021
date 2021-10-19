# ITCS8224_Fall_2021
Medical Image Segmentation

## References
[This link is a report for DL model](https://crfm.stanford.edu/report.html)
Section 2.2 provides CV related information

[This link is the paper for ATTENTION](https://arxiv.org/abs/1706.03762)


## TODOs
1. Collect related work for transformers/attention-based network
2. Apply optimization

## Notes
1. The location information is simplified at mean time lost
2. Parallism for decoder part is impossible because of the dependency

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
