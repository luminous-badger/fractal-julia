#!/usr/bin/python

# Plot Julia using PIL / Pillow. Plots x,y, not y,x as does pylab.
# JM Mon  5 Jan 2015 15:11:32 GMT
# For 1, L, and I images, use integers. For RGB images, use a 3-tuple containing integer values. 
# For F images, use integer or floating point values.
# Julia symmetric for -1 + 0i.
# JM Sun 28 Jun 2015 16:56:44 BST

from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import numpy as nm
import cmath
import math
from timeit import default_timer as timer
from lc import colour_list 

start = timer()

X_MIN = -1.9
X_MAX =  1.9
Y_MIN = -1.7
Y_MAX =  1.7

'''
X_MIN = -0.2
X_MAX =  0.2
Y_MIN = -0.2
Y_MAX =  0.2
'''
offset     = 0.01
maxiter    = 100
calc_count = 0
rnum       = 3
#real_part  = -1 * ( math.pi / 5 )
#imag_part  = math.pi / 10
real_part  = -1.255
imag_part  =  0.0
C          = complex ( real_part, imag_part )  
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
randcolour = (255,255,0) # ( 90, 90, 90 )
img        = Image.new( "RGB", [ X_SIZE, Y_SIZE ], white )

mycolour = ( 100, 150, 200 ) 
x_pixel = 0
for X in nm.arange ( X_MIN, X_MAX, offset ):
	y_pixel = 0
	for Y in nm.arange ( Y_MIN, Y_MAX, offset ):
		Z = complex ( X, Y )
		iter = 0

		while ( abs ( Z**2 ) < 4 and iter < maxiter ):
			Z = Z**2 + C
			iter = iter + 1
			#print X, Y , Z
			calc_count = calc_count + 1  
		#mycolour = ( 155,  255, 3 + iter ) 
		#mycolour = colour_list[ iter % len( colour_list ) ]
		mycolour = colour_list[ iter % lenlc  ]
		#mycolour = colour_list[ iter + 9  ]
		#mycolour = ( 13 * iter, 23 * iter, 33 * iter )
		#img.putpixel( ( x_pixel,  y_pixel ), mycolour ) 
		#print x_pixel,  y_pixel, mycolour
		#print iter,
                if ( iter <= 2 ):
                        try:
                                img.putpixel( ( x_pixel,  y_pixel ), white ) 
                        except:
                                print 'Err: X,Y', x_pixel,  y_pixel
                                #pass
                elif ( iter == maxiter ):
                        img.putpixel( ( x_pixel,  y_pixel ), randcolour ) 
                else:
                        img.putpixel( ( x_pixel,  y_pixel ), mycolour ) 
	
		y_pixel += 1

	x_pixel += 1
	#print

dt = timer() - start

MsgText = 'Julia for Z^2 +' + str( C )

draw = ImageDraw.Draw(img)
font = ImageFont.truetype( "/Library/Fonts/Arial.ttf", 12 )
draw.text( ( 0, 0 ),  MsgText, ( 139,0,0 ), font=font )

print 'Julia for', C, 'and Rand:', rnum, 'created in %f s' % dt
print 'Calc: ', calc_count
img.show()
#img.save( 'Gaston_Julia.png' )
