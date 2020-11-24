## Longest Chain

task is in wchain.pdf

This repository contain word_chain.py - algorithm and word_chain_test.py - automatic test for algorithm

### Sloving problems:

Firstly, my approach sorts words by their length

then it go from litle to bigger words and chek if i can make from this word smaller, that contain one letter less

if algorithm found these smaller words:

it's finding smaller word with longest chain of words what we can do

and than write word and chain of smaller word + 1(because we add one more word to chain) in dictionary

if word is not found it just write this word with length of chain 1 in dictionary

and in the end he just output the longest chain from dictionary

### Usage:

Programming Language: python.

Firstly, download repo:     ```git clone https://github.com/tiforn/Algorithm_part1.git```

then open package:   ```cd Algorithm_part1```

go to branch lab4   ``` git checkout lab4```

and run python file  ```python word_chain.py```
