# -*- coding: utf-8 -*-
"""
interpolation

Created on Tue Dec 03 10:43:41 2013

@author: andy
"""

import numpy as np
import scipy as sp
from PIL import Image
import matplotlib as mpl
from scipy.interpolate import griddata

im = np.array(Image.open('test.bmp').convert('L')).astype(np.float)

grid_x,grid_y = np.mgrid[0:41:41j,0:41:41j]
y,x = np.where(im!=255)
pts = np.vstack((x,y)).T
data = im[pts[:,0],pts[:,1]]

resultc = griddata(pts,data,(grid_x,grid_y),method='cubic')
resultl = griddata(pts,data,(grid_x,grid_y),method='linear')
resultn = griddata(pts,data,(grid_x,grid_y),method='nearest')


clim = [20,255]
cmap = 'gist_heat'

interp = 'nearest'

plt.subplot(221)
plt.imshow(im.T, extent=(0,1,0,1), origin='lower', clim=clim, cmap=cmap, 
               interpolation=interp)
plt.title('Original')
plt.subplot(222)
plt.imshow(resultn.T, extent=(0,1,0,1), origin='lower', clim=clim, cmap=cmap, 
               interpolation=interp)
plt.title('Nearest')
plt.subplot(223)
plt.imshow(resultl.T, extent=(0,1,0,1), origin='lower', clim=clim, cmap=cmap,
               interpolation=interp)
plt.title('Linear')
plt.subplot(224)
plt.imshow(resultc.T, extent=(0,1,0,1), origin='lower', clim=clim, cmap=cmap, 
               interpolation=interp)
plt.title('Cubic')
plt.gcf().set_size_inches(6, 6)
plt.show()