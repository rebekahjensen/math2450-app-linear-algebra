import numpy as np

#implement a symmetric binary channel 
#& 2 codes to detect & correct codes
#passing thru that channel
#scalars 0 or 1

### Parity Check Code ###
#encode_paritycheck takes one input parameter and appends the check-bit @ the end of the array & outputs encoded message
def encode_paritycheck(message):

    count_ones = sum(message) #count number of ones

    if count_ones % 2 == 0:
        checked_bit = 0 #even
        print(f"{count_ones} is correct (even). Append 0 to keep even.")
    else:
        checked_bit = 1 #odd
        print(f"{count_ones} is incorrect (odd). Append 1 to make even.")

    encoded_message = message + [checked_bit] #og message plus new parity bit
    return encoded_message

#check with example
print(encode_paritycheck([1,1,0,1]))
print(encode_paritycheck([1,1,0,1,1]))

#takes 1 input parameter, a codeword encoded by previous function
#function checks last bit, returns True if error is detected
#false otherwise

def detect_paritycheck(codeword):
    #check last bit, return True if error is found
    #to the point!
    all_ones = sum(codeword)
    return all_ones % 2 != 0 #even/odd, 0/1

print(detect_paritycheck([1,1,0,1]))
print(detect_paritycheck([1,1,0,1,1]))


#take one input codeword & remove check-bit at end of array
#then output decoded message 
#combine these two tasks to decode codewords or detect possible errors
decode_paritycheck = lambda codeword : codeword[:-1] #remove parity bit

# ### Triple Repetition Code ###  
# #let's do this 3 times!! then split and find most common value
# def encode_triplerep(message):

#     #write your code here
#     #returns triple_repeated_message

# def decode_triplerep(codeword):
#     #write your code here
#     #returns decoded_message (with errors corrected)
        
### VERIFICATION ############################

print(" Task 1\n")
print(encode_paritycheck([1,1,0,1]), "\n")

#The last bit is a parity-check bit.
Words = np.array([[0,0,1,1,0,1,1],
                  [1,1,1,0,1,1,0],
                  [1,0,0,1,0,1,1],
                  [1,1,0,0,1,1,1],
                  [1,1,1,1,1,1,0]])
for w in Words:
    if detect_paritycheck(w):
        print("Error: ", w)
    else:
        print(decode_paritycheck(w))
 
# print("\n\n Task 2\n")
# Words = np.array([[1,1,0,0],
#                   [0,0,1,1],
#                   [0,1,1,0]])
# for w in Words:
#     print(encode_triplerep(w))
# print("\n")

# Codewords = np.array([[0,0,1,1,0,1,0,0,1,0,0,1,0,0,1,1,0,1],
#                       [0,1,0,0,1,1,1,1,1,0,1,0,1,1,1,0,1,1],
#                       [1,0,0,0,1,1,1,0,1,1,0,1,0,0,0,1,1,1],
#                       [0,1,0,0,1,1,1,1,0,0,1,1,1,1,0,0,0,1],
#                       [1,1,1,1,1,1,1,0,0,1,0,0,1,0,1,1,1,1]])
# for c in Codewords:
#     print(decode_triplerep(c))