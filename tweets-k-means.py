import pandas as pd
import utilities
import sys
print('Running')
numberOfClusters = sys.argv[1]
initial_seeds = sys.argv[2]
tweets_json_path = sys.argv[3]
output_path = sys.argv[4]
df = pd.read_json(tweets_json_path)
center_ids = utilities.getCenters(initial_seeds)
id_list = df['id']
tweet_list = df['text']
tweet_data = dict()
for id,tweet in zip(id_list,tweet_list):
    tweet_data[str(id)] = tweet
flag = True
while(flag):
    cluster = dict()
    for id in tweet_data.keys():
        if id not in center_ids:
            min = 999
            min_id = ""
            for center_id in center_ids:
                dist = utilities.jaccardDistance(tweet_data[id],tweet_data[center_id])
                if min > dist:
                    min = dist
                    min_id = center_id
            if not cluster.get(min_id):
                cluster[min_id] = []
                cluster[min_id].append(min_id)
            cluster[min_id].append(id)
    updated_cluster = utilities.updateCenters(cluster,tweet_data)
    keys_old_cluster = set(cluster.keys())
    keys_new_cluster = set(updated_cluster.keys())
    intersection = len(keys_old_cluster & keys_new_cluster)
    if intersection == len(cluster.keys()):
        flag = False
    else:
        center_ids = updated_cluster.keys()
iteration = 1
for key in cluster.keys():
    with open(output_path, 'a') as f1:
        f1.write(str(iteration)+' '+",".join(cluster[key])+"\n")
    iteration+=1
with open(output_path, 'a') as f1:
    f1.write('SSE '+str(utilities.sum_squared_error(cluster,tweet_data)))
print('Executed')