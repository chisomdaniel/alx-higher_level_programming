#!/usr/bin/python3

def text_indentation(text):

    if type(text) != str:
        raise TypeError("text must be a string")

    text_list = text.split(".")

    text_list_2 = []
    text_list_3 = []
    for i in text_list:
        text_list_2 += i.split("?")
    for i in text_list_2:
        text_list_3 += i.split(":")

    for i in text_list_3:
        new_text_list = i.strip()
        print(new_text_list,  "\n")


text_indentation("""Lorem ipsum dolor sit amet, consectetur adipiscing elit. \
        Quonam modo? Utrum igitur tibi litteram videor an totas paginas commovere? \
        Non autem hoc: igitur ne illud quidem. Fortasse id optimum, sed ubi illud: \
        Plus semper voluptatis? Teneo, inquit, finem illi videri nihil dolere. \
        Transfer idem ad modestiam vel temperantiam, quae est moderatio cupiditatum \
        rationi oboediens. Si id dicis, vicimus. Inde sermone vario sex illa a Dipylo \
        stadia confecimus. Sin aliud quid voles, postea. Quae animi affectio suum \
        cuique tribuens atque hanc, quam dico. Utinam quidem dicerent alium alio \
        beatiorem! Iam ruinas videres""")
