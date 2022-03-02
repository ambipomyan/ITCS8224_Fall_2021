# ITCS8224_Fall_2021
Medical Image Segmentation

## Demo
This demo is created following the idea of [MMDetection](https://github.com/open-mmlab/mmdetection), which is a python pakage for Object-Detection. It contains various network frames including Swin-Transformer related ones, and I think it is a good and down-to-earth start.

### Envoronment
The prerequisites are:

Linux or macOS (Windows is in experimental support)  
Python 3.6+  
PyTorch 1.3+  
CUDA 9.2+ (If you build PyTorch from source, CUDA 9.0 is also compatible)  
GCC 5+  
MMCV

The environment is handled by conda, as usual, and ```conda update -n base -c defaults conda``` may be needed. For the sever, do only need these steps:
```
conda create -n openmmlab python=3.7 -y
conda activate openmmlab
conda install pytorch torchvision -c pytorch
pip install openmim
mim install mmdet
```

### Run
The transformer related network needs pretrained model, for its slow convergency. In this case, the pre-trained dataset is [COCO](https://cocodataset.org/#home).

```
python demo/image_demo.py \
demo/demo.jpg \
configs/faster_rcnn/faster_rcnn_r50_fpn_1x_coco.py \
checkpoints/faster_rcnn_r50_fpn_1x_coco_20200130-047c8118.pth \
--device cpu
```

### Result
This pre-trained model does not use data containing any classes related to tumors or brain, then the label is not correct. The original image is from [Wiki](https://en.wikipedia.org/wiki/Brain_tumor).

![](/demo/result.jpg)

## Notes
1. Adapt transformer from NLP to CV: The inputs include linear projection of image patches and their location information; Usually, the location information is simplified to (fairly small) constant
2. Computation complexity: The complexity of self-attention computation is considered as O(n^2); Window-based self-attention is now popular, e.g. Swin-Transformer/Focal-Transformer
3. Parallism of training: Dependency of decoder part needs to be handled; For now force teaching and masking are most common solutions
4. Convergency of training: Vanishing gradient is handled by skip-connection; e.g. conv and conv(upsampling) are usually connected with skip-connection in U-net
5. Adapt classes of pre-trained models to transformer model, e.g. from cake to tumor/from clock to brain...
6. Use smooth edges for segmented parts
7. Using multi-modal data

## Topics
[This link is a report for DL model](https://crfm.stanford.edu/report.html)  
[This link is the paper for ATTENTION](https://arxiv.org/abs/1706.03762)  
[This link is the Get Started Doc. of MMDetection](https://mmdetection.readthedocs.io/en/v2.19.0/get_started.html)

## TODOs
1. Collect related work for transformers/attention-based network
2. Apply optimization

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
\*HRT: High Resolution Transformer, MSA+FFN, using Local-window Self-Attention

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

## MNIST-3D-pkl
Code for transfering .jpg data to a 3D pkl
