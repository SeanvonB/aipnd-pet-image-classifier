# !/usr/bin/env python3
# -*- coding: utf-8 -*-
#   
# PROGRAMMER: Sean von Bayern
# DATE CREATED: Sept. 19, 2019
# REVISED DATE: 
#
# PURPOSE:
#   Create a function print_results that prints the results statistics from
#   the results statistics dictionary (results_stats_dic). It also allows the
#   user to be able to print out cases of misclassified dogs and cases of
#   misclassified breeds of dog using the results dictionary (results_dic).
#   This function inputs:
#       -The results dictionary as results_dic within print_results
#           function and results for the function call within main.
#       -The results statistics dictionary as results_stats_dic within
#           print_results function and results_stats for the function call within main.
#       -The CNN model architecture as model wihtin print_results function
#           and in_arg.arch for the function call within main.
#       -Prints Incorrectly Classified Dogs as print_incorrect_dogs within
#           print_results function and set as either boolean value True or
#           False in the function call within main (defaults to False)
#       -Prints Incorrectly Classified Breeds as print_incorrect_breed within
#           print_results function and set as either boolean value True or
#           False in the function call within main (defaults to False)
#   This function does not output anything other than printing a summary
#   of the final results.

# Prints summary of results and calculated statistics to the terminal
def print_results(results_dic, results_stats_dic, model, 
                  print_incorrect_dogs = False, print_incorrect_breed = False):
    """
    Prints summary results on the classification, and then prints incorrectly
    classified dogs and incorrectly classified dog breeds if user indicates
    they want those printouts (use non-default values)
    Parameters:
        results_dic - Dictionary with key as image filename and value as a List
            index 0 = pet image label (string)
            index 1 = classifier label (string)
            index 2 = 1/0 (int)  where 1 = match between pet image and
                classifer labels and 0 = no match between labels
            index 3 = 1/0 (int) where pet image IS (1) or IS NOT (0) a dog
            index 4 = 1/0 (int) where classifier IS (1) or IS NOT (0) a dog
      results_stats_dic - Dictionary that contains the results statistics
            (either a  percentage or a count) where the key is the statistic's
            name (starting with 'pct' for percentage or 'n' for count) and
            the value is the statistic's actual value
      model - Indicates which CNN model architecture will be used by the
            classifier function to classify the pet images,
            values must be either: resnet alexnet vgg (string)
      print_incorrect_dogs - True prints incorrectly classified dog images and
            False doesn't print anything (default) (bool)
      print_incorrect_breed - True prints incorrectly classified dog breeds and
            False doesn't print anything (default) (bool)
    Returns:
        None - simply printing results.
    """

    # Setup variables from the results stats dictionary
    images = results_stats_dic["n_images"]
    dogs = results_stats_dic["n_dog_images"]
    notdogs = results_stats_dic["n_notdog_images"]
    cdogs = results_stats_dic["n_correct_dogs"]
    cnotdogs = results_stats_dic["n_correct_notdogs"]
    cbreeds = results_stats_dic["n_correct_breeds"]
    pct_matches = results_stats_dic["pct_matches"]
    pct_cdogs = results_stats_dic["pct_correct_dogs"]
    pct_cnotdogs = results_stats_dic["pct_correct_notdogs"]
    pct_cbreeds = results_stats_dic["pct_correct_breeds"]

    # Prints summary header
    print("\n*** Results Summary for CNN Model Architecture",
            model.upper(), "***")

    # Prints countable statistics
    print("{}: {}  {}: {}  {}: {}".format(
            "N Images", images, "N Dog Images", dogs,
            "N NotDog Images", notdogs))

    # Prints percentage statistics
    print("{}: {:.1f}%  {}: {:.1f}%\n{}: {:.1f}%  {}: {:.1f}%".format(
            "Correct Match", pct_matches, "Correct Dog", pct_cdogs,
            "Correct NotDog", pct_cnotdogs, "Correct Breed", pct_cbreeds))

    # Print dog/not-dog misclassifications if requested and present
    if print_incorrect_dogs and cdogs + cnotdogs != images:
        print("\nIncorrect Dog/Not-Dog Assignments:")
        for key in results_dic:
            if sum(results_dic[key][3:]) == 1:
                print("Image: {}    Classified: {}".format(
                    key, results_dic[key][1]))

    # Print dog/breed misclassifications if requested and present
    if print_incorrect_breed and cdogs != cbreeds:
        print("\nIncorrect Dog Breed Assignments:")
        for key in results_dic:
            if sum(results_dic[key][3:]) == 2 and results_dic[key][2] == 0:
                print("Image: {}    Classified: {}".format(
                    key, results_dic[key][1]))
