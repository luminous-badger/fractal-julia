#!/usr/bin/python

# Plot an image from a CSV file. xpix, ypix, iter.
# JM Wed 22 Nov 2017 21:39:59 GMT

import csv
from PIL import Image
from timeit import default_timer as timer
from bluelc import colour_list

start = timer()

lenlc      = len( colour_list )
rnum       = 43
maxiter    = 50
white      = (255,255,255)
randcolour = ( 70,130,180)

with open('/Users/johnmcloughlin/work/CPP/f1.csv') as f:
	reader = csv.reader(f)
	row1 = next(reader)

	print 'Row1:', row1	
	X_SIZE = row1[ 0 ]
	Y_SIZE = row1[ 1 ]

	X_SIZE = int( X_SIZE ) 
	Y_SIZE = int( Y_SIZE )

	print 'X_SIZE: ', X_SIZE
	print 'Y_SIZE: ', Y_SIZE
	img        = Image.new( "RGB", [ X_SIZE, Y_SIZE ], white )

	for row in reader:
		#print 'Row:', row
		x_pixel    = int( row[ 0 ] )
		y_pixel    = int( row[ 1 ] )
		iter_count = int( row[ 2 ] )

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
		'''
		#mycolour = ( iter_count % 13, iter_count % 23 , iter_count % 33 )
		mycolour = colour_list[ iter_count % lenlc ]
		img.putpixel( ( x_pixel,  y_pixel ), mycolour ) 


dt = timer() - start

print 'Test plot from CSV created in %f s' % dt
img.show()
#img.save( 'bJulia_076_011_purple.png' )

