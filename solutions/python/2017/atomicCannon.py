"""
The mad scientist has developed a new communication device; he dubbed it "the Atomic Cannon."
This cannon can shoot out atoms of all different elements from the lightest element Hydrogen (H-1) to the superheavy element Oganesson (Og-118).

To encode a message into atoms, the mad scientist needs a way to break the message into different atomic symbols like H and Og.
For example, he can break the string "nation" into Na, Ti, O, and N. Of course he can also break it into N, At, I, O, N,
but this composition costs a lot more. To be specific, the former costs only 48 protons while the latter costs 160!
While the scientist is crazy, he doesn't have unlimited research funds!

The mad scientist requires your help. Given a string, you need to tell him how to break it down.
For the example above, you will need to return the string "Na Ti O N" (spaces are used as the delimiter).

Remember that:

- If there are multiple ways to break down a string, use the one with the smallest sum of atomic numbers.
- If there is a tie in terms of atomic numbers, return the lexicographically smallest string.
- In the event it's impossible to find a match, return "Invalid"

Here are all the elements in order of their atomic numbers (1-118):

H He Li Be B C N O F Ne Na Mg Al Si P S Cl Ar K Ca Sc Ti V Cr Mn Fe Co Ni Cu Zn Ga Ge As Se Br Kr Rb Sr Y Zr Nb Mo Tc Ru Rh Pd Ag Cd In Sn Sb Te I Xe Cs Ba La Ce Pr Nd Pm Sm Eu Gd Tb Dy Ho Er Tm Yb Lu Hf Ta W Re Os Ir Pt Au Hg Tl Pb Bi Po At Rn Fr Ra Ac Th Pa U Np Pu Am Cm Bk Cf Es Fm Md No Lr Rf Db Sg Bh Hs Mt Ds Rg Cn Nh Fl Mc Lv Ts Og

Example:

For message = "nation", the output should be
atomicCannon(message) = "Na Ti O N".

For message = "prhona", the output should be
atomicCannon(message) = "P Rh O Na".

Note that both "Pr H O Na" and "P Rh O Na" have a sum of 79 protons, but "P Rh O Na" is lexicographically smaller.

For message = "imthebestscientist", the output should be
atomicCannon(message) = "Invalid".

There are no possible matches.
"""


def atomicCannon(s):
    # solution by steven_w30
    INF = float('inf')
    E = ["H", "He", "Li", "Be", "B", "C", "N", "O", "F", "Ne", "Na", "Mg", "Al", "Si", "P", "S",
         "Cl", "Ar", "K", "Ca", "Sc", "Ti", "V", "Cr", "Mn", "Fe", "Co", "Ni", "Cu", "Zn", "Ga",
         "Ge", "As", "Se", "Br", "Kr", "Rb", "Sr", "Y", "Zr", "Nb", "Mo", "Tc", "Ru", "Rh", "Pd",
         "Ag", "Cd", "In", "Sn", "Sb", "Te", "I", "Xe", "Cs", "Ba", "La", "Ce", "Pr", "Nd", "Pm",
         "Sm", "Eu", "Gd", "Tb", "Dy", "Ho", "Er", "Tm", "Yb", "Lu", "Hf", "Ta", "W", "Re", "Os",
         "Ir", "Pt", "Au", "Hg", "Tl", "Pb", "Bi", "Po", "At", "Rn", "Fr", "Ra", "Ac", "Th", "Pa",
         "U", "Np", "Pu", "Am", "Cm", "Bk", "Cf", "Es", "Fm", "Md", "No", "Lr", "Rf", "Db", "Sg",
         "Bh", "Hs", "Mt", "Ds", "Rg", "Cn", "Nh", "Fl", "Mc", "Lv", "Ts", "Og"]

    EL = [e.lower() for e in E]
    N = len(s)
    A = [[] for _ in range(N)]
    C = [INF] * N + [0]

    for i in range(N, 0, -1):
        if C[i] < INF:
            for j, e in enumerate(EL):
                i0 = i - len(e)
                if i0 >= 0 and s[i0:i] == e:

                    if C[i] + j + 1 < C[i0]:
                        A[i0] = [j + 1]
                        C[i0] = C[i] + j + 1

                    elif C[i] + j + 1 == C[i0]:
                        A[i0] += [j + 1]
    if C[0] == INF:
        return 'Invalid'

    ret = []
    i = 0
    while i < N:
        ret += [min(E[x - 1] for x in A[i])]
        i += len(ret[-1])
    return ' '.join(ret)
