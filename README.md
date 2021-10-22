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
1. Adapt transformer from NLP to CV: The inputs include linear projection of image patches and their location information; Usually, the location information is simplified to (fairly small) constant
2. Computation complexity: The complexity of self-attention computation is considered as O(n^2); Window-based self-attention is now popular, e.g. Swin-Transformer/Focal-Transformer
3. Parallism of training: Dependency of decoder part needs to be handled; For now force teaching and masking are most common solutions
4. Convergency of training: Vanishing gradient is handled by skip-connection; e.g. conv and conv(upsampling) are usually connected with skip-connection in U-net

## Related work
1. [transBTS](https://arxiv.org/abs/2103.04430): conv - encoder(MSA+FFN) - conv(upsampling)
2. [transUnet](https://arxiv.org/abs/2102.04306): conv - encoder(MSA+MLP) - conv(upsampling)
3. [MedT](https://arxiv.org/abs/2102.10662): conv - Global/Local encoder(Gated\_MSA\_height+Gated\_MSA\_width) - Global/Local decoder - 1x1conv
4. [SpecTr](https://arxiv.org/abs/2103.03604): conv - encoder(MSA+MLP) - conv(upsampling)
5. [U-net transformer](https://arxiv.org/abs/2103.06104): conv - MSA - conv(upsample, with Multihead\_Cross\_Attention)
6. [UNETR](https://arxiv.org/abs/2103.10504): encoder - decoder
7. [Swin-Unet](https://arxiv.org/abs/2105.05537): encoder(Swin-transformer-block+merging) - bottleneck(2xSwin-transformer-blocks) - decoder(expanding+Swin-transformer-block)  
*Swin-transformer-block: Window\_based-MSA+MLP
8. [DS-TransUnet](https://arxiv.org/abs/2106.06716): encoder(Swin-transformer-block+merging) - TIF as skip-connections - decoder(upsampling+Swin-transformer-block)  
\*TIF: feature fusion among small and large scale patched images
9. [UTnet](https://arxiv.org/abs/2107.00781): encoder(MSA+conv) - decoder
10. [PNS-Net](https://arxiv.org/abs/2105.08468): encoder - Normalize\_Self-attention\_block - decoder
11. [Focal Transformer](https://arxiv.org/abs/2107.00641): encoder(patch\_embedding+MLP+FSA)  
\*FSA: Focal Self-Attention, applying location-based self-attention, also use window-based approach
12. [DOLG and hybrid-Swin-transformer](https://arxiv.org/abs/2110.03786): 1) conv - orthogonal\_fusion 2) conv - Swin-transformer
13. [HRFormer](https://arxiv.org/abs/2110.09408): conv - multi-revolution-HRT - conv/conv(upsampling) - multi-revolution-HRT - conv  
\*HRT: High Resolution Transformer, MSA+FFN

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
