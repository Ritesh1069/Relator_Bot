
# Relator-Bot

### General Description:

__Relator Bot__ is a research based project under __TeksMobile__.

The objective of the project is to create a web-application through which people with similar interests can connect with each other.

The user, once logged in, will be shown other people with highest compatibility so that he can make connections, or what we like to call it, __relations__.

### Github Folder Description:

This repository has total 4 folders:

__Documentations__
__Main__
__Trials__
__test datasets__

##### 1. Documentations:

This folder contains a short report about the project __Relator Bot__ and an image which represents the flow of the system.

##### 2. Main:

This folder contains the the main model (__GCN_model.ipynb__) of the project and other important codes like __datacsvgenerator.ipynb__ which generates a dummy dataset and __filter_dataset.py__ which filters the dataset based on certain criteria.

The file __graphapi.py__ can be run by enter the access token of the user's __Facebook account__ ; to access his Facebook data.

The subfolder UserData contains users html files which can be used to visualize the output of the model in an interactable graph.

##### 3. Trials:

This folder contains the models that were created in the past while on the way of achieving the most efficient one.

##### 4. test datasets:

This folder contains 5 files, out of which are 4 generated from the __datacsvgenerator.ipynb__ code .

Each of the 4 files are dummy datasets of n number of users' Facebook account details.

The amount of user differs in each file from 100, 500 and 100,000. 

However, the file __profile_dataNewest.csv__ contains real data of some Facebook users (The Team Members' accounts); this is obtained through the file __graphapi.py__ in the __Main__ folder.

### Workflow:

##### Data Collection:

For the purpose of implementing the model, dataset of dummy users is created.

For real-time implementation, User data is collected through his/her Facebook account using Graph API access token.

##### Filtering:

The choice of filtering criteria is given to the user.
The filtering of users is done on the basis of number of common interest,their location and/or their gender.

##### Model:

We are using a modified GCN model for calculating the compatibility scores between users.

### Steps to Run the Code:

##### Step 1:

Update the variable __num_entries__ (at the end of the code) according to required number of users and generate a dataset by running the code __datacsvgenerator.ipynb__ from the __Main__ folder.

##### Step 2:

Open the code __GCN_model.ipynb__ from the __Main__ folder.

Edit the the path in the variable __df1__ according to the path of your dataset which was generated in __Step 1__.

Run the code and enter the name of the user and gender preference of the matches.

##### Finish:

The generated output will show the top 100 users who have the best compatibility score with you and also the common interests between you and them.


Go ahead and make your __"relations"__!

### About TeksMobile:

__TeksMobile__ is an end-to-end cross-platform mobile app and game development company. 
It specializes in the creation of custom software for the iOS, watchOS, tvOS, macOS and Android platforms. 
More than 900 apps currently feature in the company portfolio.