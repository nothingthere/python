#!/usr/bin/python3
# Author: Claudio <3261958605@qq.com>
# Created: 2017-05-13 17:37:38
# Commentary:
# Code:
"英语句子随机生成"

import random


class Version1:
    def __init__(self):
        pass

    def sentence(self):
        return self.noun_phrase() + self.verb_phrase()

    def noun_phrase(self):
        return self.Article() + self.Adj_() + self.Noun() + self.PP_()

    def verb_phrase(self):
        return self.Verb() + self.noun_phrase()

    def Adj_(self):
        if random.choice(range(2)) == 0:
            return []
        else:
            return self.Adj() + self.Adj_()

    def PP_(self):
        if random.choice(range(2)) == 0:
            return []
        else:
            return self.PP() + self.PP_()

    def Article(self):
        return [random.choice(['the', 'a'])]

    def Noun(self):
        return [random.choice(['man', 'ball', 'woman', 'table'])]

    def Verb(self):
        return [random.choice(['hit', 'took', 'saw', 'liked'])]

    def Adj(self):
        return [random.choice(['big', 'little', 'blue', 'green', 'adiabatic'])]

    def PP(self):
        return self.Prep() + self.noun_phrase()

    def Prep(self):
        return [random.choice(['to', 'in', 'by', 'with', 'on'])]


class Version2:
    def __init__(self, big=False):
        if big:
            self.__grammer = self.__big_grammer

    def create_grammar(**grammer):
        for cat, rhs in grammer.items():
            grammer[cat] = [alt.split() for alt in rhs.split('|')]
        # print(grammer)
        return grammer

    __grammer = create_grammar(
        S='NP VP',
        NP='Art N',
        VP='V NP',
        Art='the | a',
        N='man | ball | woman',
        V='hit | took | saw | liked'
    )

    __big_grammer = create_grammar(
        S='NP VP',
        NP='Art Adj_ N PP_ | Name | Pro',
        VP='V N PP_',
        PP_=' | PP PP_',
        Adj_=' | Adj Adj_',
        PP='Pre N',
        Pre='to | in | by | with | on',
        Adj='big | little | blue | green | adiabatic',
        Art='the | a',
        Name='Pat | Kim | Lee | Terry | Robin',
        N='man | woman | ball | table',
        V='hit | took | saw | liked',
        Pro='he | she | it | these | those | that'
    )

    def generate(self, symbol='S'):
        if symbol not in self.__grammer:
            return symbol
        else:
            return ' '.join(map(self.generate, random.choice(self.__grammer[symbol])))

    def generate_tree(self, symbol='S'):
        if symbol not in self.__grammer:
            return symbol
        else:
            return {symbol: list(map(self.generate_tree, random.choice(self.__grammer[symbol])))}


if __name__ == '__main__':
    sentence = Version2()
    print(sentence.generate())
