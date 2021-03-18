with open("next_generation.txt", "w") as f:
    for i in range(2000, 2043):
        f.write(str(i) + " ")
        if i % 10 == 0:
            f.write("\n")
