

data = "There Are many variations of passages of Lorem Ipsum available," \
       " but the majority have suffered alteration in some Form, by injected" \
       " humour, or randomised words which don't look even slightly believable." \
       " If you are going to use a Passage of Lorem Ipsum, you Need to be sure" \
       " there isn't anything embarrassing Hidden in the middle of text." \
       " All the Lorem Ipsum generators on the Internet tend to repeat predefined" \
       " chunks as necessary, making this the first true generator on the Internet." \
       " It uses a dictionary of over 200 Latin words, combined with a handful of model" \
       " Sentence structures, to Generate Lorem Ipsum which looKs reasonable." \
       " The generated Lorem Ipsum is therefore always free from repetition," \
       " injected humour, or non-characteristic words etc."

# create a empty dictionary
word_occurence = {}
# store each character as uppercase
for i in data.upper():
    if i in word_occurence:
        word_occurence[i] += 1
    elif i.isalpha():           # Take just characters, not punctuations.
        word_occurence[i] = 1
    else:
        continue

print(str(word_occurence))


# ############################################################# The End 
