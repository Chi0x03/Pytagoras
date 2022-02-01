import math
from textwrap import dedent

# CORES -----------------
A   = "\x1b[38;5;220m" #|
A2  = "\x1b[38;5;12m"  #|
B   = "\x1b[38;5;15m" #|
RST = "\x1b[0m"        #|
# CORES -----------------

def banner():
    print(dedent(f"""
    {B}◖--------- {A2}P{A}y{B}tagoras ---------◗{RST}
    
    """))

def main():
    c1 = int(input(f"{A}Cateto 1{RST}: "))
    c2 = int(input(f"{A2}Cateto 2{RST}: "))
    c1 **= 2
    c2 **= 2
    hipo2 = c1 + c2
    hipo = int(math.sqrt(hipo2))
    print(f"{B}Hipotenusa: {hipo}{RST}")

banner()
main()