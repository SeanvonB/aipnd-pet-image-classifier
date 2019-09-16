# !/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# PROGRAMMER: Sean von Bayern
# DATE CREATED: Sept. 13, 2019
# REVISED DATE: 
#
# PURPOSE:
#   Create the function get_pet_labels that creates the pet labels from
#   the image's filename. This function creates and returns the results
#   dictionary as results_dic within get_pet_labels function and as results
#   within main. The results_dic dictionary has a 'key' that's the image
#   filename and a 'value' that's a list. This list will contain the
#   following item at index 0 : pet image label (string).

# Import python modules
from os import listdir

# Clean file names to a set standard:
def clean_name(name):

    # Set all lowercase
    name = name.lower()

    # Replace underscores with spaces
    split_name = name.split("_")

    # Remove non-alphabetical file details on label
    label = ""
    for word in split_name:
        if word.isalpha():
            label += word + " "

    # Remove leading/trailing spaces
    label = label.strip()

    # Return cleaned name
    return label

# Create results dictionary
def get_pet_labels(images_dir):
    """
    Parameters:
     image_dir - The (full) path to the folder of images that are to be
                 classified by the classifier function (string)
    Returns:
      results_dic - Dictionary with 'key' as image filename and 'value' as a 
      List. The list contains for following item:
         index 0 = pet image label (string)
    """

    # Create empty dictionary
    results_dic = {}

    # Create list of file names to be added
    file_names = listdir(images_dir)

    # Process list into file_name:label dictionary
    for name in file_names:

        # Skip hidden files
        if name[0] != ".":

            # Add to dictionary with cleaned label (if new)
            if name not in results_dic:
                results_dic[name] = [clean_name(name)]
            else:
                print(name + " already exists in dictionary")

    # Return file_name:label dictionary
    return results_dic
