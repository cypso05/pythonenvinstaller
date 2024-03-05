# Python Virtual Enviroment installer with Docker. 
This Python script is meant to install a specified version of Python and optionally Docker in a new virtual environment on the selected drive on the users machine. 

It first defines a Flask web application that will handle the user interface and call the install functions. The index route displays a form for selecting the Python version, drive, environment name, and whether to install Docker. On form submit, it calls the install_script function to perform the installation and displays a success or error page.

The get_available_drives function scans the system drives and returns a list of drive letters that exist. This populates the drive selection dropdown in the form.

The install_script function takes the user selections and does the following:

Creates a new folder called ScriptInstaller on the selected drive to hold the installation.

Creates a Python virtual environment in a venv subfolder using the venv module. This isolates the Python installation from the system Python.

# what the script can not do at the moment!!

# - The script can not Activate the virtual environment or upgrades pip, ( installs the native Python version on the users PC in the newly created Virtual enviroment which is not what we want to achieve)  This makes that global Python version available in the venv.

#-  If Docker installation was selected, it should generate a Dockerfile that uses the installed Python version as its base image. This Dockerfile could be used to containerize an application using the venv Python. and this part needs to be fixed as well. 

Any errors during the installation are caught and displayed on the error page.

# Overall, this should  allow the user to easily install a specific Python version and Docker to a custom location on their system through a web interface. The virtual environment keeps it isolated from the system Python. The code should handle the installation process end-to-end.

# I welcome any suggestions or ideas to improve this script so the user gets the desired end results. Right now the script only creates three different virtual enviroments in three seeparate folders all having just a virtual enviroment with the native python on the users PC rather than any python version desired and selected from the index.html page. 
