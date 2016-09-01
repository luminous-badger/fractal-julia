#!/usr/bin/python

# Plot Julia using PIL / Pillow. Plots x,y, not y,x as does pylab.
# JM Mon  5 Jan 2015 15:11:32 GMT
# For 1, L, and I images, use integers. For RGB images, use a 3-tuple containing integer values. 
# For F images, use integer or floating point values.
# Julia set for c close to -0.74-0.11i. Its Hausdorff dimension is close to 2. 
# JM Thu 27 Aug 2015 20:00:36 BST

from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import numpy as nm
import cmath
from timeit import default_timer as timer
from lc import colour_list 

start = timer()

X_MIN = -1.75
X_MAX =  1.75
Y_MIN = -1.5
Y_MAX =  1.5
offset     = 0.01
maxiter    = 95
calc_count = 0
rnum       = 43
C          = complex ( -0.724 ,  0.24713 )
#C          = complex ( -1.768667862837488812627419470 , 0.001645580546820209430325900 )

lenlc      = len( colour_list ) 

# create a new X*Y pixel image surface
# make the background white (default bg=black)
X_SIZE = ( X_MAX - X_MIN ) / offset
Y_SIZE = ( Y_MAX - Y_MIN ) / offset

X_SIZE += 1
Y_SIZE += 1

X_SIZE = int( X_SIZE )
Y_SIZE = int( Y_SIZE )

print 'X: ', X_SIZE ,' Y: ', Y_SIZE 

white      = (255,255,255)
randcolour =  ( 139, 0, 0 )
blue       = (0,0,255) 
img        = Image.new( "RGB", [ X_SIZE, Y_SIZE ], white )

mycolour = ( 100, 150, 200 ) 
x_pixel = 0
for X in nm.arange ( X_MIN, X_MAX, offset ):
	y_pixel = 0
	for Y in nm.arange ( Y_MIN, Y_MAX, offset ):
		Z = complex ( X, Y )
		iter_count = 0

		while ( abs ( Z**2 ) < 4 and iter_count < maxiter ):
			Z = Z**2 + C
			iter_count = iter_count + 1
			#print X, Y , Z
			calc_count = calc_count + 1  
		#mycolour = ( 5 * iter_count, 109 + iter_count, 43 + iter_count ) 
		#mycolour = colour_list[ iter_count % len( colour_list ) ]
		#mycolour = colour_list[ iter_count % len( colour_list ) ]
		'''
		mycolour = ( 13 * iter_count, 23 * iter_count, 33 * iter_count ) 
		img.putpixel( ( x_pixel,  y_pixel ), mycolour ) 
		'''
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

MsgText = 'Julia for Z^2 +' + str( C ) + ' and rnum: ' + str( rnum )

draw = ImageDraw.Draw(img)
font = ImageFont.truetype( "/Library/Fonts/Arial.ttf", 12 )
draw.text( ( 0, 0 ),  MsgText, ( 139,0,0 ), font=font )

print 'Julia for', C, 'and Rand:', rnum, 'created in %f s' % dt
print 'Calc: ', calc_count
img.show()
#img.save( 'Gaston_Julia.png' )

