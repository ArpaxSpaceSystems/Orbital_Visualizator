.. Orbital Visualizator documentation master file, created by
   sphinx-quickstart on Mon Dec 16 20:58:58 2024.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Orbital Visualizator documentation
==================================



.. toctree::
   :maxdepth: 2
   :caption: Contents: 
   
This documentation contains all methods and functions used in the Orbital Visualizator package. This package 
aims to give a graphic representation of an orbite of a satellite around a central body. For this, the user is asked to input either
a TLE (Two Line Elements) or directly from Keplerian parameters.
This package contains the following modules:
* orbital_visualization_app
* gui_orbital_visualizator
* keplerian_to_cartesian_convertor
* plot_orbital_visualization
   
It also contains an example file:
* __main__



Modules and functions explanations
----------------------------------

orbital_visualization_app
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. toctree::

   This module allows to invoke a graphic user interface and plot the entered orbit around Earth.



`orbit_visualizator(source="tle"):`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. toctree::

    Opens the tool to visualize an orbit from TLE or direct keplerian parameters.

    This method launches  GUI provided by the `select_data()` method allowing the user to enter
    orbital parameters (either TLE and direct orbital parameters).
    It creates a 3D representation of considered orbit and the central body (e.g., Earth) using
    `plot_orbit()` and `plot_central_body()` methods.

    **Warning:** As this project is in its early phase of development, no validation is
    implemented to verify the relevance or correctness of the user-provided values.
    
    :param source: A string to choose format of input data, should be 'tle' or 'keplerian', default
    is 'tle'
    :return: None. The orbit, the satellite's position and the central body are directly displayed
    on the created 3D object.


gui_orbital_visualizator
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. toctree::

   This module contains all functions to handle the graphic user interface including invoking
    a window, manage visibility within this GUI and handle submission of data entered by user in
    window's text widgets.


`submit_parameters(
    option: str,
    entry_tle: Text,
    name_tle: Text,
    entry_param: list[Entry],
    window: Tk,
    orbital_parameters: list[Union[float, str]],
) -> None:`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. toctree::

    Handles the submission of orbital parameters from the user interface.

    This method is triggered when the submit button is clicked.
    This function is triggered when the submit button is clicked. It extracts
    and validates user inputs from the provided widgets, then updates the global
    Orbital_Parameters list.
    Used within the `select_data()` method.

    :param option: A string holding the user's choice between tle and keplerian
    :param entry_tle: A `tkinter.Text` widget containing the two lines element
    :param name_tle: A `tkinter.Text` widget containing the name of the satellite
    :param entry_param: A list of `tkinter.Entry` widgets for direct orbital parameters
    :param window: The `tkinter.Tk` instance of the user interface window.
    :param Orbital_Parameters: A global list to store the keplerian orbital parameters including
    TLE data or direct parameters.
    :return: None. The parameters are directly appended to the `Orbital_Parameters` list.


`toggle_fields(
    option: str,
    label: Label,
    entry: Text,
    label_name: Label,
    name: Entry,
    parameters: Frame,
) -> None:`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. toctree::

    Manages visibility of fields in the GUI based on the choice made by the user: either
    TLE or direct orbital parameters.
    It is used within the `select_data()` method.

    :param option: A string containing the user's choice ("tle" or "keplerian").
    :param label: A `tkinter.Label` widget for the TLE input
    :param entry: A `tkinter.Text` widget where TLE data is entered.
    :param label_name: A `tkinter.Label` widget for the satellite's name (TLE option).
    :param name: A `Entry` tkinter.widget for entering the satellite's name (TLE option).
    :param parameters: A `tkinter.Frame` widget containing all input fields for direct orbital
     parameters.
    :return: None. The function directly modifies the visibility of the provided widgets.


`select_data(orbital_parameters: list, tles_option: str) -> None:`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. toctree::

    Configures and displays the GUI to enter TLE or direct orbital parameters.

    This method launches a GUI to allow the user to enter either TLE or direct orbital
    parameters (keplerian).
    The provided data are saved into the `Orbital_Parameters` list.
    :param Orbital_Parameters: A list containing the global orbital parameters
    :param tles_option: A string to choose format of input data, should be 'tle' or 'keplerian'
    :return: None. This function modifies the `Orbital_Parameters` list directly.


`select_data(orbital_parameters: list, tles_option: str) -> None:`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. toctree::

    Configures and displays the GUI to enter TLE or direct orbital parameters.

    This method launches a GUI to allow the user to enter either TLE or direct orbital
    parameters (keplerian).
    The provided data are saved into the `Orbital_Parameters` list.
    :param Orbital_Parameters: A list containing the global orbital parameters
    :param tles_option: A string to choose format of input data, should be 'tle' or 'keplerian'
    :return: None. This function modifies the `Orbital_Parameters` list directly.




keplerian_to_cartesian_convertor
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. toctree::

   This module is used to convert Keplerian parameters into Cartesian parameters in the J2000
    frame.


`orbit_calculation(
    orbital_parameters: list, theta: Union[float, np.ndarray]
) -> Tuple[Union[float, np.ndarray], ...]:`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. toctree::

    Converts Keplerian parameters into Cartesian coordinates in the inertial frame J2000.

    :param orbital_parameters: List of Keplerian parameters provided by the user.
    :param theta: The true anomaly of the satellite. This can be a float (for a specific
    position)or an np.ndarray (for orbit propagation over time).
    :return: Cartesian coordinates (x, y, z) of the orbit in the inertial frame J2000.
    The output type matches the input `theta` (float or np.ndarray).


plot_orbital_visualization
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. toctree::

   This module allows to plot central bodies, satellites' orbits and position in a 3D 
   representation.


`plot_central_body(space: Axes3D, radius: Union[int, float], color: str) -> None:`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. toctree::

    Plots the surface of the central body around which the satellite orbits.

    :param space: The 3D matplotlib axes (Axes3D) where the central body will be plotted.
    :param radius: the radius of the central body in km (e.g. 6371 km for Earth).
    :param color: the color of the sphere representing the central body.
    :return: None.

`plot_orbit(space: Axes3D, orbital_parameters: list) -> None:`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. toctree::

    Displays the orbit based on the Keplerian orbital parameters provided by the user in
    the specified domain.
    It also display the satellite's position based on its mean anomaly angle.

    :param space: The 3D matplotlib axes (Axes3D) where the central body will be plotted.
    :param orbital_parameters: A list containing all Keplerian orbital parameters entered by the
    user in the following format ['Major axis (a)[km]','Eccentricity (e)','Inclination (i) [rad]',
    'RAAN [rad]','Periapsis argument [rad]','True anomalie (M) [rad]','Name of the satellite'].
    :return: None. The orbit and satellite position are displayed directly on the provided Axes3D
    object.




__main__
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. toctree::

   This is the main method and it runs as an exemple. It can be executed directly in the 
   prompt using python `src/__main__.py` command.


`main()`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. toctree::

    Execute the main method of this package

    :param: None.
    :return: None.