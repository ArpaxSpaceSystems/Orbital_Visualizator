.. Orbital Visualizator documentation master file, created by
   sphinx-quickstart on Mon Dec 16 20:58:58 2024.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Orbital Visualizator documentation
==================================

This document explain how to install Orbital Visualizator tool via pip.

This documentation contains all methods and functions used in the Orbital Visualizator package. This package 
aims to give a graphic representation of an orbite of a satellite around a central body. For this, the user is asked to input either
a TLE (Two Line Elements) or directly from Keplerian parameters.

It contains 4 modules and 1 main as example:

- orbital_visualization_app
- gui_orbital_visualizator
- keplerian_to_cartesian_convertor
- plot_orbital_visualization
- __main__


There are also instructions at the end about testing.

**Warning** ``test_visualization`` **test requires interaction as it involves graphic user interface. For the test, a TLE can can be found in** ``tle_example.txt``.



Installation
------------

Pip install
^^^^^^^^^^^

It is possible to install ``orbital_visualizator`` directly through the pip install command.
To install Orbital Visualizator, type ``pip install orbital_visualizator`` in the command. It can also be found at https://pypi.org/project/Orbital-Visualizator/0.1/ .

Import in Python project
^^^^^^^^^^^^^^^^^^^^^^^^

Then to import it in your Python project type ``import orbital_visualizator``.


Example
^^^^^^^

For exemple, to directly open the tool. The following code can be implemented:

``from orbital_visualizator.orbital_visualizator_app import orbit_visualizator
Orbit_visualizator('keplerian')``


Modules and functions explanations
----------------------------------

orbital_visualization_app
^^^^^^^^^^^^^^^^^^^^^^^^^

This module allows to invoke a graphic user interface and plot the entered orbit around Earth.


orbit_visualizator(
     source="tle")->None:
~~~~~~~~~~~~~~~~~~~~~~~~~

Opens the tool to visualize an orbit from TLE or direct keplerian parameters.

This method launches  GUI provided by the ``select_data()`` method allowing the user to enter
orbital parameters (either TLE and direct orbital parameters).
It creates a 3D representation of considered orbit and the central body (e.g., Earth) using
``plot_orbit()`` and ``plot_central_body()`` methods.

**Warning:** As this project is in its early phase of development, no validation is
implemented to verify the relevance or correctness of the user-provided values.
    
:source: A string to choose format of input data, should be 'tle' or 'keplerian', default is 'tle'
:return: None. The orbit, the satellite's position and the central body are directly displayed on the created 3D object.


gui_orbital_visualizator
^^^^^^^^^^^^^^^^^^^^^^^^

This module contains all functions to handle the graphic user interface including invoking
a window, manage visibility within this GUI and handle submission of data entered by user in
window's text widgets.

submit_parameters(
    option: str,
    entry_tle: Text,
    name_tle: Text,
    entry_param: list[Entry],
    window: Tk,
    orbital_parameters: list[Union[float, str]],
) -> None:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


Handles the submission of orbital parameters from the user interface.

This method is triggered when the submit button is clicked.
This function is triggered when the submit button is clicked. It extracts
and validates user inputs from the provided widgets, then updates the global
Orbital_Parameters list.
Used within the ``select_data()`` method.

:option: A String holding the user's choice between tle and keplerian
:entry_tle: A ``tkinter.Text`` widget containing the two lines element
:name_tle: A ``tkinter.Text`` widget containing the name of the satellite
:entry_param: A list of ``tkinter.Entry`` widgets for direct orbital parameters
:window: The ``tkinter.Tk`` instance of the user interface window.
:orbital_parameters: A global list to store the keplerian orbital parameters including TLE data or direct parameters.
:return: None. The parameters are directly appended to the `Orbital_Parameters` list.




toggle_fields(
    option: str,
    label: Label,
    entry: Text,
    label_name: Label,
    name: Entry,
    parameters: Frame,
) -> None:
~~~~~~~~~~~~~~~~~~~~~~

Manages visibility of fields in the GUI based on the choice made by the user: either
TLE or direct orbital parameters.
It is used within the `select_data()` method.

:option: A String containing the user's choice ("tle" or "keplerian").
:label: A ``tkinter.Label`` widget for the TLE input
:entry: A ``tkinter.Text`` widget where TLE data is entered.
:label_name: A ``tkinter.Label`` widget for the satellite's name (TLE option).
:name: A ``Entry`` tkinter.widget for entering the satellite's name (TLE option).
:parameters: A ``tkinter.Frame`` widget containing all input fields for direct orbital parameters.
:return: None. The function directly modifies the visibility of the provided widgets.


select_data(orbital_parameters: list, tles_option: str) -> None:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Configures and displays the GUI to enter TLE or direct orbital parameters.

This method launches a GUI to allow the user to enter either TLE or direct orbital
parameters (keplerian).
The provided data are saved into the `Orbital_Parameters` list.

:orbital_parameters: A list containing the global orbital parameters
:tles_option: A string to choose format of input data, should be 'tle' or 'keplerian'
:return: None. This function modifies the `Orbital_Parameters` list directly.



keplerian_to_cartesian_convertor
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This module is used to convert Keplerian parameters into Cartesian parameters in the J2000
frame.


orbit_calculation(
    orbital_parameters: list, theta: Union[float, np.ndarray]
) -> Tuple[Union[float, np.ndarray], ...]:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Converts Keplerian parameters into Cartesian coordinates in the inertial frame J2000.

:orbital_parameters: List of Keplerian parameters provided by the user.
:theta: The true anomaly of the satellite. This can be a float (for a specific position)or an np.ndarray (for orbit propagation over time).
:return: Cartesian coordinates (x, y, z) of the orbit in the inertial frame J2000.
The output type matches the input `theta` (float or np.ndarray).


plot_orbital_visualization
^^^^^^^^^^^^^^^^^^^^^^^^^^

This module allows to plot central bodies, satellites' orbits and position in a 3D 
representation.


plot_central_body(space: Axes3D, radius: Union[int, float], color: str) -> None:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Plots the surface of the central body around which the satellite orbits.

:space: The 3D matplotlib axes (Axes3D) where the central body will be plotted.
:radius: the radius of the central body in km (e.g. 6371 km for Earth).
:color: the color of the sphere representing the central body.
:return: None.

plot_orbit(space: Axes3D, orbital_parameters: list) -> None:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Displays the orbit based on the Keplerian orbital parameters provided by the user in
the specified domain.
It also display the satellite's position based on its mean anomaly angle.

:space: The 3D matplotlib axes (Axes3D) where the central body will be plotted.
:orbital_parameters: A list containing all Keplerian orbital parameters entered by the user in the following format ['Major axis (a)[km]','Eccentricity (e)','Inclination (i) [rad]','RAAN [rad]','Periapsis argument [rad]','True anomalie (M) [rad]','Name of the satellite'].
:return: None. The orbit and satellite position are displayed directly on the provided Axes3D object.



main
^^^^

This is the main method and it runs as an exemple. It can be executed directly in the 
prompt using python ``src/__main__.py`` command.


main():
~~~~~~~

Execute the main method of this package

:param: None.
:return: None.



Testing
-------


There are 5 tests implemented in this package:

- test_keplerian_to_cartesian_convertor
- test_plot_orbit
- test_plot_planet
- test_submit_button
- test_visualization


test_keplerian_to_cartesian_convertor:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This test allows to verify the function orbit_calculation converts well Keplerian coordinates into Cartesian coordinates.

test_calcul_orbit()->None:
~~~~~~~~~~~~~~~~~~~~~~~~~~

This function test convertion from Keplerian to Cartesian coordinates for a satellite with the following orbit:

:a: 36000 km
:e: 0.00025
:i: 0.45 rad
:RAAN: 0.48 rad
:OMEGA: 0.58 rad
:M:  1.25 rad

These values were taken randomly just to check.

:param: None.
:return: None.

test_plot_orbit:
^^^^^^^^^^^^^^^^

This test allows to verify if the function plot_orbit doesn't crash.

test_display_orbit():
~~~~~~~~~~~~~~~~~~~~~

This function verifies that plot_orbit doesn't crash.

:param: None.
:return: None.

test_plot_planet:
^^^^^^^^^^^^^^^^^

This test allows to verify if the function plot_central_body doesn't crash.

test_display_planete():
~~~~~~~~~~~~~~~~~~~~~~~

This function verifies that plot_central doesn't crash.

:param: None.
:return: None.

test_submit_button:
^^^^^^^^^^^^^^^^^^^

These test allow to verify if the function submit_parameters well interpreted datas from user to good format data into Cartesian coordinates.


test_submit():
~~~~~~~~~~~~~~

This function verifies if the function submit_parameters well interpret datas from user to good format data
Data entered by user are the following:

For TLE  (ISS)

``1 25544U 98067A   14273.50403866  .00012237  00000-0  21631-3 0  1790
2 25544  51.6467 297.5710 0002045 126.1182  27.2142 15.50748592907666``

For keplerian

:a: 36000 km
:e: 0.002
:i: 0.25 rad
:raan: 0.35 rad
:omega: 0.56 rad
:m: 1.87 rad

:param: None.
:return: None.

test_visualization:
^^^^^^^^^^^^^^^^^^^

This test allows to verify if the function orbite_vizalization works properly without any bug.

test_application():
~~~~~~~~~~~~~~~~~~~

This function verifies if the function orbite_vizalization works properly without any bug.
Data entered by user are the following:
:datasource: "tle"

**Warning** This test requires interaction as it involves graphic user interface. For the test, a TLE can can be found in ``tle_example.txt``.

:param: None.
:return: None.

