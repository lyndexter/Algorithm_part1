def create_dfa(text):
    prefixes_for_symbol = [0 for _ in text]

    prefix_length = 0
    prefixes_for_symbol[0] = 0
    symbol_index = 1

    while symbol_index < len(text):
        if text[prefix_length] == text[symbol_index]:
            prefix_length += 1
            prefixes_for_symbol[symbol_index] = prefix_length
            symbol_index += 1

        else:
            if prefix_length > 0:
                prefix_length = prefixes_for_symbol[prefix_length - 1]
            else:
                prefixes_for_symbol[symbol_index] = 0
                symbol_index += 1

    return prefixes_for_symbol


def find_substring(text, pattern):
    automaton = create_dfa(pattern)

    result = []
    symbol_index = 0
    match_index = 0

    while symbol_index < len(text):
        if text[symbol_index] == pattern[match_index]:
            symbol_index += 1
            match_index += 1

        if match_index == len(pattern):
            result.append(symbol_index - len(pattern))
            match_index = automaton[match_index - 1]

        if symbol_index < len(text) and text[symbol_index] != pattern[
            match_index]:
            if match_index == 0:
                symbol_index += 1
            else:
                match_index = automaton[match_index - 1]

    return result


if __name__ == '__main__':
    print(find_substring("erfefsdfdsefeff", "efef"))
    # print(create_dfa("efefr"))
