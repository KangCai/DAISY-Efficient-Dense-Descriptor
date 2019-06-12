# DAISY-Efficient-Dense-Descriptor

[English](https://github.com/KangCai/DAISY-Efficient-Dense-Descriptor/blob/master/README.md)

很高兴你发现了这个项目，该项目是一个论文方法实现工程，原论文是 "DAISY: An Efficient Dense Descriptor Applied
to Wide-Baseline Stereo"。欢迎提出任何意见或建议。

---

### 原文概述

本文介绍了一种局部图像描述子，名叫 DAISY，能有效地进行密集计算。本文还提供了一种从**宽基线**图像对计算**密集深度**和**遮挡地图**的 EM 算法。
在宽基线应用场景下，DAISY 表现效果明显优于在窄基线场景中使用的常用算法。此外，使用 DAISY 使得我们的算法对多光照和几何变换具有鲁棒性。
DAISY 设计的灵感来源于早期的一些描述子，比如 SIFT 和 GLOH，但比它们计算速度都快的多；然而又不像 SURF（一种基于 SIFT 的高效改进算法），
不会因为引入了 artifacts 而降低匹配效果。值得注意的是，DAISY 是第一个尝试从宽基线图像对来估计密集深度图的算法，而且证明了 DAISY 在深度估计准确率、
遮挡检测、还有与其它激光扫描真实场景应用中其它描述子的对比上，是一个表现不错的描述子。本文还在多个不同光照和几何变换的室内室外场景下对 DAISY 进行测试，
结果表明 DAISY 对这些场景的不同具有鲁棒性。

---

### 算法流程

**1. 计算每个像素的一维梯度，进而计算梯度方向、幅度，并统计它对不同方向的贡献（权重占比）**

<img src="https://raw.githubusercontent.com/KangCai/DAISY-Efficient-Dense-Descriptor/master/images/doc/1.png"/>

**2. 计算每个像素以该像素为中心的，高斯卷积核平滑后的，作为不同层（中心、内、中、外）上、对不同方向的贡献**

**3. 对某一个像素，统计其周边不同层、不同方向上的直方图特征，假设维度为 D；**

**4. 以固定步长采样的方式获取前述 P 个点；总数据量为 P * D**

---

### 特征效果

特征提取过程中，产生的中间图像如下组图所示，



