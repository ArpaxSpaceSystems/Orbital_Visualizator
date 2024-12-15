from Keplerian2Cartesian import Orbit_Calculation


x,y,z=Orbit_Calculation(orbital_parameters=[36000,0.00025,0.45,0.48,0.58,1.25,"Test_Probe"],theta=1.25)

print('X : ',x)
print('Y : ',y)
print('Z : ',z)    