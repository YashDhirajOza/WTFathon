class MasalaCodeInterpreter {
    constructor() {
        this.variables = {};
        this.functions = {};
        this.spiceLevel = 0;
    }

    run(code) {
        const lines = code.split('\n');
        let i = 0;
        while (i < lines.length) {
            let line = lines[i].trim();
            if (line.startsWith('Khao maa kasam')) {
                this.declareVariable(line);
            } else if (line.startsWith('ye lee')) {
                this.yeLee(line);
            } else if (line.startsWith('chai_pe_charcha')) {
                i = this.executeLoop(lines, i);
            } else if (line.startsWith('agar_toh_phir')) {
                i = this.executeConditional(lines, i);
            } else if (line.startsWith('agle_janam_mohe')) {
                i = this.defineFunction(lines, i);
            } else if (line.startsWith('chalta_hai')) {
                this.procrastinate();
            } else if (line.startsWith('masala_add_karo')) {
                this.addSpice();
            } else if (line.startsWith('thoda_aaram')) {
                this.takeNap();
            }
            i += 1;
        }
    }

    declareVariable(line) {
        const parts = line.split(' ');
        if (parts.length >= 4 && parts[2] === '=') {
            const varName = parts[3];
            const value = eval(parts.slice(4).join(' '));
            this.variables[varName] = value;
            this.playSound("path/to/maa_.mp3"); // Replace with the correct path
        }
    }

    yeLee(line) {
        const match = line.match(/ye lee\s*\((.*)\)/);
        if (match) {
            const message = eval(match[1]);
            console.log(message);
            this.playSound("path/to/meme1.mp3"); // Replace with the correct path
        }
    }

    executeLoop(lines, start) {
        const match = lines[start].match(/chai_pe_charcha\s*\((.*)\)/);
        const condition = match[1];
        let bodyStart = start + 1;
        let bodyEnd = bodyStart;
        while (bodyEnd < lines.length && !lines[bodyEnd].trim().startsWith('bas_ho_gaya')) {
            bodyEnd += 1;
        }
        while (eval(condition)) {
            this.run(lines.slice(bodyStart, bodyEnd).join('\n'));
        }
        return bodyEnd;
    }

    executeConditional(lines, start) {
        const match = lines[start].match(/agar_toh_phir\s*\((.*)\)/);
        const condition = match[1];
        let bodyStart = start + 1;
        let bodyEnd = bodyStart;
        while (bodyEnd < lines.length && !lines[bodyEnd].trim().startsWith('bas_ho_gaya')) {
            bodyEnd += 1;
        }
        if (eval(condition)) {
            this.run(lines.slice(bodyStart, bodyEnd).join('\n'));
        }
        return bodyEnd;
    }

    defineFunction(lines, start) {
        const match = lines[start].match(/agle_janam_mohe\s*(\w+)\s*\((.*)\)/);
        const funcName = match[1];
        const params = match[2].split(',').map(p => p.trim());
        let bodyStart = start + 1;
        let bodyEnd = bodyStart;
        while (bodyEnd < lines.length && !lines[bodyEnd].trim().startsWith('bas_ho_gaya')) {
            bodyEnd += 1;
        }
        this.functions[funcName] = { params, body: lines.slice(bodyStart, bodyEnd).join('\n') };
        return bodyEnd;
    }

    procrastinate() {
        const excuses = [
            "Kal karte hain, abhi thoda Netflix dekh loon...",
            "Pehle ek chai ho jaye, phir sochtein hain.",
            "Arrey, pados wali aunty ka gossip miss ho jayega!",
            "Mummy ne bulaya hai, baad mein karta hoon.",
            "Yaar, Cricket match chal raha hai. Work can wait!"
        ];
        console.log(Procrastinating: ${excuses[Math.floor(Math.random() * excuses.length)]});
        setTimeout(() => {}, 2000);
    }

    addSpice() {
        this.spiceLevel += 1;
        console.log(Masala level badhaya! Ab spice level hai: ${this.spiceLevel});
        if (this.spiceLevel > 5) {
            console.log("Mirchi kam karo! Code mein aag lag jayegi!");
        }
    }

    takeNap() {
        const napTime = Math.floor(Math.random() * 5) + 1;
        console.log(Thoda rest kar leta hoon... ${napTime} minute mein wapas aata hoon.);
        setTimeout(() => {
            console.log("Uth gaya! Ab kaam karte hain... ya phir ek aur nap?");
        }, napTime * 60000); // Converted minutes to milliseconds
    }

    playSound(filePath) {
        const audio = new Audio(filePath);
        audio.play();
    }
}

// Example usage
const interpreter = new MasalaCodeInterpreter();

const code = `
Khao maa kasam samosa = 5
ye lee("Kitne samose hain?")
chai_pe_charcha(samosa > 0)
    ye lee("Ek samosa khaya!")
    Khao maa kasam samosa = samosa - 1
    masala_add_karo()
bas_ho_gaya
ye lee("Samose khatam ho gaye!")
thoda_aaram()
`;

interpreter.run(code);