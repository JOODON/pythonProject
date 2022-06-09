for i in range(1, len(score), 1):
    if rank == "A+":
        credit = 4.5
    elif rank == "A":
        credit = 4.3
    elif rank == "B+":
        credit = 3.5
    elif rank == "B":
        credit = 3.3
    elif rank == "C+":
        credit = 2.5
    elif rank == "C":
        credit = 2.3
    elif rank == "D+":
        credit = 1.5
    elif rank == "D":
        credit = 1.3
    else:
        credit = 0