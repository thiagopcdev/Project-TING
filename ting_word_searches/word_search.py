
def occurrence_constructor(word, phrases, have_content=False):
    occurrences_list = list()

    for i in range(len(phrases)):
        if word.lower() in phrases[i].lower():
            line = i + 1
            occurrence = {"linha": line}
            if have_content:
                occurrence['conteudo'] = phrases[i]
            occurrences_list.append(occurrence)

    return occurrences_list


def search_engine(word, instance, have_content=False):
    file_list = instance.data
    result_list = list()

    for file in file_list:
        file_name = file['nome_do_arquivo']
        phrases = file['linhas_do_arquivo']
        occurrences_list = occurrence_constructor(word, phrases, have_content)

        result = {
            "palavra": word,
            "arquivo": file_name,
            "ocorrencias": occurrences_list
        }

        if(len(occurrences_list) > 0):
            result_list.append(result)

    return result_list


def exists_word(word, instance):
    return search_engine(word, instance)


def search_by_word(word, instance):
    return search_engine(word, instance, True)
