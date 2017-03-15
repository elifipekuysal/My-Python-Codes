i_pangram= "the quick brown fox jumps over the lazy dog"
t_pangram= "pijamalı hasta yağız şoföre çabucak güvendi"

for i in t_pangram: 
    if i not in i_pangram:
        print(i)
