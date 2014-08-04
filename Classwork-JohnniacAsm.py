instruction_list = []

def dump_code(instruction_list):
  for code_item in instruction_list:
    print(code_item)

def read_program(instruction_list):
  entry = input("? ").upper()
  while entry != "GO":
    (opcode, operand) = entry.split(" ")
    if opcode == "HALT":
      instruction = "00000"
    if opcode == "LOAD":
      instruction = "01" + operand
    if opcode == "STORE":
      instruction = "02" + operand
    if opcode == "ADD":
      instruction = "03" + operand
    if opcode == "MULTIPLY":
      instruction = "04" + operand
    if opcode == "DIVIDE":
      instruction = "05" + operand
    if opcode == "SUBTRACT":
      instruction = "06" + operand
    if opcode == "TEST":
      instruction = "07" + operand
    if opcode == "GET":
      instruction = "08" + operand
    if opcode == "PUT":
      instruction = "09" + operand
    if opcode == "NOOP":
      instruction = "10" + operand
    instruction_list.append(instruction)
    entry = input("? ").upper()

read_program(instruction_list)
dump_code(instruction_list)
