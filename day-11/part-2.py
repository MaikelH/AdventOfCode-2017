import numpy as np

inputString = "s,sw,sw,nw,nw,nw,sw,s,ne,n,n,n,s,ne,ne,sw,ne,n,ne,nw,ne,sw,ne,nw,ne,ne,ne,nw,sw,se,ne,se,ne,ne,se,se,s,sw,se,se,se,ne,se,nw,ne,s,s,s,s,s,se,sw,sw,ne,s,sw,nw,s,s,s,s,s,s,s,sw,s,sw,s,sw,s,se,se,sw,s,s,sw,sw,s,s,s,s,sw,sw,sw,sw,s,s,sw,nw,sw,sw,sw,sw,n,se,sw,sw,sw,sw,sw,ne,sw,sw,ne,sw,sw,sw,sw,sw,sw,nw,sw,nw,nw,nw,sw,sw,sw,nw,s,sw,nw,nw,sw,nw,nw,nw,se,ne,sw,nw,nw,nw,s,ne,nw,nw,s,nw,nw,s,nw,nw,n,nw,nw,nw,nw,nw,nw,nw,n,nw,nw,n,nw,nw,sw,nw,se,nw,nw,nw,n,nw,nw,n,nw,nw,nw,n,s,nw,nw,nw,nw,n,nw,nw,n,ne,n,n,nw,n,n,n,nw,s,s,nw,n,nw,n,n,nw,se,n,nw,n,n,nw,nw,n,n,n,n,n,n,ne,n,n,n,n,ne,n,n,n,n,s,n,n,n,n,n,n,n,n,s,n,n,n,n,s,n,se,ne,se,nw,ne,n,n,ne,se,ne,n,nw,sw,n,n,ne,n,n,n,ne,n,se,nw,ne,ne,nw,n,n,ne,se,nw,ne,se,ne,ne,ne,se,n,sw,n,n,n,ne,ne,sw,n,n,sw,sw,ne,ne,ne,ne,n,s,ne,ne,n,s,se,ne,ne,ne,se,ne,ne,ne,ne,n,ne,n,n,ne,ne,ne,ne,ne,ne,s,s,ne,ne,n,ne,ne,ne,nw,ne,ne,ne,ne,s,ne,ne,ne,ne,se,se,ne,n,ne,se,ne,se,ne,ne,ne,ne,ne,ne,se,ne,nw,ne,s,n,ne,se,ne,ne,ne,ne,ne,se,se,se,n,nw,se,se,se,ne,se,ne,n,ne,nw,s,ne,ne,se,ne,se,ne,ne,se,se,nw,se,n,ne,se,se,se,se,nw,se,ne,nw,se,ne,se,se,se,ne,ne,ne,se,ne,ne,n,se,se,ne,se,se,s,ne,se,se,nw,ne,ne,se,ne,se,se,se,ne,sw,se,se,ne,se,se,sw,n,se,n,se,ne,se,ne,se,se,n,se,se,se,sw,ne,se,ne,se,se,se,se,sw,se,se,nw,se,n,se,se,se,se,se,n,se,se,se,se,se,se,se,se,se,sw,se,se,n,se,se,se,n,se,s,ne,se,se,ne,se,s,s,ne,n,se,se,se,ne,se,se,se,se,se,sw,s,s,se,se,ne,se,s,se,se,sw,se,se,s,s,se,sw,se,se,se,ne,se,s,n,ne,se,s,se,sw,s,n,ne,se,se,se,s,nw,n,s,se,se,se,se,ne,s,s,se,sw,nw,s,se,s,s,s,s,s,s,se,s,s,n,se,sw,se,se,s,se,se,se,s,s,se,s,se,s,sw,s,ne,s,se,s,s,se,s,se,s,s,s,s,s,se,ne,s,se,s,s,s,s,se,nw,se,se,se,se,se,s,s,ne,se,se,s,s,s,sw,s,s,se,s,s,se,ne,sw,s,sw,s,s,s,s,s,s,s,s,s,s,se,n,ne,s,s,s,s,s,se,s,se,s,s,ne,s,s,n,s,s,s,s,s,s,s,s,s,s,ne,s,s,se,s,s,s,nw,ne,s,sw,s,s,s,s,s,s,s,s,s,s,s,s,s,s,s,se,s,s,sw,s,s,s,n,s,se,se,s,s,s,s,ne,n,s,sw,s,s,sw,s,sw,nw,sw,sw,s,s,n,s,s,s,sw,s,s,s,sw,s,sw,s,nw,s,sw,s,sw,s,s,sw,s,ne,s,s,s,s,sw,nw,s,n,sw,sw,s,s,nw,s,s,sw,n,s,sw,sw,s,s,se,s,sw,s,sw,s,s,s,s,sw,sw,n,s,sw,sw,nw,s,s,nw,s,s,sw,s,s,s,s,nw,ne,s,sw,s,s,s,sw,s,s,s,se,sw,s,sw,s,sw,sw,sw,sw,sw,sw,s,sw,sw,nw,s,sw,sw,nw,s,s,ne,s,s,s,ne,s,sw,sw,s,sw,s,s,s,sw,sw,s,nw,sw,sw,s,sw,sw,sw,s,s,sw,s,sw,sw,sw,s,s,s,se,s,s,sw,sw,s,sw,sw,sw,nw,sw,sw,s,sw,sw,sw,nw,sw,sw,nw,s,s,sw,s,s,sw,sw,sw,sw,sw,sw,nw,s,sw,sw,sw,ne,sw,sw,s,sw,sw,sw,sw,sw,s,sw,s,sw,sw,sw,n,s,sw,sw,s,sw,ne,s,s,sw,s,s,se,sw,sw,sw,sw,nw,s,s,sw,s,sw,sw,sw,s,sw,se,sw,s,sw,sw,sw,sw,sw,nw,sw,sw,sw,s,nw,sw,sw,sw,s,ne,sw,nw,sw,s,sw,se,se,sw,sw,sw,sw,sw,sw,sw,nw,n,sw,sw,se,sw,sw,sw,sw,sw,sw,sw,sw,sw,sw,sw,sw,s,sw,sw,sw,sw,sw,sw,sw,sw,s,sw,sw,sw,sw,sw,nw,sw,nw,sw,sw,sw,sw,sw,sw,se,sw,sw,sw,nw,sw,sw,n,sw,sw,sw,nw,sw,sw,ne,ne,nw,nw,sw,nw,sw,sw,se,nw,s,sw,n,sw,sw,sw,se,sw,s,nw,sw,n,nw,sw,sw,n,nw,sw,sw,nw,nw,sw,sw,s,sw,sw,nw,sw,sw,sw,n,ne,s,ne,sw,sw,sw,sw,sw,s,sw,nw,sw,sw,sw,nw,sw,se,sw,nw,sw,nw,sw,nw,sw,nw,s,sw,sw,sw,s,sw,n,nw,n,nw,sw,nw,s,ne,nw,sw,se,sw,sw,sw,ne,sw,sw,nw,sw,ne,sw,nw,sw,sw,sw,nw,sw,nw,sw,sw,nw,nw,n,n,nw,sw,sw,nw,sw,s,sw,nw,nw,s,nw,sw,nw,sw,sw,nw,nw,nw,nw,nw,nw,se,se,sw,nw,s,s,s,nw,sw,nw,nw,sw,sw,sw,sw,nw,s,nw,se,s,nw,sw,sw,nw,n,nw,sw,sw,sw,nw,ne,se,nw,nw,sw,nw,sw,nw,ne,nw,sw,nw,sw,nw,nw,sw,nw,sw,ne,nw,nw,sw,nw,nw,sw,sw,sw,se,sw,nw,nw,sw,nw,nw,s,nw,sw,s,nw,s,nw,nw,sw,nw,nw,nw,sw,nw,sw,se,s,ne,nw,sw,s,ne,nw,sw,nw,nw,nw,se,sw,sw,sw,sw,nw,nw,nw,nw,nw,nw,nw,sw,sw,nw,nw,sw,nw,sw,s,nw,nw,nw,nw,nw,nw,sw,nw,sw,sw,sw,sw,sw,nw,nw,nw,nw,nw,nw,nw,nw,ne,nw,se,nw,nw,nw,nw,nw,nw,ne,s,nw,sw,sw,s,ne,sw,n,nw,ne,ne,nw,nw,nw,sw,sw,nw,nw,n,sw,nw,nw,nw,nw,ne,n,se,s,nw,nw,sw,n,n,sw,nw,nw,nw,nw,nw,nw,ne,nw,se,nw,nw,nw,nw,se,s,nw,sw,sw,ne,ne,nw,nw,se,n,se,nw,nw,n,nw,nw,nw,nw,nw,nw,nw,nw,nw,nw,nw,nw,nw,nw,n,ne,nw,nw,nw,n,nw,n,nw,nw,nw,nw,nw,nw,n,nw,nw,s,nw,nw,sw,nw,nw,nw,nw,nw,sw,nw,nw,nw,nw,nw,nw,nw,nw,nw,nw,n,s,nw,nw,nw,nw,nw,nw,nw,s,nw,nw,nw,nw,s,nw,nw,ne,nw,nw,nw,s,se,s,se,se,nw,nw,nw,nw,nw,nw,nw,nw,nw,n,nw,nw,n,nw,nw,nw,nw,n,sw,nw,ne,n,nw,nw,nw,ne,nw,nw,nw,nw,nw,nw,se,n,nw,nw,nw,nw,nw,nw,se,se,nw,n,nw,s,ne,nw,ne,nw,sw,n,sw,n,nw,nw,nw,ne,s,nw,nw,se,nw,nw,nw,nw,n,sw,nw,nw,nw,s,n,ne,nw,nw,nw,nw,nw,nw,nw,s,nw,ne,ne,nw,nw,nw,sw,s,nw,nw,nw,n,n,nw,n,nw,n,ne,ne,s,n,n,s,nw,n,sw,nw,nw,s,nw,nw,n,s,ne,n,n,n,nw,nw,n,se,nw,se,n,n,n,nw,nw,nw,nw,nw,nw,ne,nw,nw,ne,n,n,se,n,nw,n,n,ne,s,sw,nw,se,n,n,nw,n,sw,n,nw,se,n,nw,n,n,nw,nw,nw,s,nw,n,nw,nw,nw,se,n,n,nw,nw,se,nw,nw,nw,n,ne,sw,n,nw,nw,n,nw,sw,nw,nw,n,nw,s,n,nw,n,nw,nw,n,nw,n,ne,nw,n,n,se,nw,n,nw,nw,n,n,nw,n,s,se,nw,nw,n,nw,nw,n,nw,n,n,n,nw,n,n,nw,n,nw,n,nw,nw,se,nw,n,sw,nw,se,n,s,n,nw,nw,sw,n,n,s,n,s,nw,ne,n,n,n,n,n,nw,nw,nw,nw,se,nw,nw,n,s,n,n,se,nw,n,n,n,nw,n,nw,ne,s,nw,ne,nw,nw,se,nw,n,n,n,sw,n,n,n,nw,n,n,sw,n,n,n,n,n,n,n,nw,sw,n,n,se,n,nw,nw,nw,s,n,ne,n,n,n,nw,se,n,s,n,ne,nw,n,n,n,n,n,n,n,nw,n,nw,nw,nw,n,n,nw,nw,n,n,n,se,nw,n,n,se,nw,n,n,nw,n,nw,n,n,n,nw,s,se,n,n,n,n,n,ne,n,n,nw,n,nw,nw,nw,n,s,nw,n,n,n,n,sw,n,n,n,n,n,n,nw,n,n,n,ne,n,nw,n,nw,sw,n,n,n,n,n,se,n,n,n,n,n,n,n,s,nw,nw,n,n,nw,n,n,sw,nw,n,n,nw,n,n,n,nw,n,s,nw,nw,se,n,n,n,n,n,n,n,n,n,n,n,s,s,n,n,ne,ne,n,n,n,n,n,se,nw,n,nw,n,n,n,n,n,n,sw,s,nw,n,se,n,n,n,n,n,n,n,n,sw,n,n,n,se,n,n,s,n,n,n,sw,n,n,ne,n,n,n,n,n,n,n,n,n,sw,nw,n,n,n,n,sw,sw,n,n,n,n,ne,n,sw,nw,n,n,s,n,n,nw,n,n,n,n,nw,n,n,n,n,s,n,n,n,n,n,n,n,ne,n,n,n,n,n,s,s,n,n,ne,n,n,n,n,s,nw,ne,nw,nw,n,n,n,n,n,n,ne,n,nw,ne,n,n,n,s,n,n,ne,n,n,n,ne,n,n,n,n,n,ne,se,n,s,n,n,n,n,n,se,se,n,n,ne,nw,n,n,n,n,n,n,n,n,n,n,n,n,s,n,n,ne,ne,n,s,sw,n,n,n,n,ne,n,ne,ne,nw,n,n,n,ne,n,sw,ne,n,ne,n,nw,ne,n,n,n,sw,s,n,n,n,ne,se,n,n,n,n,n,n,sw,n,sw,sw,n,n,ne,n,se,ne,s,sw,n,ne,n,ne,n,ne,n,n,n,ne,ne,n,n,n,nw,ne,n,n,sw,n,ne,n,n,n,n,n,ne,ne,n,n,n,n,n,ne,s,sw,ne,n,n,n,n,n,n,n,ne,n,n,ne,s,ne,ne,sw,ne,n,s,n,ne,nw,ne,sw,ne,ne,ne,n,n,n,nw,n,n,n,ne,n,se,se,n,se,ne,nw,n,ne,n,n,ne,ne,s,ne,n,n,ne,n,n,n,n,sw,ne,n,s,ne,nw,ne,n,n,n,n,ne,ne,n,n,n,ne,se,n,n,se,ne,n,nw,n,n,ne,ne,n,n,nw,ne,nw,n,ne,n,ne,sw,n,n,nw,nw,sw,ne,ne,sw,ne,n,s,ne,ne,ne,ne,n,sw,ne,se,n,sw,ne,ne,n,ne,ne,n,n,n,n,n,sw,ne,n,n,s,nw,n,ne,n,se,ne,n,n,nw,n,ne,n,ne,nw,n,n,ne,ne,n,ne,ne,n,n,s,n,ne,n,s,n,n,ne,n,sw,ne,nw,s,ne,n,se,n,sw,n,n,n,ne,ne,s,n,nw,n,ne,ne,ne,n,n,ne,ne,n,ne,n,ne,n,sw,nw,ne,n,n,n,nw,ne,ne,n,ne,ne,ne,ne,n,ne,s,ne,n,n,n,n,n,ne,n,n,ne,n,n,n,n,n,ne,s,n,ne,nw,n,n,ne,ne,n,n,ne,n,n,n,ne,nw,ne,ne,s,se,n,n,se,ne,n,n,n,s,nw,n,ne,s,ne,n,n,ne,ne,ne,ne,sw,s,ne,s,ne,ne,n,ne,ne,n,ne,s,sw,sw,ne,nw,n,s,se,n,n,ne,nw,ne,ne,n,n,ne,sw,ne,ne,n,s,ne,ne,ne,ne,ne,ne,ne,sw,n,ne,n,ne,n,n,n,ne,s,ne,n,ne,n,ne,sw,sw,n,s,ne,nw,sw,nw,nw,se,se,ne,ne,ne,n,ne,n,n,s,n,n,se,n,ne,n,nw,sw,ne,n,n,nw,ne,n,ne,n,ne,ne,n,ne,ne,se,n,n,n,ne,se,s,ne,ne,sw,n,ne,ne,n,ne,nw,ne,se,n,ne,nw,ne,ne,ne,n,ne,sw,ne,s,n,n,ne,ne,sw,ne,n,ne,se,se,ne,ne,ne,ne,ne,ne,ne,ne,ne,ne,ne,ne,s,ne,ne,nw,se,n,nw,n,s,n,sw,nw,nw,nw,ne,ne,s,se,n,se,ne,ne,nw,ne,ne,ne,ne,ne,ne,n,ne,n,ne,sw,nw,ne,n,ne,ne,ne,ne,ne,ne,n,ne,ne,ne,ne,ne,n,ne,ne,ne,se,ne,nw,ne,nw,n,sw,n,n,ne,ne,ne,n,ne,n,sw,ne,ne,n,ne,ne,ne,ne,se,ne,ne,ne,nw,n,n,ne,ne,nw,se,se,sw,ne,n,se,s,ne,ne,sw,ne,ne,ne,ne,n,ne,n,n,se,s,ne,ne,s,ne,ne,sw,ne,ne,ne,ne,ne,ne,ne,ne,s,ne,ne,ne,se,ne,ne,ne,ne,ne,s,ne,ne,s,ne,n,ne,s,ne,ne,sw,ne,ne,s,sw,n,n,ne,ne,ne,ne,ne,ne,ne,ne,ne,ne,se,nw,ne,ne,ne,ne,se,n,ne,nw,ne,sw,ne,ne,ne,ne,n,ne,ne,ne,ne,se,ne,ne,ne,ne,ne,ne,ne,ne,ne,s,ne,sw,ne,ne,ne,ne,n,ne,ne,ne,ne,ne,n,ne,ne,sw,ne,ne,ne,ne,ne,sw,ne,ne,ne,ne,ne,ne,sw,ne,s,nw,se,ne,ne,ne,ne,nw,ne,ne,sw,ne,ne,ne,ne,ne,ne,ne,ne,ne,ne,n,ne,ne,ne,ne,ne,se,ne,ne,sw,ne,ne,s,ne,ne,se,ne,sw,ne,ne,ne,ne,sw,ne,ne,ne,n,ne,s,ne,ne,ne,ne,s,ne,s,ne,ne,ne,ne,ne,nw,s,se,n,ne,ne,se,ne,ne,ne,ne,ne,ne,ne,ne,ne,ne,ne,ne,ne,ne,nw,se,ne,ne,ne,se,se,s,se,ne,sw,ne,sw,ne,se,ne,ne,se,ne,n,ne,ne,ne,ne,ne,ne,ne,ne,ne,ne,ne,ne,se,ne,se,n,ne,ne,ne,ne,ne,ne,se,se,ne,ne,ne,ne,se,ne,ne,ne,se,ne,ne,ne,ne,sw,ne,ne,ne,nw,s,ne,s,se,se,ne,ne,se,sw,ne,s,ne,ne,se,ne,ne,se,ne,ne,se,ne,ne,s,s,ne,ne,se,ne,se,se,ne,ne,n,ne,ne,nw,se,sw,ne,ne,ne,ne,ne,ne,ne,nw,ne,ne,ne,ne,se,ne,se,ne,se,sw,ne,ne,se,se,ne,ne,ne,ne,ne,se,ne,ne,ne,ne,ne,n,ne,ne,ne,ne,ne,se,s,ne,s,ne,nw,ne,ne,se,ne,ne,se,ne,ne,se,ne,s,ne,se,se,se,se,ne,se,ne,ne,n,ne,s,ne,sw,nw,nw,se,se,ne,se,ne,ne,ne,n,ne,ne,s,ne,n,sw,ne,ne,se,ne,ne,n,sw,ne,ne,se,ne,ne,se,s,ne,nw,ne,ne,nw,ne,s,ne,ne,se,ne,ne,ne,ne,ne,ne,nw,nw,ne,ne,ne,ne,se,se,se,ne,ne,s,ne,ne,n,s,ne,ne,s,ne,ne,n,ne,ne,ne,ne,se,ne,nw,n,ne,se,ne,se,se,ne,sw,sw,ne,n,s,ne,se,ne,ne,se,ne,n,se,ne,nw,ne,ne,nw,se,ne,ne,ne,ne,ne,ne,s,ne,se,sw,ne,ne,se,n,sw,se,ne,se,ne,ne,sw,ne,se,sw,se,ne,se,se,s,s,ne,ne,se,ne,se,ne,ne,se,sw,se,ne,ne,se,ne,sw,ne,se,se,sw,ne,ne,s,se,sw,nw,s,ne,n,sw,ne,s,ne,ne,ne,se,ne,ne,s,ne,se,ne,ne,ne,s,ne,ne,ne,ne,ne,nw,se,se,se,ne,n,se,ne,s,ne,ne,s,ne,se,se,n,se,se,nw,ne,ne,se,ne,se,ne,ne,ne,s,sw,se,ne,ne,ne,se,se,se,ne,se,se,se,se,ne,se,se,se,ne,sw,s,ne,ne,se,se,ne,se,ne,nw,se,se,nw,se,ne,se,ne,ne,se,se,ne,se,ne,ne,ne,ne,se,ne,ne,ne,s,se,se,ne,ne,ne,ne,n,ne,se,ne,se,se,se,n,ne,s,ne,ne,s,ne,se,se,se,ne,ne,ne,se,se,se,se,se,s,se,ne,ne,nw,ne,se,n,ne,se,ne,se,se,s,se,se,sw,ne,se,ne,ne,ne,ne,ne,se,se,se,se,ne,se,se,n,ne,se,ne,se,ne,ne,se,se,ne,se,se,ne,nw,ne,ne,sw,ne,se,s,se,se,ne,ne,ne,n,se,sw,ne,ne,se,se,se,n,se,ne,se,sw,se,ne,se,ne,ne,se,ne,nw,se,n,se,ne,ne,ne,se,se,ne,nw,ne,se,se,ne,ne,ne,se,se,se,ne,ne,ne,ne,ne,se,se,nw,ne,se,se,se,se,s,se,se,s,se,ne,ne,nw,se,se,se,ne,ne,se,s,se,se,se,ne,ne,sw,se,ne,ne,se,se,n,se,se,se,nw,se,se,ne,ne,se,sw,se,s,se,se,se,se,se,se,se,sw,s,sw,se,ne,nw,s,se,ne,ne,se,se,nw,se,se,ne,ne,se,se,se,se,ne,ne,ne,ne,se,se,se,sw,se,sw,se,se,se,n,se,nw,se,sw,ne,se,n,se,ne,ne,se,se,ne,se,ne,se,se,n,se,sw,ne,se,se,n,se,ne,se,sw,ne,se,se,ne,nw,se,se,ne,se,se,se,se,se,se,se,s,s,se,ne,ne,se,ne,se,se,se,se,n,nw,se,ne,se,se,se,nw,se,se,se,se,ne,se,se,se,se,se,se,se,ne,ne,se,se,se,se,s,s,se,se,ne,se,ne,se,se,s,n,ne,n,se,se,se,se,se,se,se,se,se,se,se,ne,se,ne,se,se,ne,nw,se,se,se,n,se,se,nw,se,se,ne,se,se,nw,se,ne,ne,se,se,se,se,se,se,s,se,se,ne,se,se,nw,se,se,se,se,se,se,se,n,se,se,ne,se,n,se,se,se,se,se,ne,s,n,se,se,se,se,ne,se,se,se,sw,se,ne,se,ne,se,se,se,se,se,se,se,ne,se,se,ne,se,ne,ne,se,se,ne,ne,se,n,se,se,se,se,se,se,se,n,se,se,se,se,se,se,se,se,se,se,se,se,se,ne,ne,se,se,se,se,se,se,se,se,ne,se,se,se,se,se,nw,ne,se,ne,nw,se,n,se,se,ne,nw,ne,nw,se,se,se,se,se,se,se,se,ne,ne,se,se,se,se,se,se,n,se,se,se,n,ne,se,s,se,se,se,se,ne,se,ne,se,se,sw,se,se,nw,se,se,nw,nw,se,nw,se,se,se,se,se,se,se,ne,se,sw,sw,se,se,se,se,se,ne,n,nw,se,ne,s,se,se,se,se,se,se,se,sw,se,ne,se,se,se,se,se,se,se,se,se,se,se,ne,se,se,se,se,n,se,se,ne,ne,se,se,se,se,s,nw,se,se,sw,se,se,se,n,se,se,se,se,se,se,s,se,se,sw,se,se,sw,ne,se,nw,se,se,se,se,se,nw,se,se,se,s,sw,se,se,se,nw,se,sw,sw,nw,se,s,se,se,nw,se,se,se,nw,se,nw,s,se,se,n,se,ne,se,sw,se,se,s,se,se,nw,se,se,se,se,se,se,se,se,sw,se,se,s,se,se,se,se,ne,se,se,se,sw,se,se,se,se,s,se,sw,se,se,se,se,se,s,se,se,se,se,se,se,se,se,se,se,se,se,sw,se,ne,sw,se,sw,se,n,se,se,se,se,ne,se,se,s,se,se,se,se,se,se,se,se,sw,se,se,s,se,se,se,se,se,se,se,se,se,s,sw,se,sw,se,se,se,se,ne,se,se,se,se,s,se,se,se,se,s,se,se,s,se,se,se,se,se,se,se,se,nw,s,n,se,se,se,se,se,se,se,se,se,se,se,se,se,se,se,se,se,s,ne,ne,s,se,se,se,se,s,se,se,se,se,s,se,se,se,se,se,se,se,se,se,se,se,ne,se,nw,se,se,se,se,n,se,n,s,n,se,n,se,se,se,se,se,s,se,se,se,n,se,nw,se,se,se,se,se,se,s,se,se,se,se,se,se,nw,se,se,se,n,se,se,s,s,ne,se,ne,sw,se,se,n,se,se,se,se,n,s,s,se,se,se,sw,s,se,se,se,se,s,s,n,sw,se,s,sw,se,se,n,se,s,se,s,s,se,se,se,se,se,s,se,se,se,se,se,se,se,se,n,se,n,se,n,s,s,s,s,se,se,se,nw,se,se,se,nw,nw,s,se,se,se,se,se,ne,se,s,sw,se,sw,se,sw,se,se,se,n,s,s,se,s,se,se,se,sw,se,se,se,se,se,se,s,nw,s,s,n,nw,se,se,se,n,se,nw,s,se,ne,se,se,ne,s,ne,nw,se,se,s,se,se,sw,se,se,se,se,se,se,se,se,se,se,se,se,s,se,se,se,se,se,se,se,se,se,s,se,se,se,se,se,se,ne,se,s,se,s,s,s,nw,se,s,se,s,se,se,ne,s,se,s,se,se,s,s,se,se,s,se,se,se,s,se,s,sw,se,s,se,n,se,nw,se,se,se,se,nw,se,nw,s,se,se,se,s,se,ne,se,n,sw,nw,s,nw,se,se,s,se,se,se,se,se,se,se,se,s,se,s,se,s,s,s,s,se,se,se,se,se,se,se,se,s,se,s,se,se,se,s,se,s,se,se,se,se,se,s,ne,se,s,se,sw,se,s,se,se,s,se,n,sw,se,s,s,sw,se,s,se,se,se,se,s,se,se,sw,nw,s,s,se,se,se,se,s,se,se,se,s,se,se,s,se,s,s,se,ne,s,se,se,se,nw,nw,se,se,s,ne,s,se,se,se,se,s,s,nw,se,se,se,n,s,se,se,s,s,sw,sw,ne,s,se,se,se,sw,se,se,n,se,nw,se,se,s,nw,se,se,se,se,nw,se,ne,nw,s,sw,sw,se,s,se,se,s,se,nw,se,sw,n,s,se,se,sw,s,se,se,s,nw,s,se,s,s,s,ne,sw,sw,se,se,s,se,se,se,se,nw,sw,nw,s,ne,se,s,s,s,s,s,s,se,se,nw,s,se,s,se,s,s,se,se,ne,n,s,ne,se,se,se,ne,se,s,s,s,s,se,s,se,se,s,se,s,se,s,se,se,s,se,s,s,se,se,nw,se,se,s,ne,s,se,s,s,ne,ne,se,s,se,n,se,se,se,s,se,se,se,s,s,s,s,se,ne,nw,s,s,se,s,s,se,se,s,se,n,s,se,nw,s,s,se,nw,se,n,sw,se,se,sw,nw,s,s,s,se,ne,s,s,se,sw,se,se,se,s,s,se,s,s,se,se,s,se,s,s,s,se,se,s,se,se,se,se,se,se,s,s,se,se,s,s,se,s,s,sw,sw,s,s,se,nw,se,n,s,sw,s,se,se,ne,ne,ne,se,se,s,se,s,nw,ne,s,s,ne,s,s,se,se,s,se,s,s,se,nw,nw,s,s,n,s,se,s,s,ne,s,se,se,s,n,s,se,se,nw,se,se,sw,se,se,s,s,s,s,s,s,se,sw,s,se,s,n,se,se,s,s,se,s,s,se,se,n,s,s,s,ne,nw,se,s,se,sw,s,s,s,se,sw,se,s,se,s,se,s,ne,s,s,se,s,s,s,s,ne,s,s,sw,se,sw,s,s,nw,ne,s,n,s,n,s,ne,se,s,s,se,ne,n,se,s,s,nw,ne,se,s,nw,s,s,nw,sw,s,s,nw,s,se,se,se,s,sw,s,se,s,s,sw,se,s,s,ne,se,nw,se,s,s,s,s,se,n,ne,sw,nw,se,s,ne,se,s,s,ne,se,s,se,se,ne,sw,s,s,ne,s,s,s,n,s,s,nw,s,ne,se,s,n,s,s,ne,se,s,sw,s,se,se,nw,s,s,se,s,s,s,s,se,n,s,sw,s,n,se,se,s,s,se,s,s,s,se,s,s,s,se,ne,se,s,se,nw,s,se,nw,s,nw,se,se,ne,s,s,s,s,ne,s,s,se,n,s,n,ne,s,s,ne,s,se,nw,s,se,s,s,nw,s,se,se,s,nw,s,se,n,s,s,se,s,s,s,s,se,s,s,n,s,s,s,s,ne,s,se,se,s,s,s,s,s,nw,s,ne,n,s,n,se,s,se,s,s,se,se,s,s,s,sw,se,se,se,se,s,s,s,se,se,se,se,s,s,sw,ne,se,ne,s,s,nw,s,se,s,s,s,s,s,se,s,se,nw,sw,ne,s,se,s,s,nw,s,s,s,s,s,s,n,s,n,se,s,s,ne,s,se,n,sw,s,ne,se,s,s,n,s,nw,se,s,s,se,s,s,s,sw,s,s,se,se,s,s,nw,s,se,s,nw,n,se,s,s,s,s,s,n,sw,s,s,se,s,nw,s,se,ne,s,se,se,s,s,n,se,s,se,se,s,s,s,se,se,se,sw,ne,s,s,se,nw,s,ne,sw,s,s,n,s,n,se,s,ne,s,s,sw,n,s,s,s,s,s,s,s,s,s,se,s,s,s,se,s,s,se,s,ne,s,s,se,s,s,s,s,s,se,s,s,s,nw,s,ne,s,s,ne,sw,s,s,s,s,se,s,se,s,s,s,s,s,se,s,s,se,se,s,nw,s,s,se,s,s,s,s,s,s,s,s,nw,s,s,nw,n,s,s,sw,s,s,s,s,s,ne,s,s,s,ne,s,s,sw,n,s,n,ne,se,se,s,sw,s,se,sw,s,s,s,s,s,s,sw,s,ne,n,s,s,s,s,se,s,s,s,s,s,s,se,s,n,s,s,s,ne,s,s,nw,sw,s,ne,s,s,se,nw,nw,s,s,se,s,se,s,s,s,s,s,s,s,sw,s,s,s,s,s,sw,sw,s,s,se,s,s,n,ne,se,s,s,s,s,s,s,sw,s,s,s,s,s,s,s,se,sw,nw,ne,nw,n,s,s,s,s,s,s,s,se,nw,n,s,nw,s,sw,s,se,s,nw,s,sw,s,se,se,s,s,s,s,s,s,se,se,s,se,s,s,s,s,s,s,se,s,s,s,s,s,s,ne,s,nw,s,s,nw,s,se,s,s,s,se,s,s,s,s,sw,ne,s,s,s,s,s,s,s,s,s,s,se,s,sw,s,s,sw,s,s,s,se,s,s,s,s,s,se,s,s,s,ne,s,s,s,s,nw,s,s,s,nw,s,se,s,s,s,s,s,s,s,s,s,sw,s,s,s,s,ne,s,s,s,s,s,s,s,sw,s,s,s,s,sw,s,s,s,s,s,s,s,s,s,s,s,se,s,s,s,s,ne,s,s,s,s,se,s,nw,s,s,s,s,s,s,s,s,sw,ne,n,n,n,n,ne,nw,nw,nw,nw,nw,se,s,sw,sw,n,sw,sw,sw,sw,sw,sw,sw,se,sw,sw,sw,ne,sw,sw,s,s,ne,sw,sw,ne,s,nw,s,nw,s,nw,se,ne,nw,s,s,nw,s,s,se,se,se,s,se,se,se,se,sw,se,se,se,se,se,se,ne,ne,se,ne,ne,se,se,n,ne,n,se,ne,se,ne,ne,ne,ne,ne,ne,ne,ne,s,ne,nw,ne,ne,ne,nw,ne,ne,n,ne,ne,n,ne,ne,ne,ne,ne,n,ne,sw,sw,n,n,n,ne,n,ne,ne,se,n,nw,ne,ne,n,n,s,se,n,ne,ne,n,n,n,se,ne,n,n,n,s,n,n,n,n,n,n,n,n,n,n,sw,se,n,n,n,nw,n,n,n,n,nw,n,sw,nw,n,nw,nw,n,n,n,nw,s,nw,se,n,ne,n,n,n,n,n,nw,nw,sw,nw,n,nw,n,nw,nw,n,n,nw,nw,n,nw,nw,sw,nw,nw,nw,nw,nw,n,nw,nw,n,n,nw,nw,nw,nw,ne,nw,nw,n,n,nw,ne,nw,nw,nw,nw,nw,nw,s,sw,nw,nw,nw,nw,ne,sw,nw,sw,nw,nw,nw,nw,s,nw,nw,nw,nw,nw,nw,nw,n,se,nw,nw,s,nw,sw,sw,nw,nw,nw,nw,nw,sw,sw,s,nw,se,ne,se,nw,nw,ne,ne,nw,sw,s,sw,sw,s,nw,ne,nw,nw,sw,n,n,sw,sw,n,sw,sw,nw,nw,sw,nw,sw,sw,nw,nw,nw,nw,sw,se,sw,sw,se,sw,se,sw,sw,nw,n,nw,sw,sw,sw,sw,sw,sw,sw,sw,sw,sw,sw,sw,sw,se,sw,sw,sw,sw,sw,sw,nw,sw,sw,sw,sw,n,sw,sw,sw,sw,ne,sw,sw,se,ne,sw,sw,sw,sw,se,s,nw,sw,sw,ne,sw,sw,sw,n,s,s,sw,sw,sw,sw,sw,s,sw,sw,ne,sw,nw,sw,s,ne,sw,s,sw,s,sw,sw,s,sw,sw,sw,s,se,s,s,sw,nw,sw,s,s,s,s,s,s,sw,sw,sw,sw,sw,n,ne,s,se,s,nw,s,s,s,s,s,n,s,s,s,s,s,s,n,s,s,s,nw,sw,s,s,sw,s,sw,s,s,s,s,nw,se,s,ne,s,ne,s,s,s,sw,sw,s,s,ne,s,nw,n,sw,s,n,s,sw,s,s,s,s,s,s,s,s,se,s,s,s,ne,s,s,s,s,se,s,s,s,s,s,n,se,sw,s,s,s,ne,s,s,s,s,se,s,s,s,s,s,s,ne,nw,se,s,se,s,ne,s,ne,s,nw,s,s,se,se,s,nw,s,sw,sw,s,s,s,sw,se,s,se,s,se,s,n,s,se,s,s,s,n,s,s,s,se,s,s,se,s,s,se,ne,n,se,s,s,se,s,se,se,s,s,n,s,s,s,n,s,s,sw,se,n,se,s,s,se,se,s,sw,se,s,nw,s,se,se,se,s,s,se,ne,se,s,s,s,s,se,se,s,n,s,s,se,se,nw,sw,s,n,se,s,se,s,s,se,s,se,se,se,se,nw,ne,ne,s,se,se,s,se,se,se,s,s,se,sw,sw,se,se,s,s,s,se,s,se,se,se,se,n,n,se,se,se,sw,s,s,s,s,se,nw,se,s,se,se,s,nw,se,se,se,se,n,se,se,se,se,se,se,nw,se,se,ne,se,se,se,s,se,se,se,se,n,nw,se,se,se,se,se,s,se,se,n,se,sw,se,ne,se,n,se,se,ne,ne,se,se,sw,sw,se,se,se,se,ne,se,se,se,se,se,se,se,se,se,ne,ne,se,ne,se,ne,s,se,ne,se,nw,ne,sw,s,se,se,se,se,sw,se,se,se,se,ne,se,ne,se,se,se,nw,ne,se,se,se,se,ne,se,sw,se,se,ne,s,se,se,ne,se,se,se,ne,se,n,se,nw,se,se,se,sw,se,se,ne,se,se,se,ne,ne,ne,se,ne,se,se,se,se,s,se,se,sw,ne,se,nw,ne,se,se,se,ne,n,ne,n,ne,se,se,se,ne,se,ne,sw,ne,nw,se,ne,ne,ne,ne,se,ne,ne,ne,sw,se,ne,se,ne,se,ne,se,s,se,se,se,se,se,ne,ne,se,ne,ne,ne,ne,s,se,se,ne,ne,se,ne,ne,ne,s,se,ne,ne,s,se,nw,ne,se,ne,ne,n,ne,ne,s,ne,se,sw,se,ne,ne,ne,se,ne,ne,sw,ne,sw,se,ne,ne,ne,ne,ne,ne,ne,se,sw,ne,ne,ne,ne,ne,se,nw,se,ne,s,ne,se,ne,s,ne,ne,ne,sw,ne,ne,ne,se,nw,n,se,ne,nw,ne,ne,ne,sw,ne,ne,se,se,se,ne,ne,nw,ne,se,ne,ne,n,ne,ne,ne,ne,ne,ne,ne,se,ne,s,ne,ne,ne,ne,n,ne,sw,ne,ne,ne,ne,ne,ne,s,n,ne,ne,ne,sw,ne,ne,ne,ne,sw,ne,nw,ne,ne,ne,ne,ne,ne,ne,ne,ne,ne,ne,s,ne,n,ne,ne,ne,ne,n,ne,n,ne,se,sw,ne,nw,n,se,ne,n,ne,s,n,ne,ne,ne,nw,n,ne,ne,ne,sw,ne,se,ne,ne,ne,nw,nw,ne,n,ne,ne,ne,ne,ne,ne,nw,ne,ne,ne,se,ne,s,sw,nw,ne,ne,ne,ne,ne,ne,n,ne,n,ne,n,ne,ne,n,ne,ne,nw,s,n,se,ne,ne,s,ne,ne,se,ne,ne,ne,sw,n,ne,ne,n,ne,n,ne,se,ne,ne,n,ne,nw,ne,ne,n,ne,ne,n,se,ne,se,ne,ne,n,sw,n,s,n,ne,n,s,ne,ne,ne,ne,se,n,ne,n,nw,n,ne,ne,ne,s,ne,ne,ne,n,n,sw,se,sw,ne,ne,n,ne,ne,ne,ne,n,se,ne,se,ne,s,s,n,n,ne,n,ne,s,ne,nw,se,se,sw,n,n,sw,ne,s,n,se,ne,ne,ne,ne,n,sw,ne,ne,ne,ne,n,ne,n,ne,se,n,n,n,n,s,n,ne,se,n,ne,ne,nw,ne,ne,ne,n,ne,ne,n,ne,n,nw,n,n,n,n,ne,n,n,ne,ne,n,n,ne,n,n,n,ne,n,ne,ne,ne,ne,n,n,ne,n,n,ne,n,n,nw,n,n,n,n,nw,nw,n,n,n,n,sw,n,n,ne,ne,n,ne,ne,nw,n,ne,sw,ne,n,n,ne,nw,nw,n,n,nw,n,n,n,ne,n,s,n,n,ne,ne,n,n,ne,ne,ne,ne,n,n,n,sw,n,sw,n,n,n,n,s,n,nw,ne,n,n,n,n,se,nw,n,n,n,n,n,n,ne,s,n,ne,n,n,n,n,ne,ne,n,sw,n,n,n,n,ne,n,ne,n,n,ne,n,n,n,n,n,ne,n,ne,ne,n,n,n,n,ne,n,nw,s,n,s,n,n,sw,n,n,n,nw,ne,ne,nw,n,n,n,nw,n,n,n,n,n,n,nw,n,n,n,n,n,n,n,n,n,s,n,n,nw,n,n,n,nw,n,n,n,sw,s,se,n,n,n,n,n,nw,n,n,n,n,n,n,ne,n,se,sw,n,n,n,nw,n,n,n,n,n,n,n,n,n,n,ne,n,nw,n,n,ne,n,n,n,ne,n,n,n,n,n,n,se,n,n,n,s,n,nw,nw,n,n,n,n,nw,ne,sw,n,nw,n,nw,se,nw,nw,n,n,n,n,n,n,n,nw,n,n,n,n,n,n,ne,se,n,n,n,n,n,nw,n,nw,n,n,n,se,n,n,n,s,n,n,nw,n,se,sw,n,n,nw,n,n,sw,se,n,n,n,nw,nw,n,n,n,s,n,nw,n,n,n,nw,nw,s,nw,n,nw,n,nw,n,n,nw,nw,n,n,nw,s,n,n,nw,nw,n,n,n,n,n,nw,n,n,n,n,n,n,n,nw,ne,n,sw,nw,n,n,sw,nw,ne,se,n,n,nw,s,n,n,nw,nw,nw,sw,n,n,ne,n,n,nw,nw,n,nw,nw,n,n,n,nw,n,n,n,nw,n,se,nw,n,nw,nw,n,n,n,n,n,s,n,n,n,nw,nw,ne,n,nw,n,s,n,ne,nw,n,n,n,n,nw,nw,se,nw,nw,n,n,n,nw,nw,sw,nw,n,sw,nw,n,n,sw,n,nw,n,sw,nw,nw,nw,n,n,s,n,se,nw,nw,nw,n,n,se,n,n,nw,nw,nw,n,nw,nw,se,nw,n,nw,n,n,n,nw,s,n,nw,nw,nw,se,n,n,nw,nw,n,n,n,n,nw,n,n,n,nw,nw,nw,nw,sw,n,n,nw,n,nw,nw,nw,nw,n,n,n,n,nw,n,nw,nw,n,nw,n,n,n,n,n,n,sw,s,nw,nw,n,nw,nw,n,nw,n,se,nw,nw,nw,ne,n,n,nw,nw,s,nw,nw,nw,nw,nw,nw,nw,n,n,se,nw,s,nw,nw,nw,n,nw,n,nw,n,n,nw,n,se,se,nw,n,n,nw,nw,n,sw,nw,s,se,nw,nw,se,n,nw,nw,n,nw,n,s,nw,nw,nw,nw,nw,nw,nw,nw,n,nw,n,nw,n,ne,s,sw,sw,s,nw,n,n,nw,nw,nw,nw,nw,nw,nw,nw,nw,n,nw,nw,nw,n,nw,nw,nw,nw,n,nw,nw,nw,n,nw,n,n,nw,nw,n,nw,nw,nw,nw,nw,se,nw,nw,n,n,nw,se,nw,nw,n,se,nw,nw,ne,nw,n,nw,nw,sw,nw,s,nw,nw,ne,n,n,nw,nw,nw,nw,nw,nw,nw,nw,nw,nw,n,nw,n,nw,nw,ne,se,nw,nw,se,s,se,nw,n,nw,nw,nw,nw,n,n,se,nw,nw,nw,sw,nw,s,nw,nw,nw,nw,nw,nw,ne,nw,n,nw,nw,nw,nw,nw,nw,nw,nw,ne,n,nw,s,nw,nw,nw,ne,ne,nw,nw,nw,nw,nw,nw,nw,nw,nw,nw,nw,nw,n,nw,nw,nw,n,ne,s,nw,nw,nw,nw,nw,nw,s,nw,nw,nw,nw,nw,nw,nw,s,nw,nw,nw,nw,nw,nw,sw,sw,nw,n,ne,nw,nw,nw,nw,nw,nw,n,ne,nw,nw,nw,nw,nw,ne,s,s,nw,nw,nw,nw,n,nw,nw,nw,nw,nw,n,nw,se,nw,nw,nw,nw,nw,s,nw,s,nw,nw,nw,n,ne,nw,nw,nw,nw,se,nw,nw,nw,nw,nw,nw,nw,nw,ne,nw,nw,sw,nw,nw,nw,nw,se,nw,nw,se,nw,nw,nw,sw,nw,nw,n,nw,nw,nw,sw,s,nw,nw,s,n,nw,s,nw,nw,nw,sw,s,nw,nw,s,nw,nw,ne,se,nw,nw,nw,nw,nw,ne,nw,nw,nw,nw,nw,nw,nw,nw,ne,ne,nw,nw,nw,nw,n,nw,nw,nw,s,nw,nw,nw,nw,nw,sw,n,ne,sw,nw,nw,n,nw,nw,n,nw,ne,n,nw,sw,nw,nw,nw,nw,s,nw,nw,nw,nw,nw,s,sw,se,nw,nw,sw,se,sw,nw,sw,sw,nw,nw,se,sw,nw,nw,s,nw,sw,sw,nw,sw,ne,nw,nw,s,nw,nw,nw,se,nw,nw,nw,nw,ne,sw,ne,nw,nw,sw,nw,nw,nw,sw,nw,nw,nw,nw,nw,nw,sw,nw,sw,sw,sw,ne,nw,nw,nw,sw,sw,sw,sw,nw,nw,sw,nw,sw,nw,sw,nw,nw,nw,nw,nw,se,nw,nw,nw,sw,n,sw,nw,ne,nw,sw,sw,nw,nw,nw,nw,sw,nw,nw,n,sw,se,nw,nw,nw,nw,sw,nw,sw,nw,nw,nw,sw,n,sw,n,sw,sw,nw,sw,se,n,nw,sw,nw,sw,nw,sw,nw,s,nw,nw,se,nw,sw,sw,nw,nw,nw,sw,n,nw,nw,s,sw,nw,nw,nw,nw,nw,ne,sw,n,sw,sw,sw,nw,nw,nw,se,sw,nw,sw,sw,n,nw,se,nw,nw,sw,sw,sw,sw,sw,nw,sw,sw,sw,sw,nw,sw,sw,nw,nw,s,n,nw,nw,nw,ne,nw,nw,sw,sw,se,nw,nw,nw,sw,ne,sw,ne,n,nw,sw,sw,sw,nw,sw,sw,nw,sw,sw,sw,se,nw,sw,se,nw,n,nw,sw,sw,nw,sw,nw,n,nw,n,nw,nw,nw,sw,sw,nw,nw,nw,nw,nw,sw,sw,sw,nw,nw,nw,nw,nw,nw,nw,nw,ne,nw,sw,nw,nw,sw,sw,nw,sw,nw,se,sw,sw,nw,nw,sw,nw,s,sw,nw,nw,sw,sw,ne,sw,sw,nw,nw,sw,nw,nw,sw,sw,nw,s,se,sw,nw,sw,sw,sw,nw,nw,sw,nw,sw,sw,nw,sw,sw,n,n,sw,s,se,nw,sw,sw,nw,se,sw,nw,sw,nw,nw,nw,sw,sw,nw,nw,s,sw,sw,nw,sw,nw,sw,nw,nw,sw,sw,nw,nw,sw,sw,sw,nw,sw,ne,sw,sw,s,nw,se,sw,sw,se,n,sw,sw,sw,nw,sw,sw,nw,ne,nw,nw,sw,nw,nw,sw,sw,nw,nw,sw,sw,sw,se,sw,nw,sw,sw,sw,nw,nw,sw,sw,sw,sw,sw,n,sw,sw,sw,nw,sw,sw,sw,sw,sw,nw,ne,n,sw,sw,nw,s,nw,nw,sw,sw,s,nw,nw,nw,ne,sw,ne,sw,sw,sw,sw,sw,nw,nw,sw,nw,se,sw,nw,sw,sw,n,sw,ne,nw,sw,sw,sw,nw,sw,sw,sw,nw,nw,sw,sw,sw,nw,se,n,sw,sw,sw,sw,se,s,nw,sw,nw,nw,n,nw,sw,sw,sw,sw,sw,sw,sw,se,n,se,sw,sw,nw,sw,sw,n,nw,sw,sw,nw,sw,sw,s,sw,sw,sw,sw,sw,sw,nw,sw,nw,sw,sw,sw,sw,sw,s,sw,sw,sw,nw,sw,s,sw,nw,sw,sw,sw,sw,sw,sw,sw,sw,sw,s,sw,nw,sw,sw,nw,sw,nw,sw,sw,se,sw,nw,sw,nw,sw,se,sw,nw,se,n,sw,sw,s,sw,sw,sw,sw,sw,nw,sw,n,se,sw,nw,sw,sw,sw,se,sw,sw,sw,sw,sw,sw,sw,se,sw,nw,sw,sw,sw,sw,sw,sw,sw,ne,sw,n,sw,sw,sw,sw,sw,sw,sw,sw,s,sw,sw,sw,sw,nw,nw,nw,sw,sw,sw,sw,se,sw,sw,nw,sw,nw,sw,sw,sw,sw,sw,sw,sw,sw,sw,se,sw,sw,sw,se,s,sw,sw,sw,sw,sw,ne,sw,sw,sw,sw,se,sw,sw,sw,sw,sw,sw,se,sw,se,sw,sw,sw,sw,sw,sw,sw,sw,sw,n,sw,sw,sw,sw,sw,sw,sw,sw,sw,nw"
step = inputString.split(",")

coords = [0, 0, 0]
maxDistance = 0

for c in step:
    if c == "n":
        coords[1] = coords[1] + 1
        coords[2] = coords[2] - 1
    elif c == "ne":
        coords[0] = coords[0] + 1
        coords[2] = coords[2] - 1
    elif c == "se":
        coords[1] = coords[1] - 1
        coords[0] = coords[0] + 1
    elif c == "s":
        coords[1] = coords[1] - 1
        coords[2] = coords[2] + 1
    elif c == "sw":
        coords[0] = coords[0] - 1
        coords[2] = coords[2] + 1
    elif c == "nw":
        coords[1] = coords[1] + 1
        coords[0] = coords[0] - 1

    distance = int((abs(coords[0] - 0) + abs(coords[1] - 0) + abs(coords[2] - 0)) / 2)
    maxDistance = max(distance, maxDistance)

# distance = abs(coords[0]) + abs(coords[1]) + abs(coords[2])
print(maxDistance)