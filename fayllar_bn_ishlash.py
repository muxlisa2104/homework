import pickle

fayl = open('pi_million_digits.txt')
pi = fayl.read()
print(pi)
fayl.close()


pi = pi.rstrip() # qator ohiridagi bo'shliqlarni olib tashlaymiz
pi = pi.replace('\n','') # qator tashlash belgisini almashtiramiz
t_kun = '21042008'
print(t_kun in pi)

with open('pi','wb') as file:
    pickle.dump(pi,file)
