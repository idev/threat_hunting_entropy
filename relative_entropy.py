'''
This module is for calculating various entropy measurements on two pieces of data.
'''
from __future__ import division
from collections import Counter
import math
​
__version__ = '0.1'
​
class Entropy(object):
    '''
    This class contains all of the entropy functions.
    '''
    def __init__(self, data=None):
        self.data = data
        # The various algorithms are stored in a class dictionary so all
        # supported algorithms can be iterated through.
        # See the calculate function for an example.
        self.algorithms = {
            # 'Hartley': self.hartley_entropy,
            'Metric': self.metric_entropy,
            'Relative': self.relative_entropy,
            # 'Renyi': self.renyi_entropy,
            'Shannon': self.shannon_entropy,
            # 'Theil': self.theil_index,
        }
​
    def calculate(self, data):
        '''
        Calculate all supported entropy values
        '''
        results = {}
        for algo in self.algorithms:
            results[algo] = self.algorithms[algo](data)
        return results
​
    def metric_entropy(self, data, base=2):
        '''
        Calculate the metric entropy (aka normalized Shannon entropy) of data.
        '''
        entropy = 0.0

        if len(data) > 0:
            entropy = self.shannon_entropy(data, base) / len(data)

        return entropy
​
    def shannon_entropy(self, data, base=2):
        '''
        Calculate the Shannon entropy of data.
        '''
        entropy = 0.0
​
        if len(data) > 0:
            cnt = Counter(data)
            length = len(data)
            for count in cnt.values():
                entropy += (count / length) * math.log(count / length, base)
            entropy = entropy * -1.0

        return entropy
​
    def relative_entropy(self, data, base=2):
        '''
        Calculate the relative entropy (Kullback-Leibler divergence) between data and expected values.
        '''
        entropy = 0.0
        length = len(data) * 1.0
​
        if length > 0:
            cnt = Counter(data)

            # These probability numbers were calculated from the Alexa Top
            # 1 million domains as of September 15th, 2017. TLDs and instances
            # of 'www' were removed so 'www.google.com' would be treated as
            # 'google' and 'images.google.com' would be 'images.google'.
            probabilities = {
                '-': 0.013342298553905901,
                '_': 9.04562613824129e-06,
                '0': 0.0024875471880163543,
                '1': 0.004884638114650296,
                '2': 0.004373560237839663,
                '3': 0.0021136613076357144,
                '4': 0.001625197496170685,
                '5': 0.0013070929769758662,
                '6': 0.0014880054997406921,
                '7': 0.001471421851820583,
                '8': 0.0012663876593537805,
                '9': 0.0010327089841158806,
                'a': 0.07333590631143488,
                'b': 0.04293204925644953,
                'c': 0.027385633133525503,
                'd': 0.02769469202658208,
                'e': 0.07086192756262588,
                'f': 0.01249653250998034,
                'g': 0.038516276096631406,
                'h': 0.024017645001386995,
                'i': 0.060447396668797414,
                'j': 0.007082725266242929,
                'k': 0.01659570875496002,
                'l': 0.05815885325582237,
                'm': 0.033884915513851865,
                'n': 0.04753175014774523,
                'o': 0.09413783122067709,
                'p': 0.042555148167356144,
                'q': 0.0017231917793349655,
                'r': 0.06460084667060655,
                's': 0.07214640647425614,
                't': 0.06447722311338391,
                'u': 0.034792493336388744,
                'v': 0.011637198026847418,
                'w': 0.013318176884203925,
                'x': 0.003170491961453572,
                'y': 0.016381628936354975,
                'z': 0.004715786426736459
            }
​
            for char, count in cnt.items():
                observed = count / length
                expected = probabilities[char]
                entropy += observed * math.log((observed / expected), base)
        return entropy
