import numpy as np

# #implement a symmetric binary channel 
# #& 2 codes to detect & correct codes
# #passing thru that channel
# #scalars 0 or 1

# ### Parity Check Code ###
# #encode_paritycheck takes one input parameter and appends the check-bit @ the end of the array & outputs encoded message

# #actually implement vectoes as np.arrays LOL
# #get rid of if/else too

# def encode_paritycheck(message):

#     msg_ar = np.array(message) #create array
#     checked_bit = np.sum(msg_ar) % 2 #odd or even? check 'em

#     # if count_ones % 2 == 0:
#     #     checked_bit = 0 #even
#     #     print(f"{count_ones} is correct (even). Append 0 to keep even.")
#     # else:
#     #     checked_bit = 1 #odd
#     #     print(f"{count_ones} is incorrect (odd). Append 1 to make even.")

#     #easier than you think...
#     encoded_message = np.append(msg_ar, checked_bit) #og message plus new parity bit
#     return encoded_message

# #check with example
# print(encode_paritycheck([1,1,0,1]))
# print(encode_paritycheck([1,1,0,1,1]))

# #takes 1 input parameter, a codeword encoded by previous function
# #function checks last bit, returns True if error is detected
# #false otherwise

# def detect_paritycheck(codeword):
#     #check last bit, return True if error is found
#     #to the point!
#     all_ones = sum(codeword)
#     return all_ones % 2 != 0 #even/odd, 0/1

# print(detect_paritycheck([1,1,0,1]))
# print(detect_paritycheck([1,1,0,1,1]))


# #take one input codeword & remove check-bit at end of array
# #then output decoded message 
# #combine these two tasks to decode codewords or detect possible errors
# decode_paritycheck = lambda codeword : codeword[:-1] #remove parity bit

############# NEXT  ASSIGNMENT ##########################
#Task 1
def encode_triplerep(message):
    msg = np.array(message) #create array
    encoded = []
    triple_repeated_message = np.tile(message,3) #triple repeat array

    return triple_repeated_message

#Task 2
def decode_triplerep(codeword):
    codeword = np.array(codeword)
    n = len(codeword) // 3 #len of OG
    decoded_message = [] #array to store

    #restore original message in 3!! triple encoded
    for i in range(n):
        triple_bits = [codeword[i],codeword[i+n],codeword[i+2*n]]
        single_bits = sum(triple_bits) 

        if single_bits >= 2:
            decoded_message.append(1)
        else:
            decoded_message.append(0)

    return np.array(decoded_message) #og message

        
### VERIFICATION ######
Words = np.array([[1,1,0,0],
                  [0,0,1,1],
                  [0,1,1,0]])

#comment out as neccessary:

# for w in Words:
#     print(encode_triplerep(w))
# print("\n")

Codewords = np.array([[0,0,1,1,0,1,0,0,1,0,0,1,0,0,1,1,0,1],
                      [0,1,0,0,1,1,1,1,1,0,1,0,1,1,1,0,1,1],
                      [1,0,0,0,1,1,1,0,1,1,0,1,0,0,0,1,1,1],
                      [0,1,0,0,1,1,1,1,0,0,1,1,1,1,0,0,0,1],
                      [1,1,1,1,1,1,1,0,0,1,0,0,1,0,1,1,1,1]])
for c in Codewords:
    print(decode_triplerep(c))

