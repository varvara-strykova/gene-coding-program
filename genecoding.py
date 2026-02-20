
def read_dna(filename):
    # reads the file and returns the data without empty lines and 'ERROR' strings
    cleaned_dna = []
    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()  # removes leading and trailing whitespaces
            if line != '' and line != 'ERROR':
                cleaned_dna.append(line)
    return cleaned_dna

def shuffle(cleaned_dna):
    # sorts the data from the inputed list by adding elements by alternating between the right and the left part and returns the shuffled list  
    shuffled_dna = []
    mid = len(cleaned_dna)//2
    left = mid - 1
    right = len(cleaned_dna)-1
    
    # the loop ensures that the pointers will not go out of bounce
    while left >= 0 or right >= mid:  
        if left >= 0:
            shuffled_dna.append(cleaned_dna[left])
            left = left - 1  
        if right >= mid:
            shuffled_dna.append(cleaned_dna[right]) 
            right = right - 1
    return shuffled_dna
   
def select_strands(shuffled_dna, num_strands):
    # returns a dna strand, a list of dna strands of a None based on the value of num_strands 
    strand = ''
    list = []
    if len(shuffled_dna) >= num_strands:
        if num_strands == 1:
            strand = str(shuffled_dna.pop())
            return strand
        elif num_strands > 1:
            # pops and appends the last element from one string to another
            for num in range(0, num_strands):
                list.append(shuffled_dna.pop())
            return list
    else: 
        return None
    
def strand_stabillity(dna_strand):
    # checks the first letter of the strand and returns its stabillity value 
    strand_value = 0
    starting_l = ['U', 'C', 'A', 'G']
    for i in range(len(starting_l)):
        # checks the first charactr and assings the value based on it
        if dna_strand[0] == starting_l[i]:
            strand_value = strand_value + (i+2)
    return strand_value
        
def chain_stabillity(dna_chain):
    # adds all strand stabillity values in a chain to calculate chain stabillity value and return in 
    chain_value = 0
    for strand in range(len(dna_chain)):
        chain_value = chain_value + strand_stabillity(dna_chain[strand])
    return chain_value

def needs_mutation(dna_chain):
    # checks if the chain stabillity values is greated than 10 and returns a bool
    chain_value = chain_stabillity(dna_chain)
    if chain_value < 10:
        return True
    return False

def mutate_chain(dna_chain, shuffled_dna):
    # if length of shaffled_dna is greater than 0 and check for mutation holds True, appends 1 strand from shuffled_dna to the dna_chain
    check = needs_mutation(dna_chain)
    if len(shuffled_dna) > 0 and check:
        num_strands = 1
        dna_strand = select_strands(shuffled_dna, num_strands)
        dna_chain.append(dna_strand)
        
def compare_chains(chain_1, chain_2):
    # compares chain 1 to chain 2 and returns the string based on the result
    chain_1_stab = chain_stabillity(chain_1)
    chain_2_stab = chain_stabillity(chain_2)
    string = ''
    if chain_1_stab <= 14 and chain_2_stab <= 14:
        if chain_1_stab > chain_2_stab:
            string = 'Chain 1 wins!'
        elif chain_1_stab < chain_2_stab:
            string = 'Chain 2 wins!'
        else:
            string = 'Tie!'
    elif chain_1_stab > 14 or chain_2_stab > 14:
        if chain_1_stab > 14:
            string = 'Chain 2 wins!'
        else:
            string = 'Chain 1 wins!'
    else:
        string = 'Both are unstable'
    return string


def main():
    filename = input('Enter a filename: ')
    cleaned_dna = read_dna(filename)
    shuffled_dna = shuffle(cleaned_dna)
    
    while len(shuffled_dna) > 6:
        num_strands = 3
        chain_1 = select_strands(shuffled_dna, num_strands)
        chain_2 = select_strands(shuffled_dna, num_strands)
        print(f'Chain 1 before: {chain_1}')
        print(f'Chain 2 before: {chain_2}')        
        mutate_chain(chain_1, shuffled_dna)
        mutate_chain(chain_2, shuffled_dna)
        print(f'Chain 1 after: {chain_1}')
        print(f'Chain 2 after: {chain_2}') 
        result = compare_chains(chain_1, chain_2)
        print(result)
        print()
main()
