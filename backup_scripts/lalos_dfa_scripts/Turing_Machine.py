# Turing Machine
# Jose Eduardo Flores Rodriguez
# Computer Theory
# MCBICI
# Professor: Dr.Israel Roman Godinez
# 02.11.2023

import re

# Regular expressions
sigma_er = "sigma={[\w\, ]*}|sigma={\w}"
q_er = "Q={[q\d\, ]*}|Q={q\d}"
f_er = "f={[(q\d \d)->(q\d \w \w)]*}"
q0_er = "q0=q\d"
b_er = "b=\w|_"
element_symbol_er = "(q\d \w)"
trans_er = "q\d"
F_er = "F={[q\d\,]*}|F={q\d}"
test_er = "test={[(\w)*\, ]*}"
expected = []
my_dict = {}


# Functions to find the Turing Machine tuple elements
def openfile():
    # Text file lecture
    archivo = open("./automataDef.txt")
    lines = archivo.read()
    return lines


def find_states(lines):
    # Find Q
    comp = re.compile(q_er)
    find_q = comp.findall(lines)
    q = ''.join(find_q)
    return q


def find_sigmas(lines):
    # Find Sigma
    comp = re.compile(sigma_er)
    find_sigma = comp.findall(lines)
    sigma = ''.join(find_sigma)
    return sigma


def find_initial_st(lines):
    # Find q0
    comp = re.compile(q0_er)
    find_q0 = comp.findall(lines)
    q0 = ''.join(find_q0)
    return q0


def find_final_st(lines):
    # Find final states
    comp = re.compile(F_er)
    find_final = comp.findall(lines)
    final = ''.join(find_final)
    return final


def find_trans_funct(lines):
    # Find f
    comp = re.compile(f_er)
    find_f = comp.findall(lines)
    f = ''.join(find_f)
    return f


def find_test_list(lines):
    # Find test set
    comp = re.compile(test_er)
    find_test = comp.findall(lines)
    test = ''.join(find_test)
    return test


# Open file and obtain striped and split listed forms of every set of data of the tuple
file = openfile()
states = find_states(file)
q1 = find_states(states).split("=")
q2 = q1[1].strip("{}")
q3 = q2.split(",")

sigma = find_sigmas(file)
sigma1 = sigma.split("=")
sigma2 = sigma1[1].strip("{}")
sigma3 = sigma2.split(",")

print("")
print("Initial and Final states validation")
print("")
initial_st = find_initial_st(file)
list_q = states.split("=")
list_q0 = initial_st.split("=")
# If q0 does not belong to set of states print warning
if list_q0[1] in list_q[1]:
    print("Initial state in set of states")
elif list_q0[1] not in list_q[1]:
    print("(WARNING!!) Initial state is not in the set of states, please correct")

final_st = find_final_st(file)
list_F = final_st.split("=")
list_Fs = list_F[1].strip("{}")
# If final states do not belong to set of states print warning
if list_Fs in list_q[1]:
    print("Final state(s) in set of states")
elif list_Fs not in list_q[1]:
    print("(WARNING!!) Final state(s) not in the set of states, please correct")

trans_funct = find_trans_funct(file)
list_f = trans_funct.split("=")
list_f2 = list_f[1].strip("{}")
list_f3 = list_f2.split(",")
list_f4 = []
for element in list_f3:
    el_split = element.split("->")
    list_f4.append(el_split)
print(list_f4)

test_list = find_test_list(file)
test2 = test_list.split("=")
test3 = test2[1].strip("{}")
test4 = test3.split(",")

# Every item of the tuple printed in format
print("------------------------------------------------------------------------------------------")
print("Automaton Tuple Elements")
print("")
print(states)
print(sigma)
print(initial_st)
print(final_st)
print(list_f4)
print(test_list)
print("-------------------------------------------------------------------------------------------")


def turing_machine(initial_state, acc_sts, transitions, tape):
    current_state = initial_state  # Define our initial state as the current one

    while current_state == acc_sts:
        for transition in transitions:
            for letter in tape:
                current_sym = letter
                # q1  1 = (q1 1)
                if (current_state, current_sym) not in transition:
                    return 'Rejected'  # Reject test string if state and symbol do not have a defined transition in function

                # Define the value assigned to each key as the new state and symbol, and the direction to go
                new_st, new_sym, mov = transitions[(current_state, current_sym)]
                current_state = new_st

            if current_state in acc_sts:  # If current state in acceptance states validate test string as correct
                return 'Accepted'


