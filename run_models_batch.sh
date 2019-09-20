# !/bin/sh
# */AIPND-revision/intropyproject-classify-pet-images/run_models_batch.sh
#                                                                             
# PROGRAMMER: Jennifer S.
# DATE CREATED: 02/08/2018                                  
# REVISED DATE: Sept. 20, 2019
# PURPOSE: Runs all three models to test which provides 'best' solution.
#          Please note output from each run has been piped into a text file.
#
# USAGE: sh run_models_batch.sh -- will run program from commandline within Project Workspace
#  
python check_images.py --dir pet_images/ --arch resnet  --dogfile dognames.txt > result_logs/pet_images_resnet.txt
python check_images.py --dir pet_images/ --arch alexnet --dogfile dognames.txt > result_logs/pet_images_alexnet.txt
python check_images.py --dir pet_images/ --arch vgg  --dogfile dognames.txt > result_logs/pet_images_vgg.txt
