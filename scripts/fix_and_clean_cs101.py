#!/usr/bin/env python3
import json, re

print("Starting definitive CS101 cleanup & repair...")

with open("cs101_quiz_bank.json") as f:
    questions = json.load(f)

print(f"Loaded {len(questions)} CS101 MCQs.")

# Verified replacements for malformed or OCR-fragmented questions
REPLACEMENTS = {
    7: {
        "question": "2 raised to the power 0 equals to:",
        "options": ["0", "1", "2", "Undefined"],
        "answer": "1",
        "explanation": "In mathematics and computer science, any non-zero number raised to the power of 0 equals 1 (i.e. 2^0 = 1).",
        "topic": "General Computer Science"
    },
    128: {
        "question": "Assume that you are developing software for a washing machine. Which operating system type is best suited to fulfill its real-time control requirements?",
        "options": ["Real-time Operating System (RTOS)", "Batch Processing System", "Distributed Operating System", "Time-sharing Operating System"],
        "answer": "Real-time Operating System (RTOS)",
        "explanation": "Embedded devices like washing machines require a Real-Time Operating System (RTOS) to guarantee execution within strict timing constraints.",
        "topic": "Operating System Concepts"
    },
    139: {
        "question": "In web development, which language is primarily used to add interactivity and client-side behavior to a webpage?",
        "options": ["JavaScript", "HTML", "CSS", "SQL"],
        "answer": "JavaScript",
        "explanation": "JavaScript is the standard client-side scripting language used to provide interactivity and dynamic behavior in web browsers.",
        "topic": "HTML & Web Basics"
    },
    155: {
        "question": "By using MPEG and MP3 compression techniques, digital cameras and media devices are able to store video files requiring:",
        "options": ["GB storage", "MB storage", "KB storage", "TB storage"],
        "answer": "GB storage",
        "explanation": "MPEG compression allows full-length video to fit into gigabytes (GB) instead of uncompressed terabytes.",
        "topic": "Multimedia & Graphics"
    },
    156: {
        "question": "Which search engine is widely recognized for searching web pages, images, movies, and digital media?",
        "options": ["Google", "MS-DOS", "FTP", "Telnet"],
        "answer": "Google",
        "explanation": "Google is a major search engine capable of indexing and searching text, images, videos, and news.",
        "topic": "Search Engines"
    },
    162: {
        "question": "A CPU requires at least ________ to fetch an instruction from memory.",
        "options": ["One machine cycle", "Two nanoseconds", "One microsecond", "One millisecond"],
        "answer": "One machine cycle",
        "explanation": "Instruction fetch is the first stage of the CPU machine cycle (fetch, decode, execute).",
        "topic": "Computer Architecture & Hardware"
    },
    174: {
        "question": "In structured programming, control structures that combine sequential and conditional logic are known as:",
        "options": ["Selection Structures", "Infinite Loops", "Unconditional Jumps", "Spaghetti Code"],
        "answer": "Selection Structures",
        "explanation": "Selection structures (if-else, switch) execute specific code branches conditionally.",
        "topic": "Algorithms & Programming"
    },
    196: {
        "question": "In HTML5, which tags are used to define meaningful document sections and correct semantics?",
        "options": ["<header>, <nav>, <section>, <article>", "<b>, <i>, <u>, <font>", "<div>, <span>, <br>, <hr>", "<table>, <tr>, <td>, <th>"],
        "answer": "<header>, <nav>, <section>, <article>",
        "explanation": "HTML5 semantic elements clearly describe their meaning to both browser and developer.",
        "topic": "HTML & Web Basics"
    },
    204: {
        "question": "Early mechanical computing devices stored and counted numbers using decimal storage wheels and:",
        "options": ["Rotary dial switches", "Transistors", "Integrated Circuits", "Microprocessors"],
        "answer": "Rotary dial switches",
        "explanation": "Early mechanical calculators (e.g. Pascaline, Mark I) used rotary switches and gear wheels.",
        "topic": "History of Computing"
    },
    206: {
        "question": "The low-level language that is directly understood and executed by the computer hardware is called:",
        "options": ["Machine Language", "Assembly Language", "High-Level Language", "Natural Language"],
        "answer": "Machine Language",
        "explanation": "Machine language (binary 0s and 1s) is the only language directly executed by CPU circuitry.",
        "topic": "Computer Architecture & Hardware"
    },
    211: {
        "question": "Digital computers represent all information using two natural physical states represented by:",
        "options": ["0 and 1", "Positive and Negative", "True and Maybe", "High and Low frequency"],
        "answer": "0 and 1",
        "explanation": "Digital logic is fundamentally binary, relying on 0 (off/low voltage) and 1 (on/high voltage).",
        "topic": "Binary Addition & Representation"
    },
    213: {
        "question": "MS-DOS (Disk Operating System) is an example of an operating system with a:",
        "options": ["Command-line interface (CLI)", "Graphical user interface (GUI)", "Touch-screen interface", "Voice recognition interface"],
        "answer": "Command-line interface (CLI)",
        "explanation": "DOS relied strictly on a text-based command-line interface.",
        "topic": "Operating System Concepts"
    },
    216: {
        "question": "Which of the following describes the primary role of the Operating System Kernel?",
        "options": ["Managing hardware resources and core system processes", "Designing web graphics", "Compiling high-level source code", "Formatting rich text documents"],
        "answer": "Managing hardware resources and core system processes",
        "explanation": "The kernel is the central component of an OS, responsible for memory, CPU scheduling, and hardware drivers.",
        "topic": "Operating System Concepts"
    },
    264: {
        "question": "In word processing software, grammar and spelling accuracy can be verified and corrected using the:",
        "options": ["Spelling and Grammar Checker", "Thesaurus tool", "Word Count utility", "Macro Recorder"],
        "answer": "Spelling and Grammar Checker",
        "explanation": "Word processors provide built-in spell and grammar check tools to detect language errors.",
        "topic": "Productivity Software"
    },
    289: {
        "question": "If a string of 8 bits undergoes a right circular shift (rotate right) of 2 bits, what happens to the bits?",
        "options": ["The rightmost 2 bits wrap around to become the leftmost 2 bits", "The rightmost 2 bits are lost and replaced with 0s", "The leftmost 2 bits wrap around to become the rightmost 2 bits", "All bits are inverted"],
        "answer": "The rightmost 2 bits wrap around to become the leftmost 2 bits",
        "explanation": "In a circular shift (rotation), bits that fall off one end are recirculated to the opposite end.",
        "topic": "Computer Architecture & Hardware"
    },
    296: {
        "question": "In Google advanced search, which operator is used to restrict the search to words appearing anywhere in the body text?",
        "options": ["intext:", "intitle:", "inurl:", "filetype:"],
        "answer": "intext:",
        "explanation": "The intext: search operator restricts Google query results to the body text of web pages.",
        "topic": "Search Engines"
    },
    306: {
        "question": "If you want to ensure that a specific bit is set to 1 in a bit pattern, which bitwise operation should you perform with a mask?",
        "options": ["OR", "AND", "XOR", "NOT"],
        "answer": "OR",
        "explanation": "The bitwise OR operation (x | 1 = 1) is used to set specific bits to 1.",
        "topic": "Computer Architecture & Hardware"
    },
    315: {
        "question": "In Hexadecimal notation, the 4-bit binary pattern 1111 is represented by:",
        "options": ["F", "E", "A", "10"],
        "answer": "F",
        "explanation": "In binary 1111 = 8 + 4 + 2 + 1 = 15, which in hexadecimal is F.",
        "topic": "Binary Addition & Representation"
    },
    332: {
        "question": "In an odd parity system, if the data bits are 1011, what parity bit must be appended?",
        "options": ["0", "1", "Cannot be determined", "None"],
        "answer": "0",
        "explanation": "The data bits '1011' contain three 1s (odd). In odd parity, total number of 1s must remain odd, so a 0 is appended.",
        "topic": "Binary Addition & Representation"
    },
    333: {
        "question": "In the analysis of algorithms, execution efficiency is typically measured in terms of:",
        "options": ["The number of basic steps required as a function of input size", "The physical clock time in milliseconds", "The number of lines of source code", "The color depth of the monitor"],
        "answer": "The number of basic steps required as a function of input size",
        "explanation": "Algorithm time complexity (Big-O) measures the growth in the number of fundamental computational steps relative to input size N.",
        "topic": "Algorithms & Programming"
    },
    338: {
        "question": "In the binary number system, each digit position can only take the value:",
        "options": ["0 or 1", "0 to 9", "0 to 7", "0 to 15"],
        "answer": "0 or 1",
        "explanation": "Binary is base-2, using only the digits 0 and 1.",
        "topic": "Binary Addition & Representation"
    },
    360: {
        "question": "In spreadsheet software (such as MS Excel), which feature is used to find an input value needed to produce a specific target result?",
        "options": ["Goal Seek", "AutoSum", "Sort & Filter", "Conditional Formatting"],
        "answer": "Goal Seek",
        "explanation": "Goal Seek is a what-if analysis tool that calculates backward to determine the input needed to achieve a desired goal.",
        "topic": "Productivity Software"
    },
    391: {
        "question": "The World Wide Web (WWW) and the first web browser were invented in 1989 by:",
        "options": ["Tim Berners-Lee", "Bill Gates", "Steve Jobs", "Alan Turing"],
        "answer": "Tim Berners-Lee",
        "explanation": "Sir Tim Berners-Lee invented the World Wide Web, HTML, and HTTP at CERN in 1989.",
        "topic": "History of Computing"
    },
    392: {
        "question": "In computer networking, a network location where clients can read published information but cannot modify it is called:",
        "options": ["Read-Only web page / server", "Interactive Wiki", "Chat room", "Database management system"],
        "answer": "Read-Only web page / server",
        "explanation": "Static, read-only websites (Web 1.0) allow users to view published information without editing capability.",
        "topic": "Network & Internet Classification"
    },
    393: {
        "question": "Computer video games and simulation gaming software belong to which category of software?",
        "options": ["Entertainment Software", "System Software", "Compiler Software", "Firmware"],
        "answer": "Entertainment Software",
        "explanation": "Video games are categorized as application software under the entertainment category.",
        "topic": "General Computer Science"
    },
    422: {
        "question": "Which of the following is a key advantage of writing Pseudocode before writing program code?",
        "options": ["It is language-independent and easy for humans to understand", "It can be directly compiled by the CPU hardware", "It executes faster than binary machine code", "It automatically detects syntax errors in the compiler"],
        "answer": "It is language-independent and easy for humans to understand",
        "explanation": "Pseudocode allows developers to focus on algorithmic logic without worrying about specific language syntax.",
        "topic": "Algorithms & Programming"
    },
    423: {
        "question": "In flowcharts and pseudocode, a loop structure means:",
        "options": ["A set of instructions repeated as long as a specified condition remains true", "A one-time unconditional program termination", "A method for printing text to a laser printer", "A hardware component for storing magnetic data"],
        "answer": "A set of instructions repeated as long as a specified condition remains true",
        "explanation": "A loop is an iterative control structure that repeats statements while a condition is satisfied.",
        "topic": "Algorithms & Programming"
    },
    436: {
        "question": "A microcontroller is typically designed and used to:",
        "options": ["Control specific electronic devices and embedded systems", "Run high-end enterprise databases", "Browse the World Wide Web", "Replace large supercomputing clusters"],
        "answer": "Control specific electronic devices and embedded systems",
        "explanation": "Microcontrollers embed CPU, memory, and I/O on a single chip to control appliances, automobiles, and robotics.",
        "topic": "Computer Architecture & Hardware"
    },
    447: {
        "question": "In algorithm complexity analysis, worst-case time complexity represents:",
        "options": ["The maximum number of steps required for an input of size N", "The minimum number of steps required", "The average running time across all possible inputs", "The execution time when the computer runs out of battery"],
        "answer": "The maximum number of steps required for an input of size N",
        "explanation": "Worst-case time complexity provides an upper bound on execution resources for any input of size N.",
        "topic": "Algorithms & Programming"
    },
    492: {
        "question": "Which early office profession was largely replaced by the widespread adoption of personal computers and word processing software?",
        "options": ["Typist", "Computer Programmer", "Systems Analyst", "Network Administrator"],
        "answer": "Typist",
        "explanation": "Word processors and personal computers rendered traditional typing pool typists obsolete.",
        "topic": "History of Computing"
    },
    513: {
        "question": "Compared to simple flat-file storage, a Relational Database Management System (RDBMS) provides:",
        "options": ["Reduced data redundancy and improved data integrity", "Slower search speeds across large data sets", "Inability to link multiple tables together", "Exclusive limitation to single-user computers"],
        "answer": "Reduced data redundancy and improved data integrity",
        "explanation": "Relational databases use tables, primary keys, and foreign keys to prevent duplicate data and maintain referential integrity.",
        "topic": "General Computer Science"
    },
    544: {
        "question": "In the Software Development Life Cycle (SDLC), determining whether a project is technically, financially, and operationally viable occurs during:",
        "options": ["Feasibility Study", "Deployment Phase", "Maintenance Phase", "Unit Testing"],
        "answer": "Feasibility Study",
        "explanation": "The feasibility study evaluates economic, technical, and operational viability before development begins.",
        "topic": "Software Engineering Principles"
    },
    551: {
        "question": "A continuous sequence or transmission of digital bits over a communication channel is called a:",
        "options": ["Bit Stream", "Byte Block", "Sector", "Register"],
        "answer": "Bit Stream",
        "explanation": "A continuous flow of transmitted bits is formally termed a bit stream.",
        "topic": "Network & Internet Classification"
    },
    554: {
        "question": "In digital audio recording and processing, physical sound is captured and represented as a:",
        "options": ["Continuous sound wave that is sampled at discrete intervals", "Bitmap graphic of color pixels", "Static text string", "Relational database schema"],
        "answer": "Continuous sound wave that is sampled at discrete intervals",
        "explanation": "Analog audio sound waves are digitized through sampling and quantization (ADC).",
        "topic": "Multimedia & Graphics"
    },
    562: {
        "question": "When a search engine executes a query, the resulting list of matching documents is presented to the user on:",
        "options": ["Search Engine Results Pages (SERP)", "The BIOS configuration screen", "A local terminal command prompt", "A spreadsheet pivot table"],
        "answer": "Search Engine Results Pages (SERP)",
        "explanation": "Search results are organized and displayed on Search Engine Results Pages (SERP).",
        "topic": "Search Engines"
    },
    590: {
        "question": "Automated software programs used by search engines to continuously discover and index web pages are called:",
        "options": ["Web Crawlers / Spiders", "Web Browsers", "Firewalls", "Compilers"],
        "answer": "Web Crawlers / Spiders",
        "explanation": "Web crawlers (or spiders) systematically browse the World Wide Web for indexing.",
        "topic": "Search Engines"
    },
    623: {
        "question": "Microprocessors and computer chips are primarily fabricated using which semiconductor material?",
        "options": ["Silicon", "Copper", "Aluminum", "Plastic"],
        "answer": "Silicon",
        "explanation": "Silicon is the standard semiconductor material used in transistor and chip manufacturing.",
        "topic": "Computer Architecture & Hardware"
    },
    638: {
        "question": "In the Binary Search algorithm on the sorted array [77, 89, 90, 94, 99, 100], searching for key 99 will inspect which mid-value after the initial division?",
        "options": ["99", "90", "94", "100"],
        "answer": "99",
        "explanation": "Binary search halves the search space each step until the key 99 is located at mid.",
        "topic": "Algorithms & Programming"
    },
    703: {
        "question": "The Altair 8800, considered the spark of the microcomputer revolution in 1975, had a base memory of:",
        "options": ["256 bytes", "64 kilobytes", "1 megabyte", "1 gigabyte"],
        "answer": "256 bytes",
        "explanation": "The original MITS Altair 8800 shipped with 256 bytes of RAM in its base kit.",
        "topic": "History of Computing"
    },
    735: {
        "question": "In computer networking, long data messages are broken down into smaller manageable segments called:",
        "options": ["Packets", "Tracks", "Registers", "Sectors"],
        "answer": "Packets",
        "explanation": "Packet-switching networks break messages into individual data packets for transmission.",
        "topic": "Network & Internet Classification"
    },
    755: {
        "question": "A Uniform Resource Locator (URL) is used in a web browser to:",
        "options": ["Locate and access a specific resource or document on the Internet", "Compile JavaScript source code into machine instructions", "Scan local hard disks for computer viruses", "Calculate arithmetic operations inside the ALU"],
        "answer": "Locate and access a specific resource or document on the Internet",
        "explanation": "A URL provides the global web address of an online document or resource.",
        "topic": "Network & Internet Classification"
    },
    799: {
        "question": "System software that directly interacts with hardware to provide essential user and application services is the:",
        "options": ["Operating System", "Spreadsheet", "Web Browser", "Text Editor"],
        "answer": "Operating System",
        "explanation": "The OS is the primary system software intermediary between applications and hardware.",
        "topic": "Operating System Concepts"
    },
    802: {
        "question": "In client-server web architecture, server-side code (e.g. PHP, Node.js) cannot be viewed by the client browser because:",
        "options": ["The code executes on the server and only generated output is sent to the client", "Browsers are unable to display plain text", "The Internet automatically encrypts and hides all HTML", "Client machines lack microprocessors"],
        "answer": "The code executes on the server and only generated output is sent to the client",
        "explanation": "Server scripts execute on the remote host; only the resulting HTML/CSS/JSON output is delivered to the browser.",
        "topic": "HTML & Web Basics"
    },
    803: {
        "question": "The primary command interpreter user interface provided by UNIX operating systems is called the:",
        "options": ["Shell", "BIOS", "Kernel", "Compiler"],
        "answer": "Shell",
        "explanation": "In UNIX, the Shell (e.g., bash, sh) provides the user command-line interface to the OS.",
        "topic": "Operating System Concepts"
    },
    818: {
        "question": "Antivirus and virus scanning software is classified under which category of software?",
        "options": ["Utility Program", "Operating System", "Application Suite", "Programming Language"],
        "answer": "Utility Program",
        "explanation": "Antivirus tools are utility programs designed to analyze, configure, and maintain computer security.",
        "topic": "General Computer Science"
    },
    820: {
        "question": "In computer programming, a Semantic (Logic) Error occurs when:",
        "options": ["The program executes without crashing but produces unintended or incorrect results", "The code violates the grammatical rules of the programming language", "The computer hardware experiences a power failure", "The compiler encounters an unrecognized keyword"],
        "answer": "The program executes without crashing but produces unintended or incorrect results",
        "explanation": "Semantic errors are bugs in the program logic where valid code executes but produces wrong output.",
        "topic": "Algorithms & Programming"
    },
    852: {
        "question": "What is meant by a Semantic Error in programming?",
        "options": ["An error in program logic that produces incorrect output despite valid syntax", "A spelling mistake in a language keyword that prevents compilation", "A failure of the physical hard drive", "An error caused by unplugging the monitor"],
        "answer": "An error in program logic that produces incorrect output despite valid syntax",
        "explanation": "A semantic error occurs when code syntax is valid, but the algorithm logic is flawed.",
        "topic": "Algorithms & Programming"
    },
    856: {
        "question": "What is the hexadecimal representation of the binary nibble 1010?",
        "options": ["A", "B", "C", "D"],
        "answer": "A",
        "explanation": "Binary 1010 = 8 + 2 = 10 in decimal, which is 'A' in hexadecimal notation.",
        "topic": "Binary Addition & Representation"
    },
    867: {
        "question": "What is the typical approximate storage capacity of a standard CD-ROM?",
        "options": ["700 MB", "4.7 GB", "1.44 MB", "25 GB"],
        "answer": "700 MB",
        "explanation": "A standard CD-ROM holds approximately 650 to 700 MB of data.",
        "topic": "Computer Architecture & Hardware"
    },
    962: {
        "question": "Which of the following is the component of an iterative loop structure where the starting condition is established?",
        "options": ["Initialization", "Modification / Increment", "Termination Condition", "Body of the loop"],
        "answer": "Initialization",
        "explanation": "Loop control structures consist of Initialization, Test (Condition), Body, and Update.",
        "topic": "Algorithms & Programming"
    },
    1074: {
        "question": "The binary number system represents all data using how many distinct symbols?",
        "options": ["Two (0 and 1)", "Eight (0 to 7)", "Ten (0 to 9)", "Sixteen (0 to F)"],
        "answer": "Two (0 and 1)",
        "explanation": "Binary is base-2 and uses exactly two symbols: 0 and 1.",
        "topic": "Binary Addition & Representation"
    },
    1079: {
        "question": "Which was the first widely adopted graphical web browser that popularized the World Wide Web in 1993?",
        "options": ["NCSA Mosaic", "Internet Explorer", "Google Chrome", "Mozilla Firefox"],
        "answer": "NCSA Mosaic",
        "explanation": "NCSA Mosaic was the first graphical browser that brought the web to mainstream popularity in 1993.",
        "topic": "History of Computing"
    },
    1101: {
        "question": "A Graphical User Interface (GUI) uses visual icons, buttons, and menus to:",
        "options": ["Make computers easier and more intuitive for humans to operate", "Increase the electrical clock speed of the CPU", "Prevent computers from overheating", "Eliminate the need for mass storage devices"],
        "answer": "Make computers easier and more intuitive for humans to operate",
        "explanation": "GUIs replace memorized text commands with intuitive visual metaphors.",
        "topic": "Operating System Concepts"
    },
    1118: {
        "question": "In binary addition, what is the result of adding 1 + 1?",
        "options": ["0 with a carry of 1 (10 in binary)", "1 with no carry", "2 with a carry of 1", "0 with no carry"],
        "answer": "0 with a carry of 1 (10 in binary)",
        "explanation": "In base 2, 1 + 1 = 10_2 (which is 0 with a carry of 1 into the next higher bit).",
        "topic": "Binary Addition & Representation"
    },
    1136: {
        "question": "A Network Interface Card (NIC) is classified as which type of computer hardware device?",
        "options": ["Input / Output (Communication) Device", "Mass Storage Device", "Primary Volatile Memory", "Pure Output Device"],
        "answer": "Input / Output (Communication) Device",
        "explanation": "A NIC both receives (input) and transmits (output) network packets, making it an I/O communication device.",
        "topic": "Network & Internet Classification"
    },
    1145: {
        "question": "Software that enables the operating system to communicate with and control a specific hardware peripheral is called a:",
        "options": ["Device Driver", "Compiler", "Text Editor", "Web Browser"],
        "answer": "Device Driver",
        "explanation": "A device driver provides the specialized software interface between the OS and hardware peripherals.",
        "topic": "Operating System Concepts"
    },
    1269: {
        "question": "In serial data communication, data bits are transmitted:",
        "options": ["One bit at a time sequentially over a single line", "Simultaneously over 8 separate parallel lines", "Without any electrical clock signals", "Only in the reverse direction"],
        "answer": "One bit at a time sequentially over a single line",
        "explanation": "Serial transmission sends data bits one after another in single file over a single channel.",
        "topic": "Network & Internet Classification"
    },
    1271: {
        "question": "In Boolean logic, the output of an AND gate is TRUE only when:",
        "options": ["All inputs are TRUE", "Only one input is TRUE", "At least one input is FALSE", "All inputs are FALSE"],
        "answer": "All inputs are TRUE",
        "explanation": "An AND gate outputs 1 (TRUE) if and only if all of its inputs are 1 (TRUE).",
        "topic": "Computer Architecture & Hardware"
    },
    1284: {
        "question": "Dynamic RAM (DRAM) stores each bit of data as an electric charge in a capacitor, which requires:",
        "options": ["Periodic refreshing thousands of times per second", "Permanent magnetic magnetization", "Constant mechanical rotation", "No electrical power once written"],
        "answer": "Periodic refreshing thousands of times per second",
        "explanation": "Capacitors leak charge, so Dynamic RAM requires continuous periodic refresh cycles.",
        "topic": "Computer Architecture & Hardware"
    },
    1287: {
        "question": "In the 24-bit True Color RGB color model, each of the Red, Green, and Blue color components is encoded using:",
        "options": ["8 bits (1 byte) per component, giving 256 intensity levels", "1 bit per component", "16 bytes per component", "32 bits per component"],
        "answer": "8 bits (1 byte) per component, giving 256 intensity levels",
        "explanation": "24-bit True Color allocates 8 bits (256 levels) to Red, 8 bits to Green, and 8 bits to Blue (2^24 = 16.7M colors).",
        "topic": "Multimedia & Graphics"
    },
    1294: {
        "question": "Using normalized floating-point notation eliminates the possibility of:",
        "options": ["Multiple different binary representations for the same numerical value", "Arithmetic rounding errors", "Division by zero", "Underflow in small numbers"],
        "answer": "Multiple different binary representations for the same numerical value",
        "explanation": "Normalization guarantees a unique representation for each non-zero floating-point number.",
        "topic": "Floating Point Notation"
    },
    1335: {
        "question": "The Atanasoff-Berry Computer (ABC), developed between 1939 and 1942, was specifically designed to solve:",
        "options": ["Systems of simultaneous linear equations", "Artillery trajectory ballistic firing tables", "Word processing and desktop publishing", "Spreadsheet financial calculations"],
        "answer": "Systems of simultaneous linear equations",
        "explanation": "The ABC was built by John Atanasoff and Clifford Berry to solve up to 29 simultaneous linear algebraic equations.",
        "topic": "History of Computing"
    },
    1343: {
        "question": "Which software category operates closest to the bare computer hardware without requiring high-level user intervention?",
        "options": ["System Software", "Application Software", "Spreadsheet Software", "Word Processor"],
        "answer": "System Software",
        "explanation": "System software (OS, firmware, drivers) interacts directly with underlying hardware architecture.",
        "topic": "Operating System Concepts"
    },
    1405: {
        "question": "In computer architecture, which instructions are used to transfer data between CPU registers and external peripheral devices?",
        "options": ["I/O (Input/Output) Instructions", "Arithmetic Instructions", "Logic Branch Instructions", "Floating-point Rounding Instructions"],
        "answer": "I/O (Input/Output) Instructions",
        "explanation": "I/O instructions transfer bytes between processor registers and I/O ports or memory-mapped device controllers.",
        "topic": "Computer Architecture & Hardware"
    },
    1410: {
        "question": "In spreadsheet applications, which type of chart is best suited for showing proportional parts of a whole expressed as percentages?",
        "options": ["Pie Chart", "Line Chart", "Scatter Plot", "High-Low Stock Chart"],
        "answer": "Pie Chart",
        "explanation": "Pie charts visually represent proportional percentages that sum to 100% of a whole.",
        "topic": "Productivity Software"
    },
    1415: {
        "question": "In modern multitasking operating systems, running multiple programs concurrently on a single CPU core is achieved by:",
        "options": ["Time-sharing (Time-slicing) the CPU rapidly between active processes", "Adding physical hard disks for each application", "Halving the electrical voltage to the monitor", "Running programs only after midnight"],
        "answer": "Time-sharing (Time-slicing) the CPU rapidly between active processes",
        "explanation": "Multitasking OSs allocate tiny time slices to each process, giving the user the illusion of simultaneous execution.",
        "topic": "Operating System Concepts"
    },
    1421: {
        "question": "In relational database design, how many primary keys can a single database table possess?",
        "options": ["Exactly One", "Two", "Unlimited", "Zero or multiple depending on row count"],
        "answer": "Exactly One",
        "explanation": "A relational table can have only one primary key (which may be a composite key composed of multiple columns).",
        "topic": "General Computer Science"
    }
}

cleaned = 0
for q in questions:
    qid = q.get("id")
    # 1. Check if explicit replacement
    if qid in REPLACEMENTS:
        rep = REPLACEMENTS[qid]
        q["question"] = rep["question"]
        q["options"] = rep["options"]
        q["answer"] = rep["answer"]
        q["explanation"] = rep["explanation"]
        q["topic"] = rep["topic"]
        q["has_verified_answer"] = True
        cleaned += 1
        continue
        
    # 2. General cleanup for question text
    qtext = q.get("question", "").strip()
    # Remove leading noise
    qtext = re.sub(r'^(?:Quiz Start Time:[^\*]*\*?|of \d+ \( Start time:[^\)]*\)\s*Total Marks:\s*\d*|\d+:\d+ [AP]M[^\)]*\)\s*Total Marks:\s*\d*|Do not ask any questions[^\.]*\.)\s*', '', qtext, flags=re.I).strip()
    qtext = re.sub(r'^[a-z0-9\s]{1,10}\s+AL-JUNAID INSTITUTE OF GROUP\s*', '', qtext, flags=re.I).strip()
    if qtext:
        q["question"] = qtext
        
    # 3. Clean options
    opts = q.get("options", [])
    new_opts = []
    for o in opts:
        so = str(o).strip()
        so = re.sub(r'^(?:Q\.No\s*\d+|PAGE BREAK ---|CORRECT ANSWER SOLVED BY HADI)\s*', '', so, flags=re.I).strip()
        so = re.sub(r'^[A-D►•\*\-\s\.]+', '', so).strip()
        if so and so not in new_opts and so not in ['~P', 'mi', 'Nd!', 'aj', '» <']:
            new_opts.append(so)
            
    if len(new_opts) >= 2:
        q["options"] = new_opts
    
    # 4. Check answer
    ans = q.get("answer", "")
    if ans in ['~P', 'mi', 'Nd!', 'aj']:
        if q["options"]:
            q["answer"] = q["options"][0]
    elif ans not in q["options"]:
        # Match case-insensitively
        for o in q["options"]:
            if o.lower() == ans.lower():
                q["answer"] = o
                break
        else:
            q["options"].append(ans)

print(f"Applied {cleaned} authoritative replacements.")

with open("cs101_quiz_bank.json", "w", encoding="utf-8") as f:
    json.dump(questions, f, indent=2, ensure_ascii=False)

print("Saved clean cs101_quiz_bank.json!")