# Uso de la función
for element in test4[1]:
    test_list_val = turing_machine(list_q0, list_Fs, list_f4, element)
    print(test_list_val)

print("")
print("Test list elements validation")
print("Expected = ", expected)
"""
import re

# Regular expressions
sigma_er = "sigma={[\w\, ]*}|sigma={\w}"
q_er = "Q={[q\d\, ]*}|Q={q\d}"
f_er = "f={[(q\d \d)->(q\d \w \w)]*}"
q0_er = "q0=q\d"
F_er = "F={[q\d\,]*}|F={q\d}"
test_er = "test={[(\w)*\, ]*}"
element_symbol_er = "(q\d \w)"
expected = []
my_dict = {}


# Functions to find the Turing Machine tuple elements
def openfile():
    # Text file lecture
    archivo = open("automata_correct2.txt")
    lines = archivo.read()
    print(lines)
    return lines


def find_states(lines):
    # Find Q
    comp = re.compile(q_er)
    find_q = comp.findall(lines)
    q = ''.join(find_q)
    return q


def find_sigmas(lines):
    # Find Sigma
    comp = re.compile(sigma_er)
    find_sigma = comp.findall(lines)
    sigma = ''.join(find_sigma)
    return sigma


def find_initial_st(lines):
    # Find q0
    comp = re.compile(q0_er)
    find_q0 = comp.findall(lines)
    q0 = ''.join(find_q0)
    return q0


def find_final_st(lines):
    # Find final states
    comp = re.compile(F_er)
    find_final = comp.findall(lines)
    final = ''.join(find_final)
    return final


def find_trans_funct(lines):
    # Find f
    comp = re.compile(f_er)
    find_f = comp.findall(lines)
    f = ''.join(find_f)
    return f


def find_test_list(lines):
    # Find test set
    comp = re.compile(test_er)
    find_test = comp.findall(lines)
    test = ''.join(find_test)
    return test


# Open file and obtain striped and split listed forms of every set of data of the tuple
file = openfile()

states = find_states(file)
q1 = find_states(states).split("=")
q2 = q1[1].strip("{}")
q3 = q2.split(",")

in_states = find_initial_st(file)
q0 = find_initial_st(in_states).split("=")
q00 = q0[1]

f_state = find_final_st(file)
F = find_states(states).split("=")
F1 = q1[1].strip("{}")
F2 = q2.split(",")

sigma = find_sigmas(file)
sigma1 = sigma.split("=")
sigma2 = sigma1[1].strip("{}")
sigma3 = sigma2.split(",")

trans_funct = find_trans_funct(file)
list_f = trans_funct.split("=")
list_f2 = list_f[1].strip("{}")
list_f3 = list_f2.split(",")
list_f4 = []
for element in list_f3:
    sep_element = element.split("(")
    sep_element2 = sep_element[1].split(")->")
    list_f4.append(sep_element2)

test_list = find_test_list(file)
test2 = test_list.split("=")
test3 = test2[1].strip("[]")
test4 = test3.split(",")

# Every item of the tuple printed in format
print("------------------------------------------------------------------------------------------")
print("Automaton Tuple Elements")
print("")
print(states)
print(sigma)
print(list_f4)
print(in_states)
print(f_state)
print(test_list)
print("-------------------------------------------------------------------------------------------")


# Implementación de la evaluación de las cadenas
def evaluar_cadenas(list_f4, test4):
    for x in test4:
        current_st = q00
        for symbol in x:
            if (current_st, symbol) in list_f4:
                current_st = list_f3[(current_st, symbol)]
            else:
                expected.append('Rejected')
                break
        else:
            expected.append('Accepted' if current_st in list_f3 else 'Rejected')

    return expected


# Uso de la función
for element in test4[1]:
    test_list_val = evaluar_cadenas(list_f4, test4[1])
    print(test_list_val)

print("")
print("Test list elements validation")
print("Expected = ", expected) """