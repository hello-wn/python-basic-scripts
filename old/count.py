def count():
    f = open("fileForCount.txt")
    lines = f.readlines()
    count = {}
    for l in lines:
        words = l.strip().split(' ')
        for w in words:
            if w in count:
                count[w] += 1
            else: 
                count[w] = 1
    print(count)
    
count()

