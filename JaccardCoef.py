import itertools
def JaccardCoff(ground_truth, predict):
    TP = 0
    FP = 0
    FN = 0
    for each_pair in itertools.combinations(range(len(ground_truth)),2):
        if (ground_truth[each_pair[0]] == ground_truth[each_pair[1]]) and (predict[each_pair[0]] == predict[each_pair[1]]):
            TP += 1
        elif (ground_truth[each_pair[0]] != ground_truth[each_pair[1]]) and (predict[each_pair[0]] == predict[each_pair[1]]):
            FP += 1
        elif (ground_truth[each_pair[0]] == ground_truth[each_pair[1]]) and (predict[each_pair[0]] != predict[each_pair[1]]):
            FN += 1
    return float(TP)/(TP+FP+FN)
