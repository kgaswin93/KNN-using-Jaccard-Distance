# KNN-using-Jaccard-Distance

Run Code :
----------

python tweets-k-means.py <numberOfClusters> <initialSeedsFile> <TweetsDataFile> <OutputFile>

for instance : python tweets-k-means.py 15 "C:/Users/kgasw/Grad/sem1/initial_seeds.txt" "C:/Users/kgasw/Grad/sem1/Tweets.json" "C:/Users/kgasw/Grad/sem1/output.txt"

<numberOfClusters> is the number of Clusters
<initialSeedsFile> is a text file containing value of the initial seed data
<TweetsDataFile> is the data file containing Tweets in JSON format
<outputFile> is the output file explained below

Please provide path without any spaces.

utilities.py has methods to calculate jaccard distance and compute sse etc.

Libraries Used : sys, pandas
