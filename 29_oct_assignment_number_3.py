sequences1 = ["ATCCAGCT", "GGGCAACT","ATGGATCT", "AAGCAACC","TTGGAACT", "ATGCCATT", "ATGGCACT"]
sequences2 = ["ATCCAGCT", "GGGCAACT","ATGGATCT", "AAGCAACC","TTGGAACT", "ATGCCATT", "ATGGCACT"] #sequences to create dimers and then to compare them and finding the hamming distance
combinations=[]
score=[]

def func1(seq1,seq2,score): #function to calculate the distance between two sequences and appending the score into an other list
    seqa=list(seq1) #converting into list, indivisual indexes will be converted of the sequences1 or sequences2 lists
    seqb=list(seq2)
    mis_match=0 #distance represented by mismatch and will be stored in the mismatch variable
    for i in range(8):
        if seqa[i]!=seqb[i]:
            mis_match+=1
    score.append(mis_match) #appending the score into the score list
    return mis_match #returning the mismatch value
for i in range(7):
    for j in range(7):
        combinations.append(sequences1[i]) #each indivisual indexes will be returned to the function 1 and then the distances will be calculated
        combinations.append(sequences2[j])
        x=func1(sequences1[i],sequences2[j],score)
        data="the diatance between {} and {} is {}".format(sequences1[i],sequences2[j],x) #displaying in the form as asked by sir nadeem
        print(data)
        
# hamming and levenshtein distances explained with the help of an example
"""
hamming distance:
    the meaure of dissimilarity between two sequences
    i.e. the number of positions at which a residue needs to be changed
    number of subsitutions need to transform one string into another
    ATCGGTAGT
      | | ||              
    ATGGTTCCT
    hence the hamming distance is 4
levenshtein distance:
    levenshtein diatance is also a method calculate dissimilarity between two sequences but is more advanced as compared with hamming
    distance
    it inserts gaps and then modify the sequences and then compare two strings to find the distance
    consider these two sequences
    ATCGGATGGG
    ||| |||  |            
    TCGGTTGGGAC
    the hamming distance would be 7 but is not as much accurate
    if we insert gaps, then
    ATCGGATGGG--
    |    |    ||             
    -TCGGTTGGGAC
    hence after gap insertion the levenshtein distance would be only 4
    
    
"""
