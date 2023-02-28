# 后面有torch.geometric了 这是简单的模型
import math
import torch
from torch import nn

class GraphConvolution(nn.Module):
    def __int__(self, in_features, out_features, bias=True):
        super(GraphConvolution,self).__init__()
        
        self.in_features=in_features
        self.out_features=out_features
        self.weight=nn.Parameter(torch.FloatTensor(in_features,out_features))
        if bias:
            self.bias=nn.Parameter(torch.FlaotTensor(out_features))
        else:
            self.register_parameter('bias',None)
        self.reset_parameters()

    def reset_parameters(self):
        # “uniform() 方法将随机生成下一个实数,它在 [x, y] 范围内
        stdv=1./math.sqrt(self.weight.size[1])
        self.weight.data.uniform_(-stdv,stdv)
        if self.bias is not None:
            self.bias.data.uniform_(-stdv,stdv)

    def forward(self,input,adj):
        h=input@self.weight
        output=torch.spmm(adj,h)
        if self.bias is not None:
            return output + self.bias
        else:
            return output
    
    def __