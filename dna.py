import csv
import sys


def main():

    # Ensure proper usage
    if len(sys.argv) != 3:
        sys.exit("Usage: python dna.py data.csv sequence.txt")

    # Read database of people and their DNA sequences and store in array
    people = []
    with open(sys.argv[1], "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            people.append(row)

    # Store all STRs in array (no duplicates)
    strs = []
    for person in people:
        for key, value in person.items():
            if key != "name":
                if not(key in strs):
                    strs.append(key)
    
    # Open and read file
    # and store DNA sequence in 'seq'
    seq = open(sys.argv[2], "r").read()
    
    # Find longest match of each STR in DNA sequence
    # and store in 'dna' dict
    dna = {}
    for str in strs:
        dna[str] = longest_match(seq, str)
    
    # Check database for matching profiles
    result = "No match"
    for person in people:
        match = 1
        name = ""
        for key, value in person.items():
            if key != "name":
                if int(value) != dna[key]:
                    match = 0
            else:
                name = value

        if match == 1:
            result = name
            break
    
    print(result)
    return

def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):

        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:

            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1
            
            # If there is no match in the substring
            else:
                break
        
        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run


main()
