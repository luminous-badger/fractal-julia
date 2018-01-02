#!/usr/bin/python

# Plot 'brot using PIL / Pillow. Plots x,y, not y,x as does pylab.
# JM Mon  5 Jan 2015 15:11:32 GMT
# For 1, L, and I images, use integers. For RGB images, use a 3-tuple containing integer values. 
# For F images, use integer or floating point values.
'''
Print X,Y,Iter plot.
fractalworks://x?type=julia
plot_height=800
plot_width=800
max_iterations=60000
center_r=-2.951345431789738e-07
center_i=-2.951345431789743e-07
r_width=9.4325E-05
c_real=-0.7602551664522519
c_imag=0.08508278985012406
sourcemandelmagnification=3.45e-13

From: http://www.pbase.com/duncanc/image/78937965
JM Tue 12 Dec 2017 18:59:06 GMT
'''

import numpy as nm
import cmath
from timeit import default_timer as timer
from lc import colour_list
import sys

start = timer()

# The plot is centered at 0,0 at a width of about .0042 
r_width     =  9.4325E-05 * 1.5
plot_height = 800

X_MIN = 0.0 - r_width
X_MAX = 0.0 + r_width

Y_MIN = 0.0 - r_width
Y_MAX = 0.0 + r_width
offset     = ( X_MAX - X_MIN ) / plot_height
maxiter    = 5175
calc_count = 0
rnum       = 33
#rnum       = int( sys.argv[ 1 ] )
ZPower     = 2
c_real     = -0.7602551664522519
c_imag     =  0.08508278985012406
C          = complex ( c_real, c_imag )

# create a new X*Y pixel image surface
# make the background white (default bg=black)
X_SIZE = ( X_MAX - X_MIN ) / offset
Y_SIZE = ( Y_MAX - Y_MIN ) / offset

X_SIZE += 1
Y_SIZE += 1

X_SIZE = int( X_SIZE )
Y_SIZE = int( Y_SIZE )

print 'X: ', X_SIZE ,' Y: ', Y_SIZE, ' Offset:', offset, ' RW:', r_width

if ( len( sys.argv ) == 2 ):
	sys.exit()

x_pixel = 0
for X in nm.arange ( X_MIN, X_MAX, offset ):
	y_pixel = 0
	for Y in nm.arange ( Y_MIN, Y_MAX, offset ):
		Z = complex ( X, Y )
		iter_count = 0
		#print 'XYZ:', X,Y,Z

		while ( abs ( Z**ZPower ) < 4 and iter_count < maxiter ):
			Z = Z**ZPower + C
			iter_count = iter_count + 1
			#print X, Y , Z
			calc_count = calc_count + 1  
		print '{0:6d}'.format( iter_count ),	
		y_pixel += 1
	print
	x_pixel += 1

dt = timer() - start

MsgText = 'Julia for Z^' + str( ZPower ) + ' ' + str( C ) + ' Rnum: ' + str( rnum ) 

print MsgText , 'created in %f s' % dt
print  'X: ' + str( X_MAX ) + ' ' + str( X_MIN ) + ' Y: ' + str( Y_MAX ) + ' ' + str( Y_MIN ) 
print 'Calc: ', calc_count

