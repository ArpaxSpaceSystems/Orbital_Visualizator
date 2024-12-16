#from src.orbital_visualizator.orbital_visualizator_app import orbit_visualizator
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from src.orbital_visualizator.plot_orbital_visualizator import plot_orbit

#orbit_visualizator()

def test_display():
    fig = plt.figure()
    space = fig.add_subplot(111, projection="3d")
    
    plot_orbit(space,orbital_parameters=[36000,0.00025,0.45,0.48,0.58,1.25,"Test_Probe"])