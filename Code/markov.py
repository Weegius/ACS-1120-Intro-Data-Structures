from os import wait
from random import choice, random
from dictogram import Dictogram
from tokens import tokenize
import sys


class MarkovbutBetter():
  def __init__(self, tokens):
    self.mchain = {}
    self.hist = Dictogram()

    for i in range(len(tokens)-2):
      pair = (tokens[i], tokens[i+1] )
      self.hist.add_count(pair)

      if pair not in self.mchain.keys():
        self.mchain[pair] = Dictogram()
      self.mchain[pair].add_count(tokens[i+2])

  def walk(self, length=10):
    sentence = ""
    pair = self.hist.sample()
    print(pair)
    sentence += f"{pair[0]} {pair[1]} "
    for i in range(length):
      pair = (pair[1], self.mchain[pair].sample())
      sentence += f"{pair[1]} "

    return sentence      

if __name__ == '__main__':
  if len(sys.argv) > 1:
      filename = sys.argv[1]
      source = open(filename).read()
      tokens = tokenize(source)
      start = MarkovbutBetter(tokens)

      realstart = start.walk()

      print(realstart)
  else:
      print('No source text filename given as argument')
  


    