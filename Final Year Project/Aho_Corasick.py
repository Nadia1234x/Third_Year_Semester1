from collections import deque

output_function = []
number_of_states = 0
failure = [0] * (40 - 1) #sort out the 40

                
def build_FSM(file_name):
    
    
    #26 x 26 2-D array

    number_of_characters = 0

    #---initialise the output_function
    file = open(file_name, "r")

    for line in file:
        #check the file line by line. 
        word_list = line.split(" ")
        for word in word_list:
            word = word.rstrip()
            number_of_characters = number_of_characters + len(word)
        global output_function
        output_function = number_of_characters * [0] 
    print "no of char", number_of_characters 
    FSM = [[-1 for x in range(26 + 10)] for y in range(number_of_characters + 10)] #sort this out!!
    
    #---pass each word to add to the FSM. 
    file1 = open(file_name, "r")

    for line in file1: 
        word_list = line.split(" ")
        print "The word_list is: ", word_list
        for word in word_list:
            word = word.rstrip()
            print "The word 1 is: ", word
            current_state = 0   

            word_char_list = list(word)

            #print "The number of states:", number_of_states
            
            #print "number of states", number_of_states 
            #print output_function
            
            for character in word_char_list:
                
                alphabet_num = convert_alphaChar_to_int(character)
                #only considering alphabet characters, may need to change
                #because virus signatures may not only have alphabet
                if(alphabet_num > 25 or alphabet_num < 0): #clean this part up. 
                    break                           
                print character, alphabet_num
                print "current_state", current_state
                
                if(FSM[current_state][alphabet_num] == -1):
                    print "character: " + character
                    global number_of_states 
                    number_of_states = number_of_states + 1
                    print "number of states", number_of_states
                    FSM[current_state][alphabet_num] = number_of_states
                    print "GGG", FSM[current_state][alphabet_num]
                    current_state = number_of_states
                else:
                    #if alphabet_num from the current state already leads to another state
                    #build from that state onwards. 
                    current_state = FSM[current_state][alphabet_num]
        print FSM[0]
       
        print "word is: ", word, "current state is: ", current_state
        output_function.insert(current_state, word)
        print output_function
    
    #for all character which do not have a transition from state 0
    #set the transtion to 0. 
    for alphabet in range(26):
        if(FSM[0][alphabet] == -1):
            FSM[0][alphabet] = 0
   
    print FSM
    return FSM
#def build_output_function():
    
    

def failure_function_construction(FSM):
    queue = deque()
    #All states with a depth of 1 is 0 in the failure function
    for alphabet in range(26):
        if(FSM[0][alphabet] != 0):
            index = FSM[0][alphabet]
            global failure
            failure.insert(index, 0)
            queue.append(index)
            
    current_state = queue.popleft()
    #While the queue does not become empty
    while(queue):
        for alphabet in range(26):
            if(FSM[current_state][alphabet] != -1):
                queue.append(FSM[current_state][alphabet])
                print FSM[current_state][alphabet]
                value = FSM[failure[current_state]][alphabet]
                #working out the failure fn of the transitions using alphabet that are successful
                
                failure[FSM[current_state][alphabet]] = value
                print queue
        current_state = queue.popleft()

    print failure

#uses go to and failure function. 
def go_to_next_state(current_state, character):  
    output = current_state
    while(FSM[current_state][character] == -1):
        current_state = failure[current_state]
        return FSM[current_state][character]
    
#sets up       
def broop(file_name):    
      #The file that needs to be checked
      file2 = open(file_name, "r")
      for line in file2:
          word_list = line.split(" ")          
          for word in word_list:
              current_state = 0 
              print "The word is", word
              word = word.rstrip()
              char_list = list(word)            
              for x in range(len(char_list)):
                  to_int_char = convert_alphaChar_to_int(char_list[x])  
                  current_state = go_to_next_state(current_state, to_int_char)
                  if(output_function[current_state] != 0):
                      print "keyword found:", output_function[current_state]
                  
                  
#methods converts alphabet to 0,...,25    
def convert_alphaChar_to_int(char):
    number = ord(char) - 97
    return number
   
FSM = build_FSM("test_go_to_fn")    
failure_function_construction(FSM)
broop("input_test_file_AC")


    
