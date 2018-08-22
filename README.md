# SRClassifier
Naive Bayes classification of service requests types at National Instruments. 

# Problem Statement
Early on in the Applications Engineering department at National Instruments, I identified that there was frequent misclassification and misdirection of service requests that came over the phone and email. Phone misclassification was caused by a misinterpretation from the initial customer support rep. Over email, this was caused by a poor classifier that would assume every request that had "can" in the description was an issue related to the CAN protocol. Because of the poor accuracy of the email classifier, the department requires manual assignment of service requests, wasting time of NI employees and customers. In response, I developed a machine learning classifier using Multinomial Naive Bayes. In Python, I wrote a script to perform web scraping for 10 years of service request data and developed a model that predicts the correct service request type from ~75 possible categories with roughly 82% accuracy. Project still in development.

# Project Dependencies
-python
-numpy
-scipy
-sklearn
-beautifulsoup
