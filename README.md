## Knuth-Morris-Pratt algorithm

This repository contain ```KMP_algorithm_modified.py``` and ```KMP_algorithm.py``` algorithm 

and also automatic test for algorithm ```test_KMP_algorithm.py```

### Time and Space decision

algoritm in file ```KMP_algorithm.py``` is basic approach and take time complexity in worst case O(M*N) where M is ammount of unique symbol and N is len of text 

and also it take size O(N*M)

algoritm in file ```KMP_algorithm_modified.py``` is slightly modified approach. It take time complexity in worst case O(N)

and size comlexity also is O(n) what iss better than in basic

### Sloving problems:

I tell you about modified algorithm

Firstly, my approach take pattern (and run ```create_dfa``` function) 

for even substring, what begins at the beginning of pattern it search longest suffix and prefix such that sufix is equal prefix

and write len of prefix to array of prefixs 

then algorithm start finding pattern (starts main block of function ```find_substring```)

even symbol of text wich we check algorithm check with pattern symbol 

and if symbols not match my approach vheck same prefix wether they matches if not it start search pattern with beginning of pattern  

### Usage:

Programming Language: python.

Firstly, download repo:     ```git clone https://github.com/tiforn/Algorithm_part1.git```

then open package:   ```cd Algorithm_part1```

go to branch lab4   ```git checkout lab5```

and run python file  ```python main.py```
