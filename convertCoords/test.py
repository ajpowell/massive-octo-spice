#!/usr/bin/python

from BNG import to_osgb36, from_osgb36
from EN2lnglat import OSGB36toWGS84, WGS84toOSGB36

#ngr='NT275729'
ngr='SP28031820'

print ngr

E, N = to_osgb36(ngr)

print E
print N
   
lat, lon = OSGB36toWGS84(float(E), float(N))

print lat
print lon

E, N = WGS84toOSGB36(lat, lon)

print E
print N