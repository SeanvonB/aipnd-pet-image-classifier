# !/bin/sh
# */AIPND-revision/intropyproject-classify-pet-images/run_models_batch_uploaded.sh
#                                                                             
# PROGRAMMER: Jennifer S.
# DATE CREATED: 02/08/2018                                  
# REVISED DATE: Sept. 20, 2019
# PURPOSE: Runs all three models to test which provides 'best' solution on the Uploaded Images.
#          Please note output from each run has been piped into a text file.
#
# USAGE: sh run_models_batch_uploaded.sh -- will run program from commandline within Project Workspace
#  
python check_images.py --dir uploaded_images/ --arch resnet  --dogfile dognames.txt > result_logs/uploaded_images_resnet.txt
python check_images.py --dir uploaded_images/ --arch alexnet --dogfile dognames.txt > result_logs/uploaded_images_alexnet.txt
python check_images.py --dir uploaded_images/ --arch vgg  --dogfile dognames.txt > result_logs/uploaded_images_vgg.txt
