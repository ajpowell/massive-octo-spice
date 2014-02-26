#!/usr/bin/python

from BNG import to_osgb36, from_osgb36
from EN2lnglat import OSGB36toWGS84

ngr='NT275729'

print ngr

E, N = to_osgb36(ngr)
#    (327550, 672950)
print E
print N
   
lat, lon = OSGB36toWGS84(float(E), float(N))

print lat
print lon
