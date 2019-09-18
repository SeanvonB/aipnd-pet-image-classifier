# !/usr/bin/env python3
# -*- coding: utf-8 -*-
#                                                                             
# PROGRAMMER: Sean von Bayern
# DATE CREATED: Sept. 15, 2019
# REVISED DATE: 
#
# PURPOSE:
#   Create a function classify_images that uses the classifier function
#   to create the classifier labels and then compares the classifier
#   labels to the pet image labels. This function inputs:
#       -The Image Folder as image_dir within classify_images and function
#           and as in_arg.dir for function call within main.
#       -The results dictionary as results_dic within classify_images
#           function and results for the functin call within main.
#       -The CNN model architecture as model wihtin classify_images function
#           and in_arg.arch for the function call within main.
#   This function uses the extend function to add items to the list
#   that's the 'value' of the results dictionary.

# Import classifier function for using CNN to classify images
from classifier import classifier

# Extend results dictionary to include classifier labels and match results
def classify_images(images_dir, results_dic, model):
    """
    Creates classifier labels with classifier function, compares pet labels to 
    the classifier labels, and adds the classifier label and the comparison of 
    the labels to the results dictionary using the extend function. 
    Parameters: 
        images_dir  - The (full) path to the folder of images that are to be
            classified by the classifier function (string)
        results_dic - Results Dictionary with 'key' as image filename and 'value'
            as a List. Where the list will contain the following items: 
                index 0 = pet image label (string)
            NEW index 1 = classifier label (string)
            NEW index 2 = 1/0 (int) where 1 = match; 0 = no match
        model - Indicates which CNN model architecture will be used by the 
            classifier function to classify the pet images,
            values must be either: resnet alexnet vgg (string)
    Returns:
        None - results_dic is mutable data type so no return needed.         
    """

    # For each image in images_dir stored as key:
    for key in results_dic:

        # Create path to image, e.g. "./pet_images/" + "beagle"
        image = images_dir + key

        # Run classifier on image using given CCN model architecture
        model_label = classifier(image, model)

        # Format label to match those generated in get_pet_labels.py
        model_label = model_label.lower().strip()

        # Set truth to pet label value
        truth = results_dic[key][0]

        # Check if labels match and add results to list:
        # 1 = match, 0 = no match
        if truth in model_label:
            results_dic[key].extend([model_label, 1])
        else:
            results_dic[key].extend([model_label, 0])
