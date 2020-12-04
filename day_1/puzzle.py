from functools import reduce
from itertools import combinations

# read file
def main():
    file = 'input.txt'
    def read_int(file):
        with open(file) as f:
            return list(map(int, f))

    numlist = read_int(file)

    # conditional, product
    combies = [x for x in combinations(numlist,2) if sum(x) == 2020]
    prod = [reduce(lambda x,y: x*y, pair) for pair in combies]
    print(prod)


if __name__ == '__main__':
    exit(main())