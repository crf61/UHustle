# UHustle
This is Christy Felix's 2020 python project.

# Why is this important?
This program is a search engine for students looking to purchase items and services from other students on college campuses.
It makes it easier for students to purchase from other students and for customers to easier find what they are looking for.
This is an extension of UHustle's website, theuhustle.com. UHustle is an online marketplace for students who provide goods and services.

# Program Description
This program is meant for students looking for an item or service at their school or at nearby schools.
In order for the program to tell you what items are available. The user (you) needs to tell the program your name, your school, and then choose the items you want to purchase according to the available items at that school.

# How does it work?
    # Set Up a Virtual Environment 
    
    Use the code below to set up a virtual environment

    conda create -n marketplace-env python=3.7

    #There will be a prompt asking if you want to proceed. Type Y.

    Then after entering the above code the first time, activate the virtual environment using the code below

    conda activate shopping-env

    #Inputs

    You will first be asked to enter Your Name 

    Then you will be asked what school you go to. There are only 3 schools available which are: Georgetown University, George Washington University, and American University.

    Make sure you type in the complete name.

    Then program will then output names of products and services available at that school. Choose the items and services that you would like to purchase but writing on the full name of that item or service.

    When you are doing choosing, type DONE and the system will check you out.

# Testing the Script
    
    #Install pytest so the script is be automatically tested
    
    pip install pytest

    #Run pytest

    Type "pytest" to run the test.
    
    #Run the python script, use the code below

    python marketplace.py

# Why are there only three school available?
Georgetown University, George Washington University, and American University are the starter schools for UHustle's soft launch.

# What listings are available?
There are four categories available which are: Food and Drink, Entertainment, Media, and Beauty.
Users can choose from the listings available depeding on what school they choose.

# Notes
Please note not all schools have the same listings. Sometimes you won't be able to find what you want at Georgetown but may find what you're looking for at George Washington.

# IMPORTANT
In order to see the prices of the items you want, you have to write the name of items (without quotation marks)