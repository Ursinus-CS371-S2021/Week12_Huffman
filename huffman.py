import numpy as np
import matplotlib.pyplot as plt
from collections import deque
from heapq import heappush, heappop

class TreeNode(object):
    def __init__(self, key = None):
        self.key = key
        self.left = None
        self.right = None
    
    def __str__(self):
        ret = ""
        if self.key:
            ret = "{}".format(self.key)
        return ret

    def compute_coords(self, x = [0], y = 0):
        if self.left:
            self.left.compute_coords(x, y-6)
        self.x = x[0]
        self.y = y
        x[0] += 1
        if self.right:
            self.right.compute_coords(x, y-6)

    def draw(self):
        # Draw a dot
        plt.scatter(self.x, self.y, 50, 'k')
        # Draw some text indicating what the key is
        plt.text(self.x-0.2, self.y-1.5, "{}".format(self))
        # Offset in x
        x1, y1 = self.x, self.y
        if self.left:
            # Draw a line segment from my node to this left child
            x2, y2 = self.left.x, self.left.y
            plt.plot([x1, x2], [y1, y2])
            plt.text(0.5*(x1+x2), 0.5*(y1+y2), "0")
            self.left.draw()
        if self.right:
            # Draw a line segment from my node to this right child
            x2, y2 = self.right.x, self.right.y
            plt.plot([x1, x2], [y1, y2])
            plt.text(0.5*(x1+x2), 0.5*(y1+y2), "1")
            self.right.draw()
    
    def make_codebook(self, codebook, bstr):
        """
        Recursively create a codebook while traversing the tree
        
        Parameters
        ----------
        codebook: dictionary
            Key is a key in the tree, value is the binary string
        bstr: list of string
            A binary string that's been constructed incrementally
        """
        # TODO: Fill this in
        pass


class HuffmanTree(object):
    def __init__(self):
        self.root = None

    def draw(self):
        if self.root:
            self.root.compute_coords()
            self.root.draw()
        plt.axis("off")
        plt.axis("equal")
    
    def get_codebook(self):
        codebook = {}
        if self.root:
            self.root.make_codebook(codebook, [])
        return codebook
    
    def encode(self, s):
        codebook = self.get_codebook()
        res = ""
        for c in s:
            res += codebook[c]
        return res
    
    def decode(self, bstr):
        ## TODO: Fill this in
        pass


def get_chars(seed = None):
    """
    Return a list of the 26 lowercase characters, as well as the space,
    in a random order.

    Parameters
    ----------
    seed: int
        A seed for the random permutation
    """
    chars = ["{}".format(chr(ord('a') + i)) for i in range(26)]
    chars += [" ", "."]
    if seed:
        np.random.seed(seed)
        chars = [chars[i] for i in np.random.permutation(len(chars))]
    return chars

def get_char_counts(do_plot = False):
    """
    Return a dictionary whose key is a character and whose
    value is teh number of times that character shows up in a word
    """
    fin = open("words.txt")
    words = [l.strip() for l in fin.readlines()]
    counts = {}
    for w in words:
        for c in w:
            if not c in counts:
                counts[c] = 0
            counts[c] += 1
    counts[" "] = len(words)
    counts["."] = int(len(words)/5)
    if do_plot:
        keys = sorted(counts.keys())
        values = [counts[k] for k in keys]
        plt.bar(keys, values)
        plt.xticks(np.arange(len(keys)), keys)
        plt.show()
    return counts

def make_tree_naive(seed):
    chars = get_chars(seed)
    nodes = deque()
    ## TODO: Fill this in

def make_huffman_tree():
    counts = get_char_counts()
    nodes = []
    ## TODO: Fill this in

