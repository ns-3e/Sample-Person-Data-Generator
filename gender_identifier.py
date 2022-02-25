import random
from nltk.corpus import names
import nltk

def gender_features(word):
    middle = len(word)-6
    if len(word) < 3:
        return{"last_letter":word[-1], "first_letter":word[0]}
    else:
        return{"last_letter":word[-1], "first_letter":word[0], "first_three": word[:3], "last_three": word[-3:]}

labeled_names = ([(name, "male") for name in names.words('male.txt')]+
                [(name, "female") for name in names.words('female.txt')])

random.shuffle(labeled_names)

featuresets = [(gender_features(n), gender) for (n, gender) in labeled_names]

train_set = featuresets

classifier = nltk.NaiveBayesClassifier.train(train_set)

print(nltk.classify.accuracy(classifier, train_set))

def name_gender(name):
    return classifier.classify(gender_features(name))

