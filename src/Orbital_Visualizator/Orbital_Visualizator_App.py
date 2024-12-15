from Plot_Orbital_Vizualizator import plot_central_body, plot_orbit
from GUI_Orbital_Visualizator import select_data
import matplotlib.pyplot as plt


def Orbit_Visualizator(): #with entenred parameter or TLE
    """
        Open the tool to visualize an orbit from TLE or direct keplerian parameters.

        This method launches  GUI provided by the `select_data()` method allowing the user to enter orbital parameters (either TLE and direct orbital parameters).
        It creates a 3D representation of considered orbit and the central body (e.g., Earth) using `plot_orbit()` and `plot_central_body()` methods.

        **Warning:** As this project is in its early phase of development, no validation is implemented
        to verify the relevance or correctness of the user-provided values.

        :param: None.
        :return: None. The orbit, the satellite's position and the central body are directly displayed on the created 3D object.        
    """
    #Variables definition
    Orbital_Parameters=[]       #under the format [a, e, i, RAAN, Omega, M,name]

    #Figure configuration
    fig = plt.figure()
    space = fig.add_subplot(111, projection='3d')

    select_data(Orbital_Parameters)       #call user interface for data inputs

    if not Orbital_Parameters:          #exit the function if the user interface is closed
        return

    lim = 1.25*Orbital_Parameters[0]     #define max range of the plot (considered 1.25 time the size of semi-major axis length)
    space.set_xlim([-lim, lim]); space.set_ylim([-lim, lim]); space.set_zlim([-lim, lim])

    space.set_xlabel('X in km'); space.set_ylabel('Y in km'); space.set_zlabel('Z in km')

    space.set_title('Orbit visualization around Earth of ' +str(Orbital_Parameters[6])+ ' in EQJ2000 frame')
    space.set_box_aspect([1, 1, 1])

    plot_orbit(space, Orbital_Parameters)
    plot_central_body(space, radius=6371, color='b') #plot of the central body

    plt.show() #Show space with the central body and orbit considered