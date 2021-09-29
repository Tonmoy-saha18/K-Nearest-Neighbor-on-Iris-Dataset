import random

#In this part we are reading the iris.csv file and making the dataset
with open('iris.csv', 'r') as iris:
    file = iris.readlines()
    dataset = []
    for a in file:
        dataset.append(a.split(','))
    random.shuffle(dataset)

    #In this part we are spliting train,validation and test set
    train_set = []
    val_set = []
    test_set = []

    for a in dataset:
        num = random.random()
        if 0 <= num <= 0.7:
            train_set.append(a)
        elif 0.7 < num <= 0.85:
            val_set.append(a)
        else:
            test_set.append(a)

    #In this part we are doing the knn classification for val_set
    k = 5
    correct = 0
    for v in val_set:

        #here we are calculating eucliadean distance and from that distance we have taken k number of values
        L = []
        for t in train_set:
            distance = ((float(t[0]) - float(v[0]))**2 + (float(t[1]) - float(v[1]))**2 + (float(t[2]) - float(v[2]))**2 + (float(t[3]) - float(v[3]))**2)**0.5
            copy_t = []
            for a in t:
                copy_t.append(a)
            copy_t.append(distance)
            L.append(copy_t)
        L = sorted(L, key=lambda l: l[5])
        L = L[0:k]

        #here we are taking majority class from K samples
        c0 = 0
        c1 = 0
        c2 = 0
        for l in L:
            # print(type(l[4]))
            if l[4] == '0\n':
                c0 += 1
            elif l[4] == '1\n':
                c1 += 1
            else:
                c2 += 1
        # print(c0, c1, c2)
        if c0 >= c2 and c0 >= c1:
            class_ = '0\n'
        elif c1 >= c0 and c1 >= c2:
            class_ = '1\n'
        else:
            class_ = '2\n'

        #here we will check the result is correct or not
        if v[4] == class_:
            correct += 1

    #here we wil print validation accuracy
    accuracy = (correct / len(val_set))*100
    print("Validation set")
    print("------------------")
    print("For K = {} The accuracy is {} %\n\n".format(k, accuracy))

    # In this part we are doing the knn classification for test_set
    correct = 0
    for v in test_set:

        # here we are calculating eucliadean distance and from that distance we have taken k number of values
        L = []
        for t in train_set:
            distance = ((float(t[0]) - float(v[0])) ** 2 + (float(t[1]) - float(v[1])) ** 2 + (
                        float(t[2]) - float(v[2])) ** 2 + (float(t[3]) - float(v[3])) ** 2) ** 0.5
            copy_t = []
            for a in t:
                copy_t.append(a)
            copy_t.append(distance)
            L.append(copy_t)
        L = sorted(L, key=lambda l: l[5])
        L = L[0:5]

        # here we are taking majority class from K samples
        c0 = 0
        c1 = 0
        c2 = 0
        for l in L:
            # print(type(l[4]))
            if l[4] == '0\n':
                c0 += 1
            elif l[4] == '1\n':
                c1 += 1
            else:
                c2 += 1
        # print(c0, c1, c2)
        if c0 >= c2 and c0 >= c1:
            class_ = '0\n'
        elif c1 >= c0 and c1 >= c2:
            class_ = '1\n'
        else:
            class_ = '2\n'

        # here we will check the result is correct or not
        if v[4] == class_:
            correct += 1

    # here we wil print validation accuracy
    accuracy = (correct / len(test_set)) * 100
    print("Test set")
    print("------------")
    print("For K = 5 The accuracy is {} %\n".format(accuracy))
