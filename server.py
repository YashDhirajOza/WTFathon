from flask import Flask, request, jsonify
from flask_cors import CORS
import re
import random
import time
import os

app = Flask(__name__)
CORS(app)

class ProcrastiCodeInterpreter:
    def __init__(self):
        self.variables = {}
        self.functions = {}
        self.output = []

    def run(self, code):
        self.output = []
        lines = code.split('\n')
        i = 0
        while i < len(lines):
            line = lines[i].strip()
            if line.startswith('Khao maa kasam'):
                self.declare_variable(line)
            elif line.startswith('ye lee'):
                self.ye_lee(line)
            elif line.startswith('eventually'):
                i = self.execute_loop(lines, i)
            elif line.startswith('whenever'):
                i = self.execute_conditional(lines, i)
            elif line.startswith('someday'):
                i = self.define_function(lines, i)
            elif line.startswith('procrastinate'):
                self.procrastinate()
            i += 1
        return "\n".join(self.output)

    def declare_variable(self, line):
        parts = line.split()
        if len(parts) >= 4 and parts[2] == '=':
            var_name = parts[3]
            value = ' '.join(parts[4:])
            self.variables[var_name] = eval(value, {}, self.variables)
            
            # Simulate audio playback
            self.output.append("*Playing sound: maa_.mp3*")
            self.output.append(f"Variable {var_name} declared with value {self.variables[var_name]}")

    def ye_lee(self, line):
        message = re.match(r'ye lee\s*\((.*)\)', line).group(1)
        result = str(eval(message, {}, self.variables))
        self.output.append(result)
        
        # Simulate audio playback
        self.output.append("*Playing sound: meme1.mp3*")

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
        result = f"Procrastinating: {random.choice(excuses)}"
        self.output.append(result)
        time.sleep(2)

interpreter = ProcrastiCodeInterpreter()

@app.route('/run_code', methods=['POST'])
def run_code():
    code = request.json.get('code', '')
    result = interpreter.run(code)
    return jsonify({'result': result})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)