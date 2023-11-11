import torch.nn as nn

class NegModel(nn.Module):

    def __init__(self):
        super(NegModel, self).__init__()

    def forward(self, x):
        print(x.shape)
        return x
