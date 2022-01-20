def main():
    # Index n of the counts_list will contain a dictionary which maps
    # all values in the OEIS at position n+1 to their number of occurrences
    counts_list = []

    # Open the unzipped file containing every OEIS sequence
    with open('stripped') as f:
        count = 0
        for line in f:
            # Skip the headers
            if count < 4:
                count += 1
                continue

            # Convert each line to a list
            line = str(line)
            line = line[9:]
            line = line.replace(',', ' ')
            line = line.split()
            
            # Update the counts at each index
            for index, num in enumerate(line):
                    if len(counts_list) <= index:
                        counts_list.append({})
                    if counts_list[index].get(num) == None:
                        counts_list[index][num] = 0
                    counts_list[index][num] += 1
    seq = []
    for d in counts_list:
        # Compute the most common integer at each index
        seq.append(max(d, key=lambda k: d[k]))
    
    # Convert to string
    seq_str = ''
    for num in seq:
        seq_str += num + ','
    seq_str = seq_str[:-1]

    #Print the 'most common sequence'
    print(seq_str)
    print(len(seq_str))
    print(seq_str[:261])

if __name__ == '__main__':
    main()