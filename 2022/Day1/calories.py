def process(l):
    split_input = l.split('\n\n')
    sublists = [sl.split('\n') for sl in split_input]
    
    # Top 1 elf
    print(max([sum(int(i) if i != '' else 0 for i in sl) for sl in sublists]))

    # Top 3 elves
    print(sum(sorted([sum(int(i) if i != '' else 0 for i in sl) for sl in sublists])[-3:]))

if __name__ == '__main__':
    with open('part1', 'r') as f:
        l = f.read()
        process(l)
