# _*_ coding:utf-8 _*_

import sys
import pandas as pd
import numpy as np
from google.colab import drive

# data = pd.read_csv('gdrive/My Drive/hw1-regression/train.csv', header = None, encoding = 'big5')
data = pd.read_csv('./train.csv', encoding = 'big5')