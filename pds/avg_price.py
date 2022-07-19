# -*- encoding:utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

__ENTITY_author__ = "SIX DIGIT INVESTMENT GROUP"
__author__ = "GWONGZAN"

import pandas as pd
import numpy as np


org_share = 200
org_at = 18.72
org_cost = org_share * org_at

var_share = np.arange(200, 1001, 1)
var_at = np.arange(89, 100, 1)/10.0
var_cost = var_share.reshape((1, var_share.size))*var_at

est_share = var_share+org_share
est_cost = var_cost+org_cost
est_at = est_cost/est_share

print(est_share)
print(est_cost)
print(est_at)

if __name__ == "__main__":
    pass

