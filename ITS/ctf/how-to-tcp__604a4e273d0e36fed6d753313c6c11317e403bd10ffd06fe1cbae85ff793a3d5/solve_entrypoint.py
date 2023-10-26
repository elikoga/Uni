#!/usr/bin/env python3

# pwntools https://github.com/Gallopsled/pwntools
# Siehe insbesondere den Abschnitt "Installation"
# Linux wird empfholen
# Windows *kann* funktionieren, es wurde bisher nicht getestet; WSL funktioniert
from pwn import *

# Durch setzen des log_levels auf DEBUG wird jegliche Kommunikation mit dem Server
# ausgegeben. Dies kann beim debuggen sehr nützlich sein
# context.log_level = 'DEBUG'

r = remote('itsec.cs.uni-paderborn.de', 10000)

# Warten dass eine Zeile welche mit '###END WELCOME###' startet empfangen wurde
r.recvline_startswith('###END WELCOME###')
# lese die nächste Zeile
x = r.recvline()
# Sende 42 (Wichtig: als String)
r.sendline('42')

# Starte einen interaktiven Modus
# Empfehlenswert wenn man nicht weiß wie sich der Server weiterhin verhält
r.interactive()
