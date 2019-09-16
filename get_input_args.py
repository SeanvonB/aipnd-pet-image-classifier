# !/usr/bin/env python3
# -*- coding: utf-8 -*-
#                                                                             
# PROGRAMMER: Sean von Bayern
# DATE CREATED: Sept. 10, 2019
# REVISED DATE: 
#
# PURPOSE:
#   Create a function that retrieves the following 3 command line inputs
#   from the user using the Argparse Python module. If the user fails to
#   provide some or all of the 3 inputs, then the default values are
#   used for the missing inputs.

# Imports python modules
import argparse

# Collect and parse up to 3 command line arguments as run options
def get_input_args():
    """
    Command Line Arguments:
        1. Image Folder as --dir with default value "pet_images"
        2. CNN Model Architecture as --arch with default value "vgg"
        3. Text File with Dog Names as --dogfile with default value "dognames.txt"
    This function returns these arguments as an ArgumentParser object.
    Parameters:
        None - simply using argparse module to create & store command line arguments
    Returns:
        parse_args() - data structure that stores the command line arguments object
    """

    # Create parser
    parser = argparse.ArgumentParser(description="Accept run options")

    # Add argument to specify image directory
    parser.add_argument("-dir",
                        "--dir",
                        type=str,
                        default="./pet_images", 
                        help="path to image directory")

    # Add argument to specify CNN architcture
    parser.add_argument("-arch",
                        "--arch",
                        type=str,
                        default ="vgg",
                        help="name of architecture")

    # Add argument to specify file of dog names
    parser.add_argument("-dogfile",
                        "--dogfile",
                        "-df",
                        "--df",
                        type=str,
                        default ="./dognames.txt",
                        help="path to name file") 
    
    # Return parsed collection of arguments
    return parser.parse_args()
