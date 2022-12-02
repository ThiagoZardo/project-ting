def exists_word(word, instance):
    word_insensitive = word.lower()
    line_of_file = []
    for i in range(len(instance)):
        if instance.search(i) == word_insensitive:
            line_of_file.append(instance['linhas_do_arquivo'])
    return line_of_file


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
