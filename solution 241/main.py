with open("dataset_24465_4.txt", "r") as r, open("test2.txt", "w") as w:
    x = r.read().rstrip()
    w.write(x[::-1])
