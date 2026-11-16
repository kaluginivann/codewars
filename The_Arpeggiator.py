# In music, a scale is made up of seven different values (A through G inclusive) with the ROOT value occuring twice forming the scale's first and eighth (last) note.

# So if the root = B, the scale looks like this:

#   B C D E F G A B
  
# and if the root = F, the scale looks like this:

#   F G A B C D E F
  
# Each scale has an arpeggio made up of it's first, third, fifth and eighth notes.

# So the arpeggio for scale root B looks like this:

#  B D F B
 
# and the arpeggio for scale root F looks like this:

#  F A C F
 
# Write a programme that takes any possible root note and returns its arpeggio in an array. If the object input isn't a root note, return an empty value in your language (for example undefined / Nothing / None). Watch for capitalization!

# Example:

# arpeggio("A") == ["A", "C", "E", "A"]
# arpeggio("E") == ["E", "G", "B", "E"]
# arpeggio("Z") == None
# arpeggio("a") == None


def arpeggio(note: str) -> list[str] | None:
    notes = ["A", "B", "C", "D", "E", "F", "G"]
    
    if note not in notes:
        return None
    
    start = notes.index(note)
    scale = [notes[(start + i) % 7] for i in range(8)]
    
    return [scale[0], scale[2], scale[4], scale[7]]