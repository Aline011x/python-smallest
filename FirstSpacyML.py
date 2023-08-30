import spacy
nlp = spacy.load("en_core_web_lg")

w1 = 'sunny'
w2 = 'rainy'

w1 = nlp(w1)
w2 = nlp(w2)

print(w1.similarity(w2))

s1 = 'the tea is so hot'
s2 = 'the wheather is very awfull'
s3 = 'the snowman is so cold'


s1 = nlp(s1)
s2 = nlp(s2)
s3 = nlp(s3)


print(s1.similarity(s2))
print(s1.similarity(s3))
print(s3.similarity(s2))

