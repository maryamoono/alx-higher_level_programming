#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    list_keys = list(a_dictionary.keys())

    for ue_dic in list_keys:
        if value == a_dictionary.get(ue_dic):
            del a_dictionary[ue_dic]

    return (a_dictionary)
