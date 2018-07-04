def to_rna(dna_strand):
    m = {'C':'G',
         'G':'C',
         'T':'A',
         'A':'U'
         }
    s = ''
    for i in dna_strand:
        if i.upper() not in m:
            raise Exception('Bad Parameters')
        else:
            s += m[i]
    return s

