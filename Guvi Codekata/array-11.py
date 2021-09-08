def mark(no_stu, stdu_mark):
    ramesh_mark = int(no_stu[1])
    no_of_stdu = int(no_stu[0])
    if no_of_stdu == len(stdu_mark):
        if str(ramesh_mark) in stdu_mark:
            print(stdu_mark.index(str(ramesh_mark)))
        if str(ramesh_mark) not in stdu_mark:
            print(-1)
    else:
        None
mark(input().split(),input().split())