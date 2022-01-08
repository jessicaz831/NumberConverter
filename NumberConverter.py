# Decimal, Binary, Octal, Hexadecimal converter
# Can convert a number from any number system listed above to a different number system listed above

'''
Converts decimal numbers to decimal, binary, octal, or hexadecimal
number is assumed to be entered correctly by the user, string
base is the base that number will be converted to, integer
returns user's number converted to indicated base
'''
def decToBase(number, base) :
    # since math operations are required, cast number into an int
    number = int(number)
    
    # converting decimal to decimal returns number with no changes
    if base == 10 :
        return number

    # decimal can be converted to any base using the constant division method
    else :
        quotients = [number]
        remainders = []

        # while number is greater than 1, continue dividing number by base and appending to quotients list
        while number > 1 :
            quotients.append(number // base)
            number = number // base

        # mod all numbers in quotients by base to get remainders and append to remainders list
        for i in range(0, len(quotients)) :
            # calculate remainder
            r = int(quotients[i]) % base
            
            # convert certain numbers to letters according to hexadecimal and append to remainders list
            if r == 10 :
                remainders.append('A')
            elif r == 11 :
                remainders.append('B')
            elif r == 12 :
                remainders.append('C')
            elif r == 13 :
                remainders.append('D')
            elif r == 14 :
                remainders.append('E')
            elif r == 15 :
                remainders.append('F')
            else :
                remainders.append(r)
        
        newnumber = ''

        # flips and combines remainders list into a string
        for item in remainders[::-1] :
            newnumber = newnumber + str(item)

        return newnumber

'''
Converts binary numbers to decimal, binary, octal, or hexadecimal
number is assumed to be entered correctly by the user, string
base is the base that number will be converted to, integer
returns user's number converted to indicated base
'''
def binToBase(number, base) :
    # converting binary to binary returns number with no changes
    if base == 2 :
        return number

    # convert binary to decimal
    elif base == 10 :
        indexes = []
        
        # traverses number backwards
        for i in range(len(number) - 1, -1, -1) :
            # if number at i is a '1' append the index - i to indexes list
            if number[i] == '1' :
                indexes.append(len(number) - 1 - i)
        
        newnumber = 0
        for i in range(0, len(indexes)) :
            # 2 ** indexes at i for all indexes then add together
            newnumber = newnumber + (2 ** indexes[i]) 

        return newnumber

    # convert binary to octal
    elif base == 8 :
        split = []
        count = 0
        temp = ''
        flipped = ''
        newnumber = ''
        octal = []

        # flip number so binary number is split properly
        flipped = number[::-1]
        
        # splits binary number into sections of 3
        for i in range(0, len(flipped)) :
            # when third number is reached, reset count, reset temp, append a flipped version of the number to the split list
            if count == 3 :
                count = 0
                split.append(temp[::-1])
                temp = ''
            # adds one character from flipped at a time
            temp = temp + flipped[i]
            # increment count to keep track of characters added
            count += 1
        # append the last split section
        split.append(temp[::-1])
        
        # run binary to decimal function on each split section and append to octal list
        for i in range(0, len(split)) :
            octal.append(str(binToBase(split[i], 10)))
        
        # combine converted numbers in octal starting from the end of the list into a string, since the original number was flipped in the beginning
        for i in range(len(octal) - 1, -1, -1) :
            newnumber = newnumber + octal[i]

        return newnumber

    # convert binary to hexadecimal
    elif base == 16 :
        split = []
        count = 0
        temp = ''
        flipped = ''
        newnumber = ''
        hexa = []

        # flip number so binary number is split properly
        flipped = number[::-1]
        
        # splits binary number into sections of 4
        for i in range(0, len(flipped)) :
            # when fourth number is reached, reset count, reset temp, append a flipped version of the number to the split list
            if count == 4 :
                count = 0
                split.append(temp[::-1])
                temp = ''
            # adds one character from flipped at a time
            temp = temp + flipped[i]
            # increment count to keep track of characters added
            count += 1
        # append the last split section
        split.append(temp[::-1])
        
        # run binary to decimal function on each split section and append to hexa list
        for i in range(0, len(split)) :
            # convert each split section from binary to decimal
            dec = str(binToBase(split[i], 10))

            # convert certain numbers to letters according to hexadecimal
            if dec == '10' :
                dec = 'A'
            elif dec == '11' :
                dec = 'B'
            elif dec == '12' :
                dec = 'C'
            elif dec == '13' :
                dec = 'D'
            elif dec == '14' :
                dec = 'E'
            elif dec == '15' :
                dec = 'F'

            hexa.append(dec)
        
        # combine converted numbers in hexa starting from the end of the list into a string, since the original number was flipped in the beginning
        for i in range(len(hexa) - 1, -1, -1) :
            newnumber = newnumber + hexa[i]

        return newnumber

'''
Converts octal numbers to decimal, binary, octal, or hexadecimal
number is assumed to be entered correctly by the user, string
base is the base that number will be converted to, integer
returns user's number converted to indicated base
'''
def octToBase(number, base) :
    # converting octal to octal returns number with no changes
    if base == 8 :
        return number

    # convert octal to decimal
    elif base == 10 :
        # run octal to binary function on number
        binarynum = octToBase(number, 2)

        # run binary to decimal function on binarynum
        newnumber = binToBase(binarynum, 10)

        return newnumber

    # convert octal to binary
    elif base == 2 :
        split = []
        binary = []
        temp = ''
        newnumber = ''

        # separates each character in number and appends to split list
        for i in range(0, len(number)) :
            split.append(number[i])
        
        # run decimal to binary function on each character in split list and append to binary list
        for i in range(0, len(split)) :
            binary.append(decToBase(int(split[i]), 2))
        
        # adds zeros to each item in binary list so each item has 3 characters
        for i in range(0, len(binary)) :
            # if the length of the character at i in binary is less than 3, add zeros
            if len(binary[i]) < 3 :
                # temporarily save the current item at i in binary
                temp = binary[i]
                # adds zeros to the beginning of the item at i to make it 3 characters long
                # ex. '1' becomes '001', '10' becomes '010'
                binary[i] = ('0' * (3 - len(binary[i]))) + temp

        # combines every item in binary list to a string
        for i in range(0, len(binary)) :
            newnumber = newnumber + binary[i]

        return newnumber
    
    # convert octal to hexadecimal
    elif base == 16 :
        # run octal to binary function on number
        binarynum = octToBase(number, 2)

        # run binary to hexadecimal function on number
        newnumber = binToBase(binarynum, 16)

        return newnumber

'''
Converts hexadecimal numbers to decimal, binary, octal, or hexadecimal
number is assumed to be entered correctly by the user, string
base is the base that number will be converted to, integer
returns user's number converted to indicated base
'''
def hexToBase(number, base) :
    # converting hexadecimal to hexadecimal returns number with no changes
    if base == 16 :
        return number

    # convert hexadecimal to decimal
    elif base == 10 :
        # run hexadecimal to binary function on number
        binarynum = hexToBase(number, 2)

        # run binary to decimal function on number
        newnumber = binToBase(binarynum, 10)

        return newnumber

    # convert hexadecimal to binary
    elif base == 2 :
        split = []
        binary = []
        temp = ''
        newnumber = ''

        # separates each character in number and appends to split list
        for i in range(0, len(number)) :
            hexa = number[i]

            # convert certain letters to numbers according to hexadecimal
            if hexa == 'A' :
                hexa = '10'
            elif hexa == 'B' :
                hexa = '11'
            elif hexa == 'C' :
                hexa = '12'
            elif hexa == 'D' :
                hexa = '13'
            elif hexa == 'E' :
                hexa = '14'
            elif hexa == 'F' :
                hexa = '15'
            
            split.append(hexa)
        
        # run decimal to binary function on each character in split list and append to binary list
        for i in range(0, len(split)) :
            binary.append(decToBase(int(split[i]), 2))
        
        # adds zeros to each item in binary list so each item has 4 characters
        for i in range(0, len(binary)) :
            # if the length of the character at i in binary is less than 4, add zeros
            if len(binary[i]) < 4 :
                # temporarily save the current item at i in binary
                temp = binary[i]
                # adds zeros to the beginning of the item at i to make it 4 characters long
                # ex. '1' becomes '0001', '10' becomes '0010'
                binary[i] = ('0' * (4 - len(binary[i]))) + temp

        # combines every item in binary list to a string
        for i in range(0, len(binary)) :
            newnumber = newnumber + binary[i]

        return newnumber
    
    # convert hexadecimal to octal
    elif base == 8 :
        # run hexadecimal to binary function on number
        binarynum = hexToBase(number, 2)

        # run binary to octal function on number
        newnumber = binToBase(binarynum, 8)

        return newnumber

'''
Prompts the user, collects inputs, runs and prints converted number according to inputbase and outputbase, and repeats program
'''
def prompt() : 
    # asks user what number system their number is in, repeats until they enter a valid number
    inputbase = input('What base is the number?\n1. Decimal\n2. Binary\n3. Octal\n4. Hexadecimal\n')
    while inputbase != '1' and inputbase != '2' and inputbase != '3' and inputbase != '4' :
        print('INVALID INPUT')
        inputbase = input('What base is the number?\n1. Decimal\n2. Binary\n3. Octal\n4. Hexadecimal\n')

    # asks user what number system they want to convert to, repeats until they enter a valid number
    outputbase = input('What base do you want to convert the number to?\n1. Decimal\n2. Binary\n3. Octal\n4. Hexadecimal\n')
    while outputbase != '1' and outputbase != '2' and outputbase != '3' and outputbase != '4' :
        print('INVALID INPUT')
        outputbase = input('What base do you want to convert the number to?\n1. Decimal\n2. Binary\n3. Octal\n4. Hexadecimal\n')

    base = 0
    # if user chooses decimal, base is 10
    if outputbase == '1' :
        base = 10
    # if user chooses binary, base is 2
    elif outputbase == '2' :
        base = 2
    # if user chooses octal, base is 8
    elif outputbase == '3' :
        base = 8
    # if user chooses hexadecimal, base is 16
    elif outputbase == '4' :
        base = 16

    # prompts user to enter the number they want to convert
    number = input('Enter the number: ')

    # if their number is decimal, run decimal to base passing in variables from above, prints return value
    if inputbase == '1' :
        print(decToBase(number, base))
    # if their number is binary, run binary to base passing in variables from above, prints return value
    elif inputbase == '2' :
        print(binToBase(number, base))
    # if their number is octal, run octal to base passing in variables from above, prints return value
    elif inputbase == '3' :
        print(octToBase(number, base))
    # if their number is hexadecimal, run hexadecimal to base passing in variables from above, prints return value
    elif inputbase == '4' :
        print(hexToBase(number, base))

    # after converting and printing their converted number, run repeat function
    # if repeat is true, run prompt again
    if repeat() == True:
        prompt()
    # if repeat is false, exit program
    else :
        exit(0)

'''
Asks if the user would like to convert another number
returns true or false value based on user's input
'''
def repeat() :
    # asks if user wants to convert another number
    # .upper() is used so if user enters 'y' or 'n' instead of 'Y' or 'N' it still works
    userinput = input('Would you like to convert another number? (Y/N)\n').upper()
    # if user chooses yes, return true
    if userinput == 'Y' :
        return True
    # if user chooses no, return false
    elif userinput == 'N' :
        return False
    # if user doesn't enter a valid answer, run repeat function again
    else :
        repeat()

# runs prompt function to start the program
prompt()
