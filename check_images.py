# !/usr/bin/env python
# -*- coding: utf-8 -*-
# 
# PROGRAMMER: Sean von Bayern
# DATE CREATED: Sept. 10, 2019
# REVISED DATE: 
#
# PURPOSE:
#   Classifies pet images using a pretrained CNN model, compares these
#   classifications to the true identity of the pets in the images, and
#   summarizes how well the CNN performed on the image classification task.
#   Note that the true identity of the pet (or object) in the image is
#   indicated by the filename of the image. Therefore, our program must
#   first extract the pet image label from the filename before
#   classifying the images using the pretrained CNN model. With this
#   program we will be comparing the performance of 3 different CNN model
#   architectures to determine which provides the 'best' classification.
#
# NOTES:
#   Use argparse Expected Call with <> indicating expected user input:
#       python check_images.py --dir <directory with images> --arch <model>
#           --dogfile <file that contains dognames>
#
#   Example call:
#       python check_images.py --dir pet_images/ --arch vgg --dogfile dognames.txt

# Import python modules
from time import time, sleep

# Import print functions that check the lab
from print_functions_for_lab_checks import *

# Import functions created for this program
from get_input_args import get_input_args
from get_pet_labels import get_pet_labels
from classify_images import classify_images
from adjust_results_isadog import adjust_results_isadog
from calculate_results_stats import calculate_results_stats
from print_results import print_results

# Main program function defined below
def main():
    # Collect start time
    start_time = time()
    
    # Collect user input arguments from command line
    input_args = get_input_args()

    # Check command line arguments
    check_command_line_arguments(input_args)
    
    # Create results dictionary of file_name:label pairs
    results = get_pet_labels(input_args.dir)

    # Check pet images in the results dictionary using results
    check_creating_pet_image_labels(results)

    # Create labels for classifier results, compare to true labels,
    # and extend results dictionary to include results of comparison 
    classify_images(input_args.dir, results, input_args.arch)

    # Check results dictionary using results
    check_classifying_images(results)    

    # Determine if classifier correctly identified dogs as dogs,
    # and extend results dictionary with results of that determination
    adjust_results_isadog(results, input_args.dogfile)

    # Function that checks Results Dictionary for is-a-dog adjustment using results
    check_classifying_labels_as_dogs(results)


    # Use results dictionary to calculate and return a dictionary of results stats
    results_stats = calculate_results_stats(results)

    # Function that checks Results Statistics Dictionary using results_stats
    check_calculating_results(results, results_stats)


    # TODO 6: Define print_results function within the file print_results.py
    # Once the print_results function has been defined replace 'None'
    # in the function call with in_arg.arch  Once you have done the
    # replacements your function call should look like this:
    #      print_results(results, results_stats, in_arg.arch, True, True)
    # Prints summary results, incorrect classifications of dogs (if requested)
    # and incorrectly classified breeds (if requested)
    print_results(results, results_stats, None, True, True)
    
    # Collect end time
    end_time = time()
    
    # Compute overall runtime in seconds and print in hh:mm:ss format
    total_time = end_time - start_time
    print("\n** Total Elapsed Runtime:",
          str(int((total_time/3600)))+":"+str(int((total_time%3600)/60))+":"
          +str(int((total_time%3600)%60)))
    

# Call to main function to run the program
if __name__ == "__main__":
    main()
