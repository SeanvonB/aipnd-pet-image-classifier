# !/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# PROGRAMMER: Sean von Bayern
# DATE CREATED: Sept. 17, 2019
# REVISED DATE: 
#
# PURPOSE:
#   Create a function adjust_results_isadog that adjusts the results
#   dictionary to indicate whether or not the pet image label is of-a-dog,
#   and to indicate whether or not the classifier image label is of-a-dog.
#   This function inputs:
#       -The results dictionary as results_dic within adjust_results_isadog
#           function and results for the function call within main.
#       -The text file with dog names as dogfile within adjust_results_isadog
#           function and in_arg.dogfile for the function call within main.
#   This function then uses extend to add items to the lists that are the
#   'value' of the results dictionary.

# Determine whether or not pet labels and classifier labels are dogs
def adjust_results_isadog(results_dic, dogfile):
    """
    Adjusts the results dictionary to determine whether classifier correctly
    classified images 'as a dog' or 'not a dog', especially when not a match.
    Demonstrates whether model architecture correctly classifies dog images
    even if it gets dog breeds wrong, i.e. they weren't initially a match.
    Parameters:
        results_dic - Dictionary with 'key' as image filename and 'value' as
            a List. Where the list will contain the following items:
                index 0 = pet image label (string)
                index 1 = classifier label (string)
                index 2 = 1/0 (int) where 1 = match between pet image
                    and classifer labels and 0 = no match between labels
            NEW index 3 = 1/0 (int) where pet image IS (1) or IS NOT (0) a dog
            NEW index 4 = 1/0 (int) where classifier IS (1) or IS NOT (0) a dog
        dogfile - A text file that contains names of all dogs from the classifier
            function and dog names from the pet image files. This file has
            one dog name per line; dog names are all in lowercase with
            spaces separating the distinct words of the dog name.
    Returns:
           None - results_dic is mutable data type so no return needed.
    """           
    
    # Create dictionary of dog breed names to compare results against
    dog_dic = {}

    # Read in dogfile line-by-line
    with open(dogfile, "r") as file:
        dog = file.readline()
        
        # Continue reading in lines until EOF
        while dog != "":

            # Remove newline characters
            dog = dog.rstrip()

            # Add to dictionary if not already present
            if dog not in dog_dic:
                dog_dic[dog] = 1
            else:
                print(dog + " already exists in dictionary")
            
            # Read in next line
            dog = file.readline()

    # Compare dictionaries and extend results dictionary with outcome
    for key in results_dic:

        # Determine pet IS a dog and classifier label IS a dog
        if results_dic[key][0] in dog_dic and results_dic[key][1] in dog_dic:
            results_dic[key].extend((1, 1))
        
        # Determine pet IS a dog and classifier label IS NOT a dog
        elif results_dic[key][0] in dog_dic and results_dic[key][1] not in dog_dic:
            results_dic[key].extend((1, 0))
        
        # Determine pet IS NOT a dog and classifier label IS a dog
        elif results_dic[key][0] not in dog_dic and results_dic[key][1] in dog_dic:
            results_dic[key].extend((0, 1))
        
        # Determine pet IS NOT a dog and classifier label IS NOT a dog
        if results_dic[key][0] not in dog_dic and results_dic[key][1] not in dog_dic:
            results_dic[key].extend((0, 0))
        
    # Dog dog dog this word has lost all meaning
