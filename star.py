#!/usr/bin/python

import numpy as nm

plot_height=751
plot_width=751
max_iterations=10000
center_r=-2.768000000000029e-05
center_i=3.32160000000001e-05
r_width=0.004152
c_real=0.2650393607207308
c_imag=0.003034021619132559
sourcemandelmagnification=1.85e-14

print 'center_r:', center_r
print 'center_r: {0:.21f}'.format( center_r )
print 'center_i:', center_i

xmin = center_r - r_width
xmax = center_r + r_width
ymin = center_i - r_width
ymax = center_i + r_width
print 'xmin:', xmin
print 'xmax:', xmax
print 'ymin:', ymin
print 'ymax:', ymax

div_offset = 400.0

xspan = xmax - xmin
xoffset = xspan / div_offset 
yspan = ymax - ymin
yoffset = yspan / div_offset 
loopcount = 1
xsize = xspan / xoffset
ysize = yspan / yoffset

print 'xspan:', xspan, ' div_offset:', div_offset, ' xoffset:', xoffset, ' xsize:', xsize
print 'yspan:', yspan, ' div_offset:', div_offset, ' yoffset:', yoffset, ' ysize:', ysize
'''
for X in nm.arange ( xmin, xmax, offset ):
	print 'loopcount:', loopcount, ' X:', X
	loopcount += 1
'''	
