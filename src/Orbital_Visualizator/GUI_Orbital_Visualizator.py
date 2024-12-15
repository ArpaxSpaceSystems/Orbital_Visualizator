def submit_parameters(option:StringVar, entry_tle:Text, name_tle:Text, entry_param:list[Entry], window:Tk, Orbital_Parameters:list[Union[float, str]]) -> None:
    """
        Handles the submission of orbital parameters from the user interface.

        This method is triggered when the submit button is clicked.
        This function is triggered when the submit button is clicked. It extracts
        and validates user inputs from the provided widgets, then updates the global Orbital_Parameters list.
        Used within the `select_data()` method.

        :param option: A `tkinter.StringVar` holding the user's choice between TLE and direct orbital parameters
        :param entry_tle: A `tkinter.Text` widget containing the two lines element
        :param name_tle: A `tkinter.Text` widget containing the name of the satellite
        :param entry_param: A list of `tkinter.Entry` widgets for direct orbital parameters
        :param window: The `tkinter.Tk` instance of the user interface window.
        :param Orbital_Parameters: A global list to store the keplerian orbital parameters including TLE data or direct parameters.
        :return: None. The parameters are directly appended to the `Orbital_Parameters` list.
    """
    mu_Earth = 398600.4418  # km^3 / s^2
    if option.get() == "TLE":
        tle_line_1 = entry_tle.get("1.0", "1.end").strip()
        tle_line_2 = entry_tle.get("2.0", "2.end").strip()
        if ((tle_line_1)and(tle_line_2)and(name_tle)):
            satellite = EarthSatellite(tle_line_1, tle_line_2, name_tle.get())
            Orbital_Parameters.append((mu_Earth / (2*np.pi/(((2*np.pi/(satellite.model.no_kozai*60))*3600)))**2)**(1/3))
            Orbital_Parameters.append(satellite.model.ecco)
            Orbital_Parameters.append(satellite.model.inclo)        #in radian
            Orbital_Parameters.append(satellite.model.nodeo)        #in radian
            Orbital_Parameters.append(satellite.model.argpo)        #in radian
            Orbital_Parameters.append(satellite.model.mo)           #in radian
            Orbital_Parameters.append(satellite.name)
            window.destroy()
        else:
            Orbital_Parameters.clear()
            messagebox.showwarning("Error", "Please enter a valid TLE and a name.")
    else:
        
        for i in range(6):
            if entry_param[i].get():
                Orbital_Parameters.append(float(entry_param[i].get()))
            else:
                break
        Orbital_Parameters.append(entry_param[6].get())
        if all(element for element in Orbital_Parameters):
            window.destroy()
        else:
            Orbital_Parameters.clear()
            messagebox.showwarning("Error", "Please enter valid numerical values for orbital parameters.")
        

def toggle_fields(option:StringVar, label:Label, entry:Text, label_name:Label, name:Entry, parameters:Frame)->None:    #function to determine visibility of fields depending on the chosen option
    """
        Manages visibility of fields in the GUI based on the choice made by the user: either TLE or direct orbital parameters.
        It is used within the `select_data()` method.

        :param option: A `tkinter.StringVar` containing the user's choice ("TLE" or "direct").
        :param label: A `tkinter.Label` widget for the TLE input
        :param entry: A `tkinter.Text` widget where TLE data is entered.
        :param label_name: A `tkinter.Label` widget for the satellite's name (TLE option).
        :param name: A `Entry` tkinter.widget for entering the satellite's name (TLE option).
        :param parameters: A `tkinter.Frame` widget containing all input fields for direct orbital parameters.
        :return: None. The function directly modifies the visibility of the provided widgets.
    """
    if option.get() == "TLE":
        label.pack(pady=5)
        entry.pack(pady=5)
        label_name.pack(padx=5, pady=5)
        name.pack(padx=5, pady=5)
        parameters.pack_forget()
    else:
        label.pack_forget()
        entry.pack_forget()
        label_name.pack_forget()
        name.pack_forget()
        parameters.pack(pady=10)

def select_data(Orbital_Parameters: list)->None:              #function to open an user interface to give orbital parameters
    """
        Configures and displays the GUI to enter TLE or direct orbital parameters.

        This method launches a GUI to allow the user to enter either TLE or direct orbital parameters (keplerian).
        The provided data are saved into the `Orbital_Parameters` list. 
        :param Orbital_Parameters: A list containing the global orbital parameters
        :return: None. This function modifies the `Orbital_Parameters` list directly.
    """    
    label=['Major axis (a) [km] : ','Eccentricity (e) :','Inclination (i) [rad] :','RAAN [rad] :','Periapsis argument [rad] :','True anomalie (M) [rad] :','Name of the satellite: ']
    Orbital_Parameters_Variable=['a','e','i','RAAN','OMEGA','M','name']
    entry_window = tk.Tk()      #main window creation
    entry_window.title('Orbital parameters selection')
    icone = tk.PhotoImage(file="Orbito_Logo.png")
    entry_window.iconphoto(True, icone)

    #TLE
    tles_option = tk.StringVar(value="TLE")     #TLE or parameters choice variable
    frame_options = tk.Frame(entry_window)
    frame_options.pack(pady=10)      #Frame for TLE
    label_option = tk.Label(frame_options, text="Choose an option :")
    label_option.pack(side=tk.LEFT)
    radio_tle = tk.Radiobutton(frame_options, text="TLE", variable=tles_option, value="TLE")
    radio_tle.pack(side=tk.LEFT)
    radio_parametres = tk.Radiobutton(frame_options, text="Orbital parameters", variable=tles_option, value="Paramètres Orbitaux")
    radio_parametres.pack(side=tk.LEFT)
    label_tle = tk.Label(entry_window, text="Please enter TLE (in two lines):")
    label_tle.pack(pady=5) #Text box for TLE
    entry_tle = tk.Text(entry_window, width=70, height=2)
    entry_tle.pack(pady=5)
    entry_name_label= tk.Label(entry_window, text="Name of the satellite")
    entry_name_label.pack(padx=5, pady=5)
    entry_name_value=tk.Entry(entry_window)
    entry_name_value.pack(padx=5, pady=5)

    #Direct ortibal parameters
    frame_parameters = tk.Frame(entry_window)
    frame_parameters.pack(pady=10)    #Direct orbital parameters frame

    for i in range(7):
        label[i]= tk.Label(frame_parameters, text=label[i])
        label[i].grid(row=i, column=0, padx=5, pady=5)
        Orbital_Parameters_Variable[i]=tk.Entry(frame_parameters)
        Orbital_Parameters_Variable[i].grid(row=i, column=1, padx=5, pady=5)

    tles_option.trace("w", lambda *args: toggle_fields(tles_option, label_tle, entry_tle, entry_name_label, entry_name_value, frame_parameters))    #line to update visibility of field according to option chosen (TLE or direct parameters)

    btn_submit = tk.Button(entry_window, text="Submit", command=lambda: submit_parameters(tles_option, entry_tle, entry_name_value,Orbital_Parameters_Variable,entry_window, Orbital_Parameters))
    btn_submit.pack(pady=20) #Button for submission

    toggle_fields(tles_option, label_tle, entry_tle, entry_name_label, entry_name_value, frame_parameters)  # Initialize visible fields
    entry_window.mainloop()     #Keep the user interface opened
