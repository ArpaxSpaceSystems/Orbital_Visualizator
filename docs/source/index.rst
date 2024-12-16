.. Orbital Visualizator documentation master file, created by
   sphinx-quickstart on Mon Dec 16 20:58:58 2024.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Orbital Visualizator documentation
==================================

Add your content using ``reStructuredText`` syntax. See the
`reStructuredText <https://www.sphinx-doc.org/en/master/usage/restructuredtext/index.html>`_
documentation for details.


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