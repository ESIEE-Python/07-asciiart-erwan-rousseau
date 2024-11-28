""" Code permettant d'encode des string"""
def artcode_i(s):
    """retourne la liste de tuples encodant une chaîne de caractères passée en argument selon 
    un algorithme itératif
    Args:
        s (str): la chaîne de caractères à encoder
    Returns:
        list: la liste des tuples (caractère, nombre d'occurences)
    """
    list_tuple =[]
    char = s[0]
    compteur =0
    for element in s:
        if element == char:
            compteur +=1
        else:
            list_tuple.append((char,compteur))
            compteur =1
            char = element
    list_tuple.append((char,compteur))
    return  list_tuple

def artcode_r(string):
    """retourne la liste de tuples encodant une chaîne de caractères passée en argument selon 
    un algorithme récursif
    Args:
        s (str): la chaîne de caractères à encoder

    Returns:
        list: la liste des tuples (caractère, nombre d'occurences)
    """
    if len(string)==0:
        return []
    compteur=1
    char = string[0]   
    while compteur<len(string):
        if string[compteur]==char:
            compteur +=1
        else:
            break
    return [(char,compteur)]+artcode_r(string[compteur:])
#### Fonction principale


def main():
    """fonction d'appelle principale"""
    print(artcode_i('MMMMaaacXolloMM'))
    print(artcode_r('MMMMaaacXolloMM'))

if __name__ == "__main__":
    main()
