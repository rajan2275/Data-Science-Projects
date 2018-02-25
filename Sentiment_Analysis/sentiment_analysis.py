import nltk
import nltk.classify.util
from nltk.classify import NaiveBayesClassifier
from nltk.corpus import movie_reviews

def extract_features(word_list):
    return dict([(word, True) for word in word_list])

if __name__=='__main__':
    # Load positive and negative reviews
    nltk.download('movie_reviews')
    positive = movie_reviews.fileids('pos')
    negative = movie_reviews.fileids('neg')

    features_positive = [(extract_features(movie_reviews.words(fileids=[f])), 'Positive') for f in positive]
    features_negative = [(extract_features(movie_reviews.words(fileids=[f])), 'Negative') for f in negative]

    # Split the data into train and test (80/20)
    threshold_factor = 0.8
    threshold_positive = int(threshold_factor * len(features_positive))
    threshold_negative = int(threshold_factor * len(features_negative))

    features_train = features_positive[:threshold_positive] + features_negative[:threshold_negative]
    features_test = features_positive[threshold_positive:] + features_negative[threshold_negative:]

    print('-------------------------------------')
    print('Training and test Data Points.')
    print('-------------------------------------')
    print('\n Training datapoints:', len(features_train))
    print('Test datapoints:', len(features_test))
    print('-------------------------------------')

    # Train a Naive Bayes classifier
    classifier = NaiveBayesClassifier.train(features_train)

    print('-------------------------------------')
    print('Accuracy of the classifier:')
    print('-------------------------------------')

    print(nltk.classify.util.accuracy(classifier, features_test))
    print('-------------------------------------')

    # Input reviews
    input_reviews = [ "Pathetic movie",
                      "It is an amazing movie",
                      "I will never recommend it to anyone.",
                      "The direction was challenging and the story was ok"
    ]


    print('-------------------------------------')
    print('\nPredictions:')
    print('-------------------------------------')
    for review in input_reviews:
        print('\nReview:', review)
        probdist = classifier.prob_classify(extract_features(review.split()))
        pred_sentiment = probdist.max()
        print('Predicted sentiment:', pred_sentiment)
        print('Probability:', round(probdist.prob(pred_sentiment), 2))
