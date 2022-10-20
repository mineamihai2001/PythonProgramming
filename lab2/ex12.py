def group_by_rhyme(words: list):
    rhymes = {}
    for word in words:
        rhyme = word[-2:]
        if rhyme in rhymes:
            rhymes[rhyme].append(word)
        else:
            rhymes[rhyme] = [word]   
    return list(rhymes.values())  

print(group_by_rhyme(['ana', 'banana', 'carte', 'arme', 'parte']))