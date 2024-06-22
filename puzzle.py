from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

A_Statement = Symbol ("A's Statement")
B_Statement = Symbol ("B's Statement")
C_Statement = Symbol ("C's Statement")

# Puzzle 0
# A says "I am both a knight and a knave." => AKnave
A_Statement= And (AKnight, AKnave)

knowledge0 = And(
    Or (AKnight, AKnave), # A is either a knight or a knave
    Or (BKnight, BKnave), # B is either a knight or a knave
    Or (CKnight, CKnave), # C is either a knight or a knave
    Not (And (AKnight, AKnave)), # A cannot be both a knight and a knave
    Not (And (BKnight, BKnave)), # B cannot be both a knight and a knave
    Not (And (CKnight, CKnave)), # C cannot be both a knight and a knave
    Biconditional (A_Statement, AKnight) # A is a knight if A's statement is true
)

# Puzzle 1
# A says "We are both knaves." => AKnave
# B says nothing. => BKnight
A_Statement = And (AKnave, BKnave)

knowledge1 = And(
    Or (AKnight, AKnave), # A is either a knight or a knave
    Or (BKnight, BKnave), # B is either a knight or a knave
    Or (CKnight, CKnave), # C is either a knight or a knave
    Not (And (AKnight, AKnave)), # A cannot be both a knight and a knave
    Not (And (BKnight, BKnave)), # B cannot be both a knight and a knave
    Not (And (CKnight, CKnave)), # C cannot be both a knight and a knave
    Biconditional (A_Statement, AKnight) # A is a knight if A's statement is true
)

# Puzzle 2
# A says "We are the same kind." => AKnave
# B says "We are of different kinds." => BKnight
A_Statement = Or(And(AKnight, BKnight), And(AKnave, BKnave))
B_Statement = Or(And(AKnight, BKnave), And(AKnave, BKnight))

knowledge2 = And(
    Or (AKnight, AKnave), # A is either a knight or a knave
    Or (BKnight, BKnave), # B is either a knight or a knave
    Or (CKnight, CKnave), # C is either a knight or a knave
    Not (And (AKnight, AKnave)), # A cannot be both a knight and a knave
    Not (And (BKnight, BKnave)), # B cannot be both a knight and a knave
    Not (And (CKnight, CKnave)), # C cannot be both a knight and a knave
    Biconditional (A_Statement, AKnight), # A is a knight if A's statement is true
    Biconditional (B_Statement, BKnight) # B is a knight if B's statement is true
)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which. => A is a knight
A_Statement = Or (AKnight, AKnave)
# B says "A said 'I am a knave'." => B is a knave
# B says "C is a knave." => B is a knave.
B_Statement = And (Biconditional(AKnave, BKnight),CKnave)
# C says "A is a knight." => C is a knight.
C_Statement = AKnight 

knowledge3 = And(
    Or (AKnight, AKnave), # A is either a knight or a knave
    Or (BKnight, BKnave),  # B is either a knight or a knave
    Or (CKnight, CKnave),  # C is either a knight or a knave
    Not (And (AKnight, AKnave)), # A cannot be both a knight and a knave
    Not (And (BKnight, BKnave)), # B cannot be both a knight and a knave
    Not (And (CKnight, CKnave)), # C cannot be both a knight and a knave
    Biconditional (A_Statement, AKnight), # A is a knight if A's statement is true
    Biconditional (B_Statement, BKnight), # B is a knight if B's statement is true
    Biconditional (C_Statement, CKnight) # C is a knight if C's statement is true
)


def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()
