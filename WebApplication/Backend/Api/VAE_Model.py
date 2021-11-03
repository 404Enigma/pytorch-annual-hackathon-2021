import torch.nn as nn
import torch as th
import torch.nn.functional as F


class Reshape(nn.Module):
    def __init__(self, *args):
        super().__init__()
        self.shape = args

    def forward(self, x):
        return x.view(self.shape)


class Mod2(nn.Module):
  def __init__(self):
    super(Mod2,self).__init__()
    self.lay1 = nn.Conv2d(3,32,3,2,1)
    self.lay2 = nn.Conv2d(32,64,3,2,1)
    self.lay3 = nn.Conv2d(64,128,3,1,0)#53.0 44.0

    self.mean = nn.Linear(128*53*44,128)
    self.log_var = nn.Linear(128*53*44,128)
    
    self.decFCL = nn.Linear(128,128*53*44)
    self.declay2 = nn.ConvTranspose2d(128,64,3,1,0)
    self.declay1 = nn.ConvTranspose2d(64,32,3,2,1)
    self.declay0 = nn.ConvTranspose2d(32,3,3,2,1)


  def encoder(self,x):

    x = F.leaky_relu(self.lay1(x))
    x = F.leaky_relu(self.lay2(x))
    x = F.leaky_relu(self.lay3(x))
    x = x.view(-1,128*53*44)
    mu = self.mean(x)
    logvar = self.log_var(x)
    return mu,logvar

  def reparameterize(self, mu, logVar):
    std = th.exp(logVar/2)
    eps = th.randn_like(std)
    return mu + std * eps


  def decoder(self,x):
    x = F.leaky_relu(self.decFCL(x))
    x = x.view(-1,128,53,44)
    x = F.leaky_relu(self.declay2(x))
    x = F.leaky_relu(self.declay1(x))
    #x = F.pad(x,(0,0,2,0))
    x = F.leaky_relu(self.declay0(x))
    x = F.sigmoid(x)
    return x



  def forward(self,x):
    mu,logvar = self.encoder(x)
    z = self.reparameterize(mu,logvar)
    out = self.decoder(z)
    return out,mu,logvar

