def result(answer,guess):
    A=0
    B=0
    for idx_ans, val_ans in enumerate(answer):
            if answer[idx_ans] == guess[idx_ans]:
                A+=1
            elif val_ans in guess:
                B+=1
    return str(A)+"A"+str(B)+"B"

    print(result('1234','4321'))