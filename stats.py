def get_num_words(text):
    words = text.split()
    return len(words)


def get_chars_stats(text):
    stat_list = []
    char_list = list(text.lower())
    _s = set()
    for cl in char_list:
        if cl in _s:
            for cd in stat_list:
                if cd.get("char", "~") == cl:
                    cd["num"] = cd["num"] + 1
        else:
            if cl.isalpha():
                stat_list.append({"char": cl, "num": 1})
                _s.add(cl)
    result = sorted(stat_list, reverse=True, key=lambda x: x["num"])
    return result
