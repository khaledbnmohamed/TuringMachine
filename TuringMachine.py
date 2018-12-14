from collections import Counter



dict = {}
input_tape=""
Next_transition_state=-1
found_transition_function="null" 
Final_Decision="Refused"

def Store_elements(type,value1,value2):


	if(type==alphabets):
		return int(int(value1)*int(value2))

	if type =='transitions':
		result = [x.strip() for x in value1.split(',')]
		dict[result[0]+result[1]]=result[2]+result[3]+result[4]



def TM(input_tape,Next_transition_state,position_of_head):

 
	while(position_of_head !=-5 ):
		Next_transition_state = SearchForTransition(position_of_head,Next_transition_state,input_tape) #will give the next transition to implemnt
		# print("in TM Next_transition_state is",Next_transition_state)
		# print("in TM input_tape[position_of_head] is",input_tape[position_of_head])
		# print("in TM found_transition_function[1][found_transition_function[1]] is",found_transition_function[1])

		input_tape[position_of_head]=found_transition_function[1]
		print(input_tape)
		print("in TM found_transition_function[2] is",found_transition_function[2])
		position_of_head=MoveHeadPoisiton(found_transition_function[2],position_of_head,input_tape)
	
	return input_tape

def MoveHeadPoisiton(character,position_of_head,input_tape):
	
	global Final_Decision 


	Accepted=False
	if(character=='y'):
		Accepted=True
		if(input_tape[position_of_head]=='#'):
			if(Accepted):
				print("INTERNALLY Accepted")
				Final_Decision="Accepted"
			return -5 #Done"	



	if(character=='n'):
		Accepted=False
		if(input_tape[position_of_head]=='#'):
			if(Accepted):

				print("INTERNALLY Accepted")
				Final_Decision="Accepted"
			return -5 #Done"	

	if(character=='r'):
		if(input_tape[position_of_head]=='#'):
			if(Accepted):
				print("INTERNALLY Accepted")
				Final_Decision="Accepted"
			return -5 #Done"
		else:
			return position_of_head+1
	elif(character=='l'):
		if(input_tape[position_of_head-1]=='<'):
			if(Accepted):

				print("INTERNALLY Accepted")
				Final_Decision="Accepted"
			return -5 #Done"
		else:
			return position_of_head-1



def SearchForTransition(position_of_head,current_state,input_tape):
	count=0
	global found_transition_function
	key= ( str(current_state) +input_tape[position_of_head]) 
	print("Key is",key)
	if key in dict:
		found_transition_function=dict.get(key)
		print ("Value is",found_transition_function)
		print ("Value number is",found_transition_function[0])

		Next_transition_state=found_transition_function[0]
		print("DONE",++count)
		print ("Next_transition_state is",Next_transition_state)

		return Next_transition_state




# def Implement(Next_transition_state):
# 	stringtokeinzer with ,


try:
	number_of_states = int(input("Enter number_of_states "))
except ValueError:
 print("Numbers only")	

print ("number_of_states", number_of_states)
alphabets = input("Enter number_of_alphabets seprated by commas ")

if('<' in alphabets):
	number_of_alphabets = len(''.join(alphabets.split(',')))-1

else:
	number_of_alphabets = len(''.join(alphabets.split(',')))
print (number_of_alphabets ,'number_of_alphabets')
transition_number=Store_elements(alphabets,number_of_states,number_of_alphabets)
print(transition_number)


for x in range(transition_number): 
	number_of_transitions = input("Enter transition function seprated by commas ") #(Current state,input symbol!!!!next state,new character,decision)
	Store_elements('transitions',number_of_transitions,0)

input_tape = list(input("Enter tape "))
input_tape.append('#')
print(input_tape)
position_of_head = 1

print(TM(input_tape,0,position_of_head))

print(Final_Decision)

# print(dict)
