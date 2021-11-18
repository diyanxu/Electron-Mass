import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

# Function to calculate electromagnetic field value
def electromag_func():
    return None


# Function for error calculation
def electromag_error_func():
    return None


# Model function for constant voltage
def volt_model():
    return None


# Model function for constant current
def current_model():
    return None


# main function
if __name__ == "__main__":
    # loading data
    data_voltage = np.loadtxt('data/constant_volts.txt', skiprows=1)
    data_current = np.loadtxt('data/constant_current.txt', skiprows=1)

    # parsing constants and errors
    voltage_const = data_voltage[0][0]
    voltage_const_error = data_voltage[0][1]
    current_const = data_current[0][0]
    current_const_error = data_current[0][1]

    # parsing data for voltage constant
    voltage_const_currents = data_voltage[:,2]
    voltage_const_currents_error = data_voltage[:,3]
    voltage_const_rad = data_voltage[:,4]
    voltage_const_rad_error = data_voltage[:,5]

    # parsing data for current constant
    current_const_voltage = data_current[:,2]
    current_const_voltage_error = data_current[:,3]
    current_const_rad = data_current[:,4]
    current_const_rad_error = data_current[:5]

    
