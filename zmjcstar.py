#!/usr/bin/python

# Plot 'brot using PIL / Pillow. Plots x,y, not y,x as does pylab.
# JM Mon  5 Jan 2015 15:11:32 GMT
# For 1, L, and I images, use integers. For RGB images, use a 3-tuple containing integer values. 
# For F images, use integer or floating point values.
# Julia from: http://www.pbase.com/duncanc/image/85389324
# Star Julia. Zoom in.
# JM Sun 26 Nov 2017 17:42:09 GMT

from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import numpy as nm
import cmath
from timeit import default_timer as timer
from lc import colour_list
import sys

start = timer()

center_r=-2.768000000000029e-05
center_i=3.32160000000001e-05
r_width=0.004152
X_MIN = center_r - r_width
X_MAX = center_r + r_width
Y_MIN = center_i - r_width 
Y_MAX = center_i + r_width

div_offset = 400.0

X_SPAN = X_MAX - X_MIN
xoffset = X_SPAN / div_offset 
Y_SPAN = Y_MAX - Y_MIN
yoffset = Y_SPAN / div_offset 

#offset     = 0.01
maxiter    = 975
calc_count = 0
rnum       = 94
#rnum       = int( sys.argv[ 1 ] )
ZPower     = 2
#CInput     = float( sys.argv[ 1 ] )
#C          = complex ( 0.211, CInput )
#C          = complex ( CInput,  0.0  )
c_real     = 0.2650393607207308
c_imag     = 0.003034021619132559
C          = complex ( c_real, c_imag )

# create a new X*Y pixel image surface
# make the background white (default bg=black)
X_SIZE = ( X_MAX - X_MIN ) / xoffset
Y_SIZE = ( Y_MAX - Y_MIN ) / yoffset

X_SIZE += 1
Y_SIZE += 1

X_SIZE = int( X_SIZE )
Y_SIZE = int( Y_SIZE )

print 'X: ', X_SIZE ,' Y: ', Y_SIZE 

if ( len( sys.argv ) == 2 ):
	sys.exit()

white      = (255,255,255)
randcolour = (100,149,237)
img        = Image.new( "RGB", [ X_SIZE, Y_SIZE ], white )
lenlc      =  len( colour_list ) 

x_pixel = 0
for X in nm.arange ( X_MIN, X_MAX, xoffset ):
	y_pixel = 0
	for Y in nm.arange ( Y_MIN, Y_MAX, yoffset ):
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

