def getCenters(path):
    with open(path, 'r') as myfile:
        data = myfile.read().replace('\n', '')
    return data.split(",")
def getKeyWords(sentence):
    wordList = sentence.split(" ")
    return list(set(wordList))

def getWordDict(text):
    text_words = getKeyWords(text)
    word_dict = dict()
    for word in text_words :
        word_dict[word] = True
    return word_dict

def jaccardDistance(text1,text2):
    text_dict1 = getWordDict(text1)
    text_dict2 = getWordDict(text2)
    union_dict = text_dict1.copy()
    union_dict.update(text_dict2)
    union = len(union_dict)
    keys_a = set(text_dict1.keys())
    keys_b = set(text_dict2.keys())
    intersection = len(keys_a & keys_b)
    return (1-(intersection/union))

def updateCenters(cluster,tweet_data):
    updated_cluster = dict()
    for center in cluster.keys():
        min_distance = 999
        min_center = center
        for temp_center in cluster[center]:
            total_distance = 0
            for id in cluster[center]:
                if temp_center != id:
                    total_distance += jaccardDistance(tweet_data[temp_center],tweet_data[id])
            if min_distance > total_distance:
                min_distance = total_distance
                min_center = temp_center
        updated_cluster[min_center] = cluster[center]
    return updated_cluster

def sum_squared_error(cluster,tweet_data):
    sum = 0
    for center in cluster.keys():
        for id in cluster[center]:
            if center != id:
                sum += jaccardDistance(tweet_data[center], tweet_data[id])
    return sum