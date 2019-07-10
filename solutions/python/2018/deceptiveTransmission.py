"""
Due to recent advances in our cryptographic technology (i.e. the invention of the state-of-the-art Ceasar Cipher decoder),
the opposition has been on the losing side. As their attack plans were leaked and used against them, they suffered heavy losses.
Many soldiers from the enemy side defected and the war seemed like it would end soon.
However, just when you thought everything was over, the enemy was able to come up with a new cipher.
With their newly secure communication channels in place, the enemy is now moving again.

Can you crack the enemy code? Time is of the essense. The outcome of the war lies in your hands.

Example
For enemyMessage = "‪T‪h‪i‪s‪ ‭i‪s‪ ‭H‭Q‭.‪ ‪C‭o‭m‪m‪e‪n‪c‪e‪ ‪o‪p‭e‪r‪a‭t‪i‭o‪n‭ ‭C‪O‭B‪R‭A‪.‪ ‭S‪e‪n‭d‭ ‭a‪l‭l‪ ‭u‪n‪i‭t‪s‪ ‭t‭o‪ ‪a‭t‭t‭a‭c‭k‪ ‭t‪h‪e‪ ‭n‭o‪r‪t‪h‪ ‪g‪a‭t‪e‪ a‭t‪ ‪2‭1‪4‪5", the output should be
deceptiveTransmission(enemyMessage) = "ATTACK SOUTH GATE".

How the actual message was encrypted is not clear to us, but we found this note in an enemy base: Pqbdxkldoxmev / Yxzlk'p zfmebo
"""

m, = eval(dir()[0])
s = ''
while m:
    t = 1
    for _ in '     ':
        i, j, *m = m
        t += t + ord(i) % 2
    s += chr(-~t % 59 + 32)
return s.strip()
