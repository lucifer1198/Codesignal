"""This is a reverse challenge, enjoy!"""

# msg: "a"
# "a"
#
# msg: "b"
# "x"
#
# msg: "c"
# "j"
#
# msg: "Codefights"
#      "Jre.ucidyo"
#
# msg: "Simple message"
#      "Ocmln. m.ooai."
#
# msg: "Karovd"
#      "Taprke"

# 167 chars
# A = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
# B = "AXJE>UIDCHTNMBRL POYGK<QF:axje.uidchtnmbrl poygk,qf;"
#
# def Karovd(msg):
#    t = str.maketrans(A, B)
#    return msg.translate(t)


# 154 chars
# def Karovd(m):
#    return m.translate(
#        str.maketrans(
#            "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz",
#            "AXJE>UIDCHTNMBRL POYGK<QF:axje.uidchtnmbrl poygk,qf;"
#        )
#    )


# 147 chars
def Karovd(m):
    import string as S
    return m.translate(
        str.maketrans(
            ''.join(sorted(S.ascii_letters)),
            "AXJE>UIDCHTNMBRL POYGK<QF:axje.uidchtnmbrl poygk,qf;"
        )
    )
