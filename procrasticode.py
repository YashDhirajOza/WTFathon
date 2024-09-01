import re
import random
import time
from playsound import playsound

class MasalaCodeInterpreter:
    def __init__(self):
        self.variables = {}
        self.functions = {}
        self.spice_level = 0

    def run(self, code):
        lines = code.split('\n')
        i = 0
        while i < len(lines):
            line = lines[i].strip()
            if line.startswith('Khao maa kasam'):
                self.declare_variable(line)
            elif line.startswith('ye lee'):
                self.ye_lee(line)
            elif line.startswith('chai_pe_charcha'):
                i = self.execute_loop(lines, i)
            elif line.startswith('agar_toh_phir'):
                i = self.execute_conditional(lines, i)
            elif line.startswith('agle_janam_mohe'):
                i = self.define_function(lines, i)
            elif line.startswith('chalta_hai'):
                self.procrastinate()
            elif line.startswith('masala_add_karo'):
                self.add_spice()
            elif line.startswith('thoda_aaram'):
                self.take_nap()
            i += 1

    def declare_variable(self, line):
        parts = line.split()
        if len(parts) >= 4 and parts[2] == '=':
            var_name = parts[3]
            value = ' '.join(parts[4:])
            self.variables[var_name] = eval(value, {}, self.variables)
            playsound(r"D:\WTF\maa_.mp3")

    def ye_lee(self, line):
        message = re.match(r'ye lee\s*\((.*)\)', line).group(1)
        print(eval(message, {}, self.variables))
        playsound(r"D:\WTF\meme1.mp3")

    def execute_loop(self, lines, start):
        condition = re.match(r'chai_pe_charcha\s*\((.*)\)', lines[start]).group(1)
        body_start = start + 1
        body_end = body_start
        while body_end < len(lines) and not lines[body_end].strip().startswith('bas_ho_gaya'):
            body_end += 1
        while eval(condition, {}, self.variables):
            self.run('\n'.join(lines[body_start:body_end]))
        return body_end

    def execute_conditional(self, lines, start):
        condition = re.match(r'agar_toh_phir\s*\((.*)\)', lines[start]).group(1)
        body_start = start + 1
        body_end = body_start
        while body_end < len(lines) and not lines[body_end].strip().startswith('bas_ho_gaya'):
            body_end += 1
        if eval(condition, {}, self.variables):
            self.run('\n'.join(lines[body_start:body_end]))
        return body_end

    def define_function(self, lines, start):
        func_def = re.match(r'agle_janam_mohe\s*(\w+)\s*\((.*)\)', lines[start])
        func_name = func_def.group(1)
        params = [p.strip() for p in func_def.group(2).split(',')]
        body_start = start + 1
        body_end = body_start
        while body_end < len(lines) and not lines[body_end].strip().startswith('bas_ho_gaya'):
            body_end += 1
        self.functions[func_name] = (params, '\n'.join(lines[body_start:body_end]))
        return body_end

    def procrastinate(self):
        excuses = [
            "Kal karte hain, abhi thoda Netflix dekh loon...",
            "Pehle ek chai ho jaye, phir sochtein hain.",
            "Arrey, pados wali aunty ka gossip miss ho jayega!",
            "Mummy ne bulaya hai, baad mein karta hoon.",
            "Yaar, Cricket match chal raha hai. Work can wait!"
        ]
        print(f"Procrastinating: {random.choice(excuses)}")
        time.sleep(2)

    def add_spice(self):
        self.spice_level += 1
        print(f"Masala level badhaya! Ab spice level hai: {self.spice_level}")
        if self.spice_level > 5:
            print("Mirchi kam karo! Code mein aag lag jayegi!")

    def take_nap(self):
        nap_time = random.randint(1, 5)
        print(f"Thoda rest kar leta hoon... {nap_time} minute mein wapas aata hoon.")
        time.sleep(nap_time)
        print("Uth gaya! Ab kaam karte hain... ya phir ek aur nap?")

# Example usage
interpreter = MasalaCodeInterpreter()

code = """
Khao maa kasam samosa = 5
ye lee("Kitne samose hain?")
chai_pe_charcha(samosa > 0)
    ye lee("Ek samosa khaya!")
    Khao maa kasam samosa = samosa - 1
    masala_add_karo()
bas_ho_gaya
ye lee("Samose khatam ho gaye!")
thoda_aaram()
"""

interpreter.run(code)