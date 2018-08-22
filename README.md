# SRClassifier
Naive Bayes classification of service requests types at National Instruments. 

# Problem Statement
Early on in the Applications Engineering department at National Instruments, I identified that there was frequent misclassification and misdirection of service requests that came over the phone and email. Phone misclassification was caused by a misinterpretation from the initial customer support rep. Over email, this was caused by a poor classifier that would assume every request that had "can" in the description was an issue related to the CAN protocol. Because of the poor accuracy of the email classifier, the department requires manual assignment of service requests, wasting time of NI employees and customers. The project was initially sparked by wanting to develop a way to get customers in touch with the correct person first and as fast as possible, removing all middlemen and improving their experience. 

# Solution
I developed a machine learning classifier using Multinomial Naive Bayes. In Python, I wrote a script to perform web scraping for 10 years of service request data and incorporated the NB model which predicts the correct service request type from ~75 possible categories with roughly 82% accuracy. 

# Process
After web scraping for the raw data, I realized that the model itself only achieved around 25% accuracy. There was extreme bias towards high frequency types, so I wrote a script to balance the training set. I created a dictionary of keywords for most of the types (Keywords.csv), which included associated hardware, software, and commonly used phrases. Some of the SR Types are brand new, so I parsed their associated manuals and trainings to gather the most commonly used phrases. The balancing script set a threshold on the max number of training datapoints for each high frequency type, and then created artificial data from the keywords for low frequency types. This increased the accuracy to a sufficient percentage. From there, I developed a UI in LabVIEW NXG (UIClassifier.gvi) that simulates a user input and classifies their description. This is ultimately designed as a proof-of-concept for implementing this with the current system in place.

# Shortfalls
Reviewing the training data (TrainingDataFINAL.csv) shows that there are many occassions where the employee in charge of the request didn't label the issue correctly. There is little accountability for doing that, so this significantly dropped the accuracy. I didn't fully have the time capacity to manually check thousands of datapoints for accuracy. This shortfall is especially relevant with the SRType "LV", or LabVIEW. By far the most all-encompassing type, it is mislabeled an overwhelming majority of the time. For that reason, I left LabVIEW datapoints out of the training and test set. 

# Company Impact // Future Development
Working towards getting the Tech Lead in the department to further train the model on the newer products as well as add more correctly labeled data to fully integrate this project into our phone and email system. 

New proposed system:
All requests are made online and filtered through my classifier.
The current system in place to assign the issue to an engineer happens without the need for manual assignment.
The correct individual reaches out to them.

# Project Dependencies
python // numpy // scipy // sklearn // beautifulsoup // LabVIEW NXG 
