sentence = 'The quick brown fox jumped over the lazy dog.'

# query = sentence.find('oops')
# query_two = sentence.index('oops')

# print(query)
# print(query_two)

query = 'oops' in sentence
query_two = 'fox' in sentence

print(query)
print(query_two)