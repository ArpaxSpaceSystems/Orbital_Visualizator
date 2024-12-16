Orbital Visualizator Documentation
===================================

Master file, created by `sphinx-quickstart` on Mon Dec 16 20:58:58 2024.
This file contains the complete documentation for the Orbital Visualizator package.

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   modules
   examples
   tests

Introduction
------------

The **Orbital Visualizator** package provides tools for graphical representation of a satellite's orbit around a central body. Users can input either a TLE (Two Line Elements) or Keplerian parameters to generate 3D visualizations. 

### Package Overview

The package consists of the following modules:
- **`orbital_visualization_app`**: Main application module to invoke the GUI and plot orbits.
- **`gui_orbital_visualizator`**: Handles GUI interactions and data submissions.
- **`keplerian_to_cartesian_convertor`**: Converts Keplerian orbital parameters to Cartesian coordinates.
- **`plot_orbital_visualization`**: Visualizes orbits and central bodies in 3D.

Additionally, an example implementation is available in:
- **`__main__`**

Modules and Functions
---------------------

### `orbital_visualization_app`

.. toctree::
   :maxdepth: 1

This module provides a graphical user interface for entering orbital data and visualizing the orbit.

#### Key Functions

**`orbit_visualizator(source="tle")`**  
Launches the GUI for orbit visualization based on TLE or Keplerian parameters.  
**Parameters**:
- `source` (str): Input format, either `"tle"` or `"keplerian"` (default: `"tle"`).  
**Returns**: None.

---

### `gui_orbital_visualizator`

.. toctree::
   :maxdepth: 1

Manages the graphical interface, including data input, toggling visibility, and submitting parameters.

#### Key Functions

**`submit_parameters(option, entry_tle, name_tle, entry_param, window, orbital_parameters)`**  
Handles submission of user inputs from the GUI.  
**Parameters**:
- `option` (str): User's choice of input type ("tle" or "keplerian").
- `entry_tle` (`tkinter.Text`): Widget for TLE data.
- `name_tle` (`tkinter.Text`): Widget for satellite name.
- `entry_param` (list): Entry widgets for direct orbital parameters.
- `window` (`tkinter.Tk`): GUI window.
- `orbital_parameters` (list): Global list to store orbital parameters.  
**Returns**: None.

**`toggle_fields(option, label, entry, label_name, name, parameters)`**  
Toggles visibility of fields based on user input type.  

---

### `keplerian_to_cartesian_convertor`

.. toctree::
   :maxdepth: 1

Converts Keplerian parameters to Cartesian coordinates in the J2000 inertial frame.

#### Key Functions

**`orbit_calculation(orbital_parameters, theta)`**  
Computes Cartesian coordinates from Keplerian parameters.  
**Parameters**:
- `orbital_parameters` (list): List of Keplerian parameters.
- `theta` (float or `np.ndarray`): True anomaly.  
**Returns**: Tuple of Cartesian coordinates (x, y, z).

---

### `plot_orbital_visualization`

.. toctree::
   :maxdepth: 1

Provides 3D visualization tools for orbits and central bodies.

#### Key Functions

**`plot_central_body(space, radius, color)`**  
Plots the central body (e.g., Earth).  
**Parameters**:
- `space` (`Axes3D`): 3D plot axis.
- `radius` (float): Radius of the central body (e.g., 6371 km for Earth).
- `color` (str): Color of the central body.  
**Returns**: None.

**`plot_orbit(space, orbital_parameters)`**  
Plots the satellite's orbit based on Keplerian parameters.  
**Parameters**:
- `space` (`Axes3D`): 3D plot axis.
- `orbital_parameters` (list): Keplerian orbital parameters.  
**Returns**: None.

---

Examples
--------

### `__main__`

.. toctree::
   :maxdepth: 1

The main method demonstrates how to run the package.  
**Usage**:  
```bash
python src/__main__.py