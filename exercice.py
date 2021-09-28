#!/usr/bin/env python
# -*- coding: utf-8 -*-

from matplotlib.colors import cnames


def list_to_dict(some_list: list) -> dict:
    # TODO: Transformer la liste en dictionnaire, les éléments de la liste deviennent les clés et leur index deviennent les valeurs
    diction={}

    for element in some_list:
        diction[element]=some_list.index(f"{element}")

    return diction


def color_name_to_hex(colors: list) -> list:
    # TODO: Trouver la valeur hex de chaque couleur dans la liste et créer une liste de tupple où le premier élément est le nom de la couleur et le deuxième est la valeur hex
    list_tuple=[]

    for element in colors:

        couleur_tuple=(element,cnames[element])
        list_tuple.append(couleur_tuple)

    return list_tuple


def create_list() -> list:
    # TODO: Créer une liste des 10 000 premiers entiers positif, sauf pour les entiers de 15 à 350
    list_entier=[]

    for nb in range(0, 10001):
        if nb>=15 and nb <=350:
            continue

        list_entier.append(nb)

    return list_entier


def compute_mse(model_dict: dict) -> dict:
    # TODO: Calculer l'erreur quadratique moyen pour chaque modèle. Retourner un dictionnaire contenant les MSE.
    somme_prevu= 0
    somme_reel= 0
    compt=0
    dict_erreur={}

    for key in model_dict:
        somme_prevu= 0
        somme_reel= 0
        compt=0
        for couple in model_dict[key]:
            somme_prevu+=(couple[1])**2
            somme_reel+=(couple[0])**2
            compt+=1
        
        moyenne_prevu=(somme_prevu/compt)**0.5
        moyenne_reel=(somme_reel/compt)**0.5
        dict_erreur[key]=(moyenne_reel,moyenne_prevu)

    return dict_erreur


def main() -> None:
    some_list = ["a", "b", "z", "patate"]
    print(f"La liste suivante {some_list} est transformée en dictionnaire: {list_to_dict(some_list)}")

    colors = ["blue", "red", "green", "yellow", "black", "white"]
    print(f"La valeur hex associée aux couleurs est: {color_name_to_hex(colors)}")

    print(f"La liste des 10000 entiers est: {create_list()}")

    model_dict = {"LR": [(90, 92), (96, 100), (20, 25), (21, -2), (3, -20)],
                  "DNN": [(100, 101), (50, 50), (1,2), (-10, -12), (-1, 7)],
                  "RF": [(10, 19), (56, 70), (1, 9), (-100, -12), (-11, 7)]}
    print(f"Le mse des différents modèles est: {compute_mse(model_dict)}")


if __name__ == '__main__':
    main()
