import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

# Coil electromagnetic field expressed as a function of 1/r where x is 1/r
def field_coil_r_func(x, a, b):
    return x*a - b

#Function to calculate coil electromagnetic field
def field_coil_func(x):
    return ((4/5)**(3/2))*4*np.pi*(10**(-7))*130*x/0.15


# main function
if __name__ == "__main__":
    # loading data
    data_voltage = np.loadtxt('data/constant_volts.txt', skiprows=1)

    # parsing constants and errors
    voltage_const = data_voltage[0][0]
    voltage_const_error = data_voltage[0][1]

    # parsing data for voltage constant
    voltage_const_currents = data_voltage[:,2]
    voltage_const_currents_error = data_voltage[:,3]
    voltage_const_rad = data_voltage[:,4]
    voltage_const_rad_error = data_voltage[:,5]

    #data for the coil field at constant voltage
    field_coil = field_coil_func(voltage_const_currents)
    field_coil_error = field_coil*np.sqrt(((voltage_const_currents_error
                                            /voltage_const_currents)**2)+
                                          ((0.0025/0.15)**2))
    
    #Curve_fit on field_coil_r_func for external field, b
    popt, pcov = curve_fit(field_coil_r_func, 1/(voltage_const_rad/100),
                           field_coil, sigma=field_coil_error, 
                           absolute_sigma=True)
    pstd = np.sqrt(np.diag(pcov))
    
    print('slope = ', popt[0], '+-', pstd[0],', intercept = ', popt[1],'+-', 
          pstd[1])
    # plot code if needed
    '''
    #model data
    field_coil_r = field_coil_r_func(1/(voltage_const_rad/100), popt[0], popt[1])
    
    #plot
    plt.plot(1/voltage_const_rad, field_coil_r)
    '''