def create_dfa(text):
    unique_symbols = set(text)
    automaton = {symbol: [0 for _ in text] for symbol in unique_symbols}
    print(automaton)
    prev_index = 0
    automaton[text[0]][0] = 1
    for symbol_index, symbol in enumerate(text):
        if symbol_index == 0: continue

        for unique_symbol in unique_symbols:
            automaton[unique_symbol][symbol_index] = automaton[unique_symbol][
                prev_index]
        automaton[symbol][symbol_index] = symbol_index + 1
        prev_index = automaton[symbol][prev_index]

    for key, row in automaton.items():
        print("{} - {}".format(key, row))
    return automaton


def find_substring(text, pattern):
    automaton = create_dfa(pattern)
    result = []
    length = 0
    index = 0
    for symbol in text:
        index += 1
        if symbol not in automaton:
            length = 0
            continue
        length = automaton[symbol][length]

        if length == len(pattern):
            result.append(index - len(pattern))
            length = 0
    return result


if __name__ == '__main__':
    print(find_substring("efefeff", "efef"))
    pass
