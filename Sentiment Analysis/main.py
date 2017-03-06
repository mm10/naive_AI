''' Just the input & output part.
All processing is done in the functions of the bayes module'''

import bayes

if __name__ == '__main__':
    TEXT_TO_CHECK = raw_input("Input: ").lower()
    TYPES = ["happy", "sad"]
    RESULT = bayes.calculate(TEXT_TO_CHECK, TYPES)
    print "Judgement:",
    RESULT_VALUE = RESULT[TYPES[0]] - RESULT[TYPES[1]]
    if RESULT_VALUE:
        print RESULT_VALUE > 0 and TYPES[0] or TYPES[1]
    else:
        print "neutral"
    # to improve the database incase of wrong prediction
    bayes.improve(TEXT_TO_CHECK, TYPES)
