# !/usr/bin/env python3
# -*- coding: utf-8 -*-
#                                                                             
# PROGRAMMER: Sean von Bayern
# DATE CREATED: Sept. 17, 2019
# REVISED DATE: 
#
# PURPOSE:
#   Create a function calculate_results_stats that calculates the
#   statistics of the results of the program using the classifier's model
#   architecture to classify the images. This function will use the
#   results in the results dictionary to calculate these statistics.
#   This function will then put the results statistics in a dictionary
#   (results_stats_dic) that's created and returned by this function.
#   This function returns:
#       Results Statistics Dictionary (results_stats_dic)
#           This dictionary contains the results statistics (either a
#           percentage or a count) where the key is the statistic's name
#           (starting with 'pct' for percentage or 'n' for count) and value
#           is the statistic's value.
#           This dictionary should contain the following keys:
#               n_images: number of images
#               n_dog_images: number of dog images
#               n_notdog_imgages: number of NON-dog images
#               n_matches: number of matches between pet & classifier labels
#               n_correct_dogs: number of correct dog images
#               n_correct_notdogs: number of correct NON-dog images
#               n_correct_breed: number of correct dog breeds
#               pct_matches: percentage of correct matches
#               pct_correct_dogs: percentage of correct dogs
#               pct_correct_breed: percentage of correct dog breeds
#               pct_correct_notdogs: percentage of correct NON-dogs

# Create and return results stats dictionary
def calculate_results_stats(results_dic):
    """
    Calculates statistics of the results of the program run using classifier's model
    architecture to classifying pet images. Then puts the results statistics in a
    dictionary (results_stats_dic) so that it's returned for printing to help
    the user to determine the 'best' model for classifying images.
    Parameters:
        results_dic - Dictionary with keys as image filenames and values as a List
            index 0 = pet image label (string)
            index 1 = classifier label (string)
            index 2 = 1/0 (int)  where 1 = match between pet image and
                classifer labels and 0 = no match between labels
            index 3 = 1/0 (int) where pet image IS (1) or IS NOT (0) a dog
            index 4 = 1/0 (int) where classifier IS (1) or IS NOT (0) a dog
    Returns:
        results_stats_dic - Dictionary that contains the results statistics (either
            a percentage or a count) where the key is the statistic's name
            (starting with 'pct' for percentage or 'n' for count) and the value is
            the statistic's actual value.
    """

    # Create new stats results dictionary with zeroed values
    results_stats_dic = {
        "n_images": 0,
        "n_dog_images": 0,
        "n_notdog_images": 0,
        "n_matches": 0,
        "n_correct_dogs": 0,
        "n_correct_notdogs": 0,
        "n_correct_breeds": 0,
        "pct_matches": 0.0,
        "pct_correct_dogs": 0.0,
        "pct_correct_notdogs": 0.0,
        "pct_correct_breeds": 0.0,
    }

    # Collect countable (n_) stats from results_dic
    results_stats_dic["n_images"] = len(results_dic)
    for key in results_dic:
        if results_dic[key][3] == 1:
            results_stats_dic["n_dog_images"] += 1
        if results_dic[key][3] == 0:
            results_stats_dic["n_notdog_images"] += 1
        if results_dic[key][2] == 1:
            results_stats_dic["n_matches"] += 1
        if results_dic[key][3] == 1 and results_dic[key][4] == 1:
            results_stats_dic["n_correct_dogs"] += 1
        if results_dic[key][3] == 0 and results_dic[key][4] == 0:
            results_stats_dic["n_correct_notdogs"] += 1
        if results_dic[key][2] == 1 and results_dic[key][3] == 1:
            results_stats_dic["n_correct_breeds"] += 1

    # Setup variables from countable stats
    images = results_stats_dic["n_images"]
    dogs = results_stats_dic["n_dog_images"]
    notdogs = results_stats_dic["n_notdog_images"]
    matches = results_stats_dic["n_matches"]
    cdogs = results_stats_dic["n_correct_dogs"]
    cnotdogs = results_stats_dic["n_correct_notdogs"]
    cbreeds = results_stats_dic["n_correct_breeds"]

    # Calculate percantage (pct_) stats
    if images > 0:
        results_stats_dic["pct_matches"] = (matches / images) * 100.0
    if dogs > 0:
        results_stats_dic["pct_correct_dogs"] = (cdogs / dogs) * 100.0
        results_stats_dic["pct_correct_breeds"] = (cbreeds / dogs) * 100.0
    if notdogs > 0:
        results_stats_dic["pct_correct_notdogs"] = (cnotdogs / notdogs) * 100.0

    # Return completed results stats dictionary
    return results_stats_dic
