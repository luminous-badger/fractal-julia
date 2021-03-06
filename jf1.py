#!/usr/bin/python

# Plot 'brot using PIL / Pillow. Plots x,y, not y,x as does pylab.
# JM Mon  5 Jan 2015 15:11:32 GMT
# For 1, L, and I images, use integers. For RGB images, use a 3-tuple containing integer values. 
# For F images, use integer or floating point values.
'''
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

from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import numpy as nm
import cmath
from timeit import default_timer as timer
from lc import colour_list
import sys

start = timer()

# The plot is centered at 0,0 at a width of about .0042 
r_width     =  9.4325E-05 * 1.5
plot_height = 200

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

white      = (255,255,255)
randcolour = (100,149,237)
img        = Image.new( "RGB", [ X_SIZE, Y_SIZE ], white )
lenlc      =  len( colour_list ) 

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
		if ( iter_count + rnum  >= lenlc ):
			mycolour = colour_list[ iter_count % lenlc ]
		else:
			mycolour = colour_list[ iter_count + rnum  ]
		if ( iter_count <= 2 ):
			img.putpixel( ( x_pixel,  y_pixel ), white ) 
		elif ( iter_count == maxiter ):
			img.putpixel( ( x_pixel,  y_pixel ), randcolour ) 
		else:
			img.putpixel( ( x_pixel,  y_pixel ), mycolour ) 
		y_pixel += 1

	x_pixel += 1

dt = timer() - start

MsgText = 'Julia for Z^' + str( ZPower ) + ' ' + str( C ) + ' Rnum: ' + str( rnum ) 

draw = ImageDraw.Draw(img)
font = ImageFont.truetype( "/Library/Fonts/Arial.ttf", 12 )
draw.text( ( 0, 0 ),  MsgText, ( 0,0,0 ), font=font )

#print 'Julia for:', C, 'created in %f s' % dt
print MsgText , 'created in %f s' % dt
print  'X: ' + str( X_MAX ) + ' ' + str( X_MIN ) + ' Y: ' + str( Y_MAX ) + ' ' + str( Y_MIN ) 
print 'Calc: ', calc_count

fname = 'Julia_Z_' + str( ZPower ) + '_C_' + str( C ) + '_X:' + str( X_MAX ) + str( X_MIN ) + '_Y:' + str( Y_MAX ) + str( Y_MIN ) + '.png'
print 'Fname:', fname

img.show()
#img.save( fname )

