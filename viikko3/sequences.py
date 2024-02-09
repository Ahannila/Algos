def count(s):
    count_tira = 0
    running_counts = {'T': 0, 'I': 0, 'R': 0, 'A': 0}

    for char in s:
        char = char.upper()  # Consider both uppercase and lowercase letters

        if char in running_counts:
            count_tira += running_counts[char]

        # Update running counts
        for key in running_counts:
            if key == char:
                running_counts[key] += 1
            else:
                running_counts[key] = 0

    return count_tira

if __name__ == "__main__":
    print(count("aybabtu"))            # 0
    print(count("tira"))                # 1
    print(count("ritari"))              # 6
    print(count("tiratiratira"))        # 45
    print(count("xaxrxixtx"))           # 4
