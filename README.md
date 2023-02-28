# PyTorch安装指令
请先安装Anaconda和CUDA 10.0。

- 配置国内源

```python
# 配置国内源，方便安装Numpy,Matplotlib等
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main/
# 配置国内源，安装PyTorch用
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/pytorch/
# 显示源地址
conda config --set show_channel_urls yes
```

- 安装PyTorch
```python
# 安装PyTorch，要使用国内源请去掉-c pytorch这个参数！！
conda install pytorch torchvision cudatoolkit=10.0

```

- 安装常用库

```python
pip install numpy matplotlib pillow pandas
```

# 课程链接

<!--  
<p align="center">
  <a href="https://study.163.com/course/courseMain.htm?share=2&shareId=480000001847407&courseId=1208894818&_trace_c_p_k2_=61a9e0a511f7409b92a08d4f4c964330
">
    <img src="res/ad_banner.png">
  </a>
</p> 
 -->
**课程链接:** https://study.163.com/course/courseMain.htm?share=2&shareId=480000001847407&courseId=1208894818&_trace_c_p_k2_=61a9e0a511f7409b92a08d4f4c964330

<p align="center">
  <img width="700"  src="res/版权声明.png">
</p> 


**课程大纲:**
![课程介绍](res/outline.png)



# 计划
好多之前学了，但是不全，主要自己挑着模仿代码，代码不熟，理论基本都了解，也会,这个讲的也没有很好;
实践过程中最好看pytorch官方的说明tutorial/docs



- [x] 回归问题 lesson3-5 2023.2.14

- [x] pytorch基础 lesson6-14 

  2023.2.25 6-8 1h 

  2023.2.26 9 0.5h; 6-9整理笔记1h 10-13 下午2.5h

- [x] SGD随机梯度下降 lesson16-22 

  2023.2.27 13  14一边打一边记笔记; 推导部分跳着看 22太老了 都不对了

- [x] 神经网络 lesson24-29

- [x] 测试与可视化 lesson30

- [x] 过拟合lesson31-35

- [x] CNN 37-45

- [x] RNN 46-53 cNN rnn都跳了 没仔细看 因为在 nlp-tutorial里面看过了

- [ ] auto-encoder 54-55

- [ ] GAN 56-56

- [ ] 拓展 GCN 58 63

**attention,transformer那块看nlp-tutorial!!  这下基本上所有基础模型都练习过,后面用到再细扒!!!!**
