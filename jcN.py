#!/usr/bin/python

# Plot 'brot using PIL / Pillow. Plots x,y, not y,x as does pylab.
# JM Mon  5 Jan 2015 15:11:32 GMT
# For 1, L, and I images, use integers. For RGB images, use a 3-tuple containing integer values. 
# For F images, use integer or floating point values.
# Julias for Z^N.
# JM Wed  1 Mar 2017 15:38:40 GMT

from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import numpy as nm
import cmath
from timeit import default_timer as timer
from lc import colour_list
import sys

start = timer()

X_MIN = -1.7
X_MAX =  1.7
Y_MIN = -1.2
Y_MAX =  1.2
offset     = 0.005
maxiter    = 1975
calc_count = 0
rnum       = 63
ZPower     = 1.8
#C          = complex ( -0.91217, 0.39721 ) # Nice for z^7
CInpt      = float( sys.argv[ 1 ] )
C          = complex ( -0.451, CInpt )

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
randcolour = (250,250,210) 
img        = Image.new( "RGB", [ X_SIZE, Y_SIZE ], white )
lenlc      =  len( colour_list ) 

mycolour = ( 100, 150, 200 ) 
x_pixel = 0
for X in nm.arange ( X_MIN, X_MAX, offset ):
	y_pixel = 0
	for Y in nm.arange ( Y_MIN, Y_MAX, offset ):
		Z = complex ( X, Y )
		iter_count = 0

		while ( abs ( Z**ZPower ) < 4 and iter_count < maxiter ):
			Z = Z**ZPower + C
			iter_count = iter_count + 1
			#print X, Y , Z
			calc_count = calc_count + 1  
		'''
		mycolour = ( 13 * iter_count, 23 * iter_count, 33 * iter_count ) 
		img.putpixel( ( x_pixel,  y_pixel ), mycolour ) 
		'''
		if ( iter_count + rnum  >= lenlc ):
			mycolour = colour_list[ iter_count % lenlc ]
		else:	
			mycolour = colour_list[ iter_count + rnum  ]
		
		if ( iter_count <= 2 ):
			try:
				img.putpixel( ( x_pixel,  y_pixel ), white ) 
			except:
				print 'Err: X,Y', x_pixel,  y_pixel
				#pass
		elif ( iter_count == maxiter ):
			img.putpixel( ( x_pixel,  y_pixel ), randcolour ) 
		else:
			img.putpixel( ( x_pixel,  y_pixel ), mycolour ) 
		y_pixel += 1

	x_pixel += 1

dt = timer() - start

MsgText = 'Julia for Z^' + str( ZPower ) + '+' + str( C ) + ' CO: ' + str( rnum ) 

draw = ImageDraw.Draw(img)
font = ImageFont.truetype( "/Library/Fonts/Arial.ttf", 12 )
draw.text( ( 0, 0 ),  MsgText, ( 139,0,0 ), font=font )

print 'Julia for: Z^', ZPower, '+', C, 'and colour offset', rnum, 'created in %f s' % dt
print 'Calc: ', calc_count
Fname = 'Julia_Ze' + str ( ZPower ) + str ( C.real ) + '+' + str ( C.imag ) + 'i.png'
print 'Fname:', Fname
img.show()
#img.save( Fname )

