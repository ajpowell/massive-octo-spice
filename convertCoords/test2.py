#!/usr/bin/python

from BNG import to_osgb36, from_osgb36

print "test2.py"

print ""
print "Testing BNG library..."
print ""

orig_osmapref = 'NT2755072950'

print "  to_osgb36()"
e,n =  to_osgb36(orig_osmapref)
#    (327550, 672950)
if e == 327550:
  print "    Eastings  : OK"
else:
  print "    Eastings  : Failed"
  
if n == 672950:
  print "    Northings : OK"
else:
  print "    Northings : Failed" 

print "  from_osgb36()"
osmapref = from_osgb36((327550, 672950),10)
#    'NT276730'

if osmapref == orig_osmapref:
  print "    OSMapRef  : OK"
else:
  print "   OSMapRef : Failed"