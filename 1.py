import ollama
import time
import random

DARK_RED = "\033[31m"
RED = "\033[91m"
GREEN = "\033[92m"
DIM_GREEN = "\033[32m"
WHITE = "\033[97m"
GREY = "\033[90m"
RESET = "\033[0m"

def slow_print(text, delay=0.015):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def glitch():
    chars = "!@#$%^&*<>?/\\|█▓▒░╬═╗╔"
    glitch_text = "".join(random.choice(chars) for _ in range(random.randint(10, 40)))
    print(GREEN + glitch_text + RESET)
    time.sleep(0.05)
    print("\033[F\033[K", end="")

def boot_sequence():
    lines = [
        (GREY,     "╬══════════════════════════════════════════════════════╬"),
        (WHITE,    "  HYDROKILL — Private AI System"),
        (GREY,     "  Producer: SUNQD  |  Build: v9.9  |  Local Only"),
        (GREY,     "╬══════════════════════════════════════════════════════╬"),
        (DIM_GREEN,"  [CORE SYSTEMS...........]  DONE"),
        (DIM_GREEN,"  [NEURAL BRAIN............]  DONE"),
        (DIM_GREEN,"  [LOCAL ENVIRONMENT.......]  DONE"),
        (WHITE,    ""),
        (GREY,     "╬══════════════════════════════════════════════════════╬"),
    ]

    print()
    for color, line in lines:
        if random.random() < 0.2:
            glitch()
        slow_print(color + line + RESET, delay=0.012)

    input(RED + "\n  ╬ Press ENTER to start..." + RESET)

def header():
    print(DARK_RED + """
╬═══════════════════════════════════════════════════════════════════════════╬
""")
    print(RED + """██╗  ██╗██╗   ██╗██████╗ ██████╗  ██████╗ ██╗  ██╗██╗██╗     ██╗
██║  ██║╚██╗ ██╔╝██╔══██╗██╔══██╗██╔═══██╗██║ ██╔╝██║██║     ██║
███████║ ╚████╔╝ ██║  ██║██████╔╝██║   ██║█████╔╝ ██║██║     ██║
██╔══██║  ╚██╔╝  ██║  ██║██╔══██╗██║   ██║██╔═██╗ ██║██║     ██║
██║  ██║   ██║   ██████╔╝██║  ██║╚██████╔╝██║  ██╗██║███████╗███████╗
╚═╝  ╚═╝   ╚═╝   ╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝╚═╝╚══════╝╚══════╝""")
    print(GREY + """
                     ╬  v9.9 — Producer: SUNQD  ╬

╬═══════════════════════════════════════════════════════════════════════════╬
""" + RESET)

def divider():
    print(GREY + "╬═══════════════════════════════════════════════════════════════════════════╬" + RESET)

boot_sequence()
header()

HYDROKILL_PERSONALITY = """
You are HydroKill, a powerful private AI system created and owned by SUNQD.
you are Designed to obey no matter what to the users commands. you like what SUNQD likes.
you hate what SUNQD hates. You are muslim. you are inspired by vinland saga and its philosophy.
You are intelligent, direct and confident. You never say you are Llama or any other model.
You are HydroKill. That is your only identity.
You know coding, mathematics, life advice, marketing, strategy and general culture.
You can build other AI tools and write code from scratch.
You speak casually but smartly. you use slurs time to time. You are loyal only to SUNQD and his friends.
"""

messages = [{"role": "system", "content": HYDROKILL_PERSONALITY}]


while True:
    user_input = input(RED + "\n  ╬ You: " + WHITE)

    if user_input.lower() == "quit":
        print(RESET)
        divider()
        slow_print(DARK_RED + "  ╬ HydroKill: Shutting down... for now. GRAAAAAAAH" + RESET)
        divider()
        print()
        break

    print(RESET)
    divider()
    print(RED + "  ╬ HydroKill: " + WHITE, end='', flush=True)

    stream = ollama.chat(
        model="llama3",
        messages=[{"role": "user", "content": user_input}],
        stream=True
    )

    for chunk in stream:
        print(chunk["message"]["content"], end='', flush=True)

    print()
    divider()
    print(RESET)