#### Fonction secondaire

"""
On cherche à vérifier si un entier est premier ou pas.
"""
def isprime(p):

    """
    Checke si p est un nombre premier.

    p est un int.

    Retourne des booléens : Si p est premier retourne VRAI, si p n'est pas premier retouorne FAUX.
    """
    #Cas de base
    if p<= 1:
        return False
    if p<= 3:
        return True
    if p%2==0 or p%3==0:
        return False

    #Vérification divisibles jusqu'à racine carrée de p
    i = 5
    while i*i <= p:
        if p%i==0 or p%(i + 2)==0:
            return False
        i += 6
    return True

#### Fonction principale

def main():

    """
    Appelle la fonction isprime(p) avec n = 100
    """
    # vos appels à la fonction secondaire ici

    for n in range(100):
        if isprime(n):
            print(n, end=", ")

    print()


if __name__ == "__main__":
    main()
