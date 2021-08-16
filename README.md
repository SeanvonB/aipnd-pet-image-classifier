# Dog Breed Classifier

This was my submission for a project that was part of Udacity's Computer Vision Nanodegree. The purpose of this project was to test different Convolutional Neural Network architectures against each other by creating a relatively simple package that features the ability to easily switch between architectures and compare results.

Initially, I've tested three popular CNN architectures: AlexNet, ResNet, and VGG. The classifier then proceeds to test these architectures by running them through two connected classification exercises. First, it splits the image dataset into *dog* and *not-dog* groups; then, it determines which breeds are the highest probable match for each *dog* image. Of the three, VGG appears to be the best choice for this application with 100% accuracy on *dog* and *not-dog* classifications, the highest accuracy on breed matching, and – surprisingly – the niche ability to classify breeds correctly from inverted images.

This program was built on a foundation provided by Udacity [here](https://github.com/udacity/AIPND-revision).
