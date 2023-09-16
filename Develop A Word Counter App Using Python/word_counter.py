search_words = ["Python", "C", "OOP", "Hello", "java"]


for x in range(len(search_words)):
    word = search_words[x]

    count = 0
    with open("input.txt", 'r') as f:
        for line in f:
            words = line.split()
            for i in words:
                if(i.lower()==word.lower()):
                    count=count+1
    print(word.capitalize(), "->", count)

