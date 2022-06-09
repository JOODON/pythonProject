from Score import *

# 작업 선택 종류
SEARCH, LIST, STATS, DATAMG, END = ('1', '2', '3', '4', 'x')

def sel_task():  # 작업 선택 메뉴
    print("_" * 50)
    print("1:검색   2:현황   3:통계   4:데이터관리   x:종료")
    selno = input("<작업 선택> ")
    if len(selno) == 0:
        return 'x'
    else:
        return selno


def find_student():
    instid = input(">학번 입력: ")
    val = get_student(instid)
    sname, deptid = val  # 리스트 언팩킹
    dname = get_dept(deptid)
    print("학번: %s    성명: %s   소속학과: %s(%s)" % (instid, sname, dname, deptid))


def selmenu01_find():
    while True:
        print("_" * 50)
        print("1: 학생검색    2: 학과검색    3: 교수검색    4: 과목검색    5: 성적검색    0: 복귀")
        selno = input("<작업 선택> ")
        if len(selno) == 0 or selno == '0':
            return
        if len(selno) >= 0 and type(int(selno)) is int:
            selno = int(selno)
            if selno == 1:
                find_student()
            elif selno == 2:
                find_dept()
            elif selno == 3:
                find_prof()
            elif selno == 4:
                find_subject()
            elif selno == 5:
                find_stscore()
            else:
                print("!잘못된 입력!")


def List01_find():
    while True:
        print("_" * 50)
        print("1:학생 성적 현황(학생 성적 통지서) 2.과목별 성적 현황 3.복귀")
        selno = input("<작업 선택> ")
        if len(selno) == 0 or selno == '0':
            return
        if len(selno) >= 0 and type(int(selno)) is int:
            selno = int(selno)
            if selno == 1:
                all_List()
            elif selno == 2:
                List_subject1()
            elif selno == 3:
                find_dept()
            else:
                print("!잘못된 입력!")


###########################################################2###################################################################
def find_student():
    instid = input(">학번 입력: ")
    val = get_student(instid)
    sname, deptid = val  # 리스트 언팩킹
    dname = get_dept(deptid)
    print("학번: %s    성명: %s   소속학과: %s(%s)" % (instid, sname, dname, deptid))


def find_dept():
    indeptid = input(">학과 번호 입력:")
    dname = get_dept(indeptid)
    print("학과명 :%s (%s)" % (dname, indeptid))


def find_prof():
    prof = input(">검색할 교수님을 입력:")
    dname = get_prof(prof)
    name, age = dname
    print("교수님 성함 :%s (%s)" % (name, age))


def find_subject():
    insubject = input(">검색할 과목을 입력:")
    subject = get_subject(insubject)
    study, time, fulltime, FirstName = subject
    print("[과목명:%s] [학점 : %s] [이수 시간:%s] [ProF:%s]" % (study, time, fulltime, FirstName))


def find_stscore():
    instscore = input(">[학번]을 입력 해주세요")
    for number, studynumber, score in stscore:
        if instscore == number:
            print("[번호 :%s] [과목 번호:%s] [점수:%s]" % (number, studynumber, score))


###########################################################2###################################################################
def all_List():
    instid = input(">학번 입력: ")
    val = get_student(instid)
    sname, deptid = val
    dname = get_dept(deptid)
    print("[학번: %s]    [성명: %s]   [소속학과: %s(%s)]" % (instid, sname, dname, deptid))
    count=0
    counttime=0
    Average=0
    sumscore=0
    for number, studynumber, score in stscore:
        subject = get_subject(studynumber)
        study, time, fulltime, FirstName = subject
        ascore=int(score)
        if ascore <= 100 and ascore>= 95:
            rank = "A+"
        elif ascore < 95 and ascore >= 90:
            rank = "A"
        elif ascore < 90 and ascore >= 85:
            rank = "B+"
        elif ascore < 85 and ascore >=80:
            rank = "B"
        elif ascore < 80 and ascore >=75:
            rank = "C+"
        elif ascore < 75 and ascore >=70:
            rank = "C"
        elif ascore < 70 and ascore >=65:
            rank = "D+"
        elif ascore < 65 and ascore >=60:
            rank = "D"
        else:
            rank = "F"
        if number == instid:
            print("[과목명:%s] [과목코드 : %s] [학점:%s] [점수:%s] [등급:%s]" % (study, studynumber, time, score,rank))
            count+=1
            times=int(time)##학점을 더해주기 위해 형 변환
            counttime=counttime+times##총 학점 수
            sumscore=sumscore+int(score)##평균을 구하기 위해 형 변환
            Average=sumscore/count##평균 값

            sumcredit = 0  ##평점 출력
            credit = 0
            if rank == "A+":
                credit += 4.5
            elif rank == "A":
                credit += 4.3
            elif rank == "B+":
                credit += 3.5
            elif rank == "B":
                credit += 3.3
            elif rank == "C+":
                credit += 2.5
            elif rank == "C":
                credit += 2.3
            elif rank == "D+":
                credit += 1.5
            elif rank == "D":
                credit += 1.3
            else:
                credit = 0
    print("[과목 수:%d] [학점 수:%d] [평균 점수: %d] [평점%.1f]"%(count,counttime,Average,float(credit)))

def List_subject1():
    insubject = input(">검색할 과목코드를 입력해주세요:")
    subject = get_subject(insubject)
    study, time, fulltime, FirstName = subject
    dname = get_prof(FirstName)
    name, age = dname
    dname = get_dept(fulltime)

    print("[과목명:%s] [과목코드: %s][학점 : %s] [개설 학과:%s] [교수님 이름:%s]" % (study,insubject,time,dname,name))


########## Main ################
while True:  # 작업 선택
    selno = sel_task()  # 작업 번호 선택
    if selno == SEARCH:
        selmenu01_find()
    elif selno == LIST:
        List01_find()
    elif selno == STATS:
        print(STATS)
    elif selno == DATAMG:
        selmenu04_up()
    elif selno == END:  # (x)끝내기
        break
    else:
        break
################################