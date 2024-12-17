import urllib.request
import os.path

if __name__ == "__main__":

    # We always start with a dataset to train on. Let's download the tiny shakespeare dataset
    # !wget https://raw.githubusercontent.com/karpathy/char-rnn/master/data/tinyshakespeare/input.txt

    if not os.path.isfile('./input.txt'):
        print("Retrieving input.txt ...", end=" ")
        urllib.request.urlretrieve("https://raw.githubusercontent.com/karpathy/char-rnn/master/data/tinyshakespeare/input.txt", "input.txt")
        print("Done!")

    

