def get_codon(sequence):
    codons=[]
    length=len(sequence)
    for i in range(0,length,3):
        codon=sequence[i:i+3]
        if codon=='UGA' or codon=='UAA' or codon=='UAG':
            codon='*'
        codons.append(codon)
    return codons
get_codon("AUGGGUAGCCCUAAUACUAGUCCUAAAAAG")
