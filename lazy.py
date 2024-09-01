import sys
import re
import random
import time

class ProcrastiCodeInterpreter:
    def __init__(self):
        self.variables = {}
        self.functions = {}
        self.output = []
    
    def run(self, code):
        lines = code.split('\n')
        i = 0
        while i < len(lines):
            line = lines[i].strip()
            if line.startswith('maybe'):
                self.declare_variable(line)
            elif line.startswith('complain'):
                self.complain(line)
            elif line.startswith('eventually'):
                i = self.execute_loop(lines, i)
            elif line.startswith('whenever'):
                i = self.execute_conditional(lines, i)
            elif line.startswith('someday'):
                i = self.define_function(lines, i)
            elif line.startswith('procrastinate'):
                self.procrastinate()
            i += 1

    def declare_variable(self, line):
        parts = line.split()
        if len(parts) >= 4 and parts[2] == '=':
            var_name = parts[1]
            value = ' '.join(parts[3:])
            self.variables[var_name] = eval(value, {}, self.variables)

    def complain(self, line):
        message = re.match(r'complain\s*\((.*)\)', line).group(1)
        output_message = f"Ugh, fine. {eval(message, {}, self.variables)}"
        print(output_message)
        self.output.append(output_message)

    def execute_loop(self, lines, start):
        condition = re.match(r'eventually\s*\((.*)\)', lines[start]).group(1)
        body_start = start + 1
        body_end = body_start
        while body_end < len(lines) and not lines[body_end].strip().startswith('done'):
            body_end += 1
        while eval(condition, {}, self.variables):
            self.run('\n'.join(lines[body_start:body_end]))
        return body_end

    def execute_conditional(self, lines, start):
        condition = re.match(r'whenever\s*\((.*)\)', lines[start]).group(1)
        body_start = start + 1
        body_end = body_start
        while body_end < len(lines) and not lines[body_end].strip().startswith('done'):
            body_end += 1
        if eval(condition, {}, self.variables):
            self.run('\n'.join(lines[body_start:body_end]))
        return body_end

    def define_function(self, lines, start):
        func_def = re.match(r'someday\s*(\w+)\s*\((.*)\)', lines[start])
        func_name = func_def.group(1)
        params = [p.strip() for p in func_def.group(2).split(',')]
        body_start = start + 1
        body_end = body_start
        while body_end < len(lines) and not lines[body_end].strip().startswith('done'):
            body_end += 1
        self.functions[func_name] = (params, '\n'.join(lines[body_start:body_end]))
        return body_end

    def procrastinate(self):
        excuses = [
            "I'll do it in 5 minutes...",
            "But first, let me check my emails.",
            "I need a coffee break to think about this.",
            "I should reorganize my desk before starting.",
            "Let me just quickly check social media first."
        ]
        procrastination_message = f"Procrastinating: {random.choice(excuses)}"
        print(procrastination_message)
        self.output.append(procrastination_message)
        time.sleep(2)

    def save_output(self, filename):
        with open(f"{filename}.lazy", "w") as file:
            file.write('\n'.join(self.output))
        print(f"Output saved to {filename}.lazy")

def main():
    if len(sys.argv) != 3 or sys.argv[1] != "run":
        print("Usage: lazy run <filename>.lazy")
        sys.exit(1)

    filename = sys.argv[2]
    if not filename.endswith('.lazy'):
        print("Error: The file must have a .lazy extension.")
        sys.exit(1)

    try:
        with open(filename, 'r') as file:
            code = file.read()
    except FileNotFoundError:
        print(f"Error: File {filename} not found.")
        sys.exit(1)

    interpreter = ProcrastiCodeInterpreter()
    interpreter.run(code)
    interpreter.save_output(filename.split('.')[0])  # Save the output

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: lazy run <filename>.lazy")
        sys.exit(1)

    filename = sys.argv[1]
    if not filename.lower().endswith('.lazy'):
        print("Please provide a .lazy file.")
        sys.exit(1)

    try:
        with open(filename, 'r') as file:
            code = file.read()
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
        sys.exit(1)

    interpreter = ProcrastiCodeInterpreter()
    interpreter.run(code)