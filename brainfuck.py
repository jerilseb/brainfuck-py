#!/usr/bin/env python
from sys import argv

def brainfuck(src, input):

    tape_index = 0
    tape = [0]

    src_index = 0
    src_length = len(src)

    input_index = 0

    while src_index < src_length:

        character = src[src_index]

        if character == ">":
            tape_index += 1
            while len(tape) <= tape_index:
                tape.append(0)

        elif character == "<":
            if tape_index > 0:
                tape_index -= 1

        elif character == "+":
            tape[tape_index] += 1

        elif character == "-":
            tape[tape_index] -= 1

        elif character == ".":
            print chr(tape[tape_index]) + " (" + str(tape[tape_index]) + ")"

        elif character == ",":
            tape[tape_index] = ord(input[input_index])
            input_index += 1

        elif character == "[":
            if tape[tape_index] == 0:
                depth = 1
                while depth > 0:
                    src_index += 1
                    if src[src_index] == "[":
                        depth += 1
                    elif src[src_index] == "]":
                        depth -= 1

        elif character == "]":
            depth = 1
            while depth > 0:
                src_index -= 1
                if src[src_index] == "[":
                    depth -= 1
                elif src[src_index] == "]":
                    depth += 1
            src_index -= 1

        src_index += 1

    return tape

if __name__ == "__main__":

    filename = argv[1]
    input = argv[2]

    with open(filename) as file:
        src = file.read()
        tape = brainfuck(src, input)
        print tape
