import numpy as np
import matplotlib.pyplot as plt
from Import_Functions import import_npy
from Global_Units import IMAGE_PRAMS

#define a function that takes in a 2D array and finds the optimal threshold for background to signal threshold for intensity
def signal_threshold(data,threshold_guess,plot=False,ignore_zero=True,name=None):
    '''Docstring for signal_threshold

    Parameters:
    -----------
    data: 2D array
        The data to be analyzed, each index is a pixel with a value of the intensity of the pixel
    threshold_guess: int
        The initial guess for the threshold on the intensity value of a pixel
    plot: bool
        If True, the function will plot the original array with only pixels above the threshold value and a histogram of the intensities 
    ignore_zero: bool
        If True, the function will ignore all pixels with an intensity value of 0 when finding the optimal threshold value
    name: str
        The name of the array, used for the title of the histogram plot
    
    Returns:
    --------
    threshold: int
        The threshold value for the intensity of a pixel that separates background from signal
    thresholded_data: 2D array
        The data with only pixels above the threshold value

    '''
    #make a copy of the data
    data_copy = data.copy()
    #set all values below the threshold to 0
    data_copy[data_copy<threshold_guess] = 0
    #plot the histogram of the intensities of the pixels
    if plot:
        plt.hist(data.flatten()[data.flatten()>0],bins=20)
        #plot a vertical line at the threshold value
        plt.axvline(threshold_guess,color='r',label='Threshold Value')
        plt.legend()
        #label the axes
        plt.xlabel('Intensity')
        plt.ylabel('Number of Pixels')
        #make the title
        plt.title('Histogram of Intensities for the {0} channel'.format(name))
        plt.show()
    
    #make a imshow plot of the 2D array with only pixels above the threshold value and a second imshow plot the with the original array
    #make both of the plots in one figure but on two different axes
    if plot:
        fig,ax = plt.subplots(1,2,figsize=(15,5))
        #plot the array with only pixels above the threshold value
        ax[0].imshow(data_copy)
        #label the axes
        ax[0].set_xlabel('X Position (Pixels)')
        ax[0].set_ylabel('Y Position (Pixels)')
        #make the title
        ax[0].set_title('Array with Pixels Below Threshold Removed  \n Threshold = {0} for channel {1}'.format(threshold_guess,name))
        #plot the original array
        ax[1].imshow(data)
        #label the axes
        ax[1].set_xlabel('X Position (Pixels)')
        ax[1].set_ylabel('Y Position (Pixels)')
        #make the title
        ax[1].set_title('Original Array')
        plt.show()

    return threshold_guess,data_copy

#define a function which takes a 2D array and a intensity threshold and returns the array with the following modifications:
#1. all pixels below the threshold are set to 0
#2. all pixels above the threshold are set to 1
def threshold_array(data,threshold):
    '''Docstring for threshold_array

    Parameters:
    -----------
    data: 2D array
        The data to be analyzed, each index is a pixel with a value of the intensity of the pixel
    threshold: int
        The threshold value for the intensity of a pixel that separates background from signal
    
    Returns:
    --------
    thresholded_data: 2D array
        The data with only pixels above the threshold value

    '''
    #make a copy of the data
    data_copy = data.copy()
    #set all values below the threshold to 0
    data_copy[data_copy<threshold] = 0
    #set all values above the threshold to 1
    data_copy[data_copy>threshold] = 1
    return data_copy

#define a function to take two 2D arrays of 0s and 1s and apply a and gate to them
def and_gate(data1,data2,*args):

    '''Docstring for and_gate

    Parameters:
    -----------
    data1: 2D array
        The first data to be analyzed, each index is a pixel with a value of 1 or 0
    data2: 2D array
        The second data to be analyzed, each index is a pixel with a value of 1 or 0
    *args: 2D array
        Any number of additional arrays to be analyzed, each index is a pixel with a value of 1 or 0
    Returns:
    --------
    and_data: 2D array
        and operation of the two arrays

    '''
    #check to see how many more arrays are being passed in
    if len(args) == 0:
        #if there are no additional arrays, just do the and operation on the two arrays
        and_data = np.logical_and(data1,data2)
    else:
        #if there are additional arrays, do the and operation on the first two arrays and then do the and operation on the result and the next array
        and_data = np.logical_and(data1,data2)
        for i in range(len(args)):
            and_data = np.logical_and(and_data,args[i])
    return and_data