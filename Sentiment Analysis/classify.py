import json

train_data = None
vocab = None


def prob_prior(cases):
    genre = train_data.values()
    return {
        cases[0]: float(genre.count(cases[0])) / len(train_data),
        cases[1]: float(genre.count(cases[1])) / len(train_data)
    }


def prob_likelihood(word, genre):
    count_word = 0
    for key, value in train_data.items():
        if word in key and value == genre:
            count_word += 1
    count_all = 0
    for key, value in train_data.items():
        if value == genre:
            count_all += 1
    return (count_word + 1.0) / (count_all + len(vocab))


def prod_prob_likelihood(text, genre):
    prod = 1.0
    for word in text.split():
        prod *= prob_likelihood(word, genre)
    return prod


def calculate(text, cases):
    ''' Returns the probabilities corresponding to all the cases.
        text should be a string. cases should be a list containing all the genres.'''
    start()
    text = text.lower()
    prob1, prob2 = prob_prior(cases).values()
    return {
        cases[0]: prob1 * prod_prob_likelihood(text, cases[0]),
        cases[1]: prob2 * prod_prob_likelihood(text, cases[1])
    }


def start():
    global train_data
    global vocab
    with open('data.json') as data_file:
        train_data = json.load(data_file)
    vocab = set([word.lower() for word_set in train_data.keys()
                 for word in word_set.split()])


def improve(text, genres):
    global train_data
    further = raw_input("Offer Correction? ").lower()
    if further in ['yes', 'y']:
        answer = raw_input(
            "Actual Answer [" + genres[0] + "/" + genres[1] + "]: ")
        if answer in genres:
            train_data[text] = answer
            with open("data.json", "w") as myfile:
                json.dump(train_data, myfile)


if __name__ == '__main__':
    calculate("happy", ["happy", "sad"])
