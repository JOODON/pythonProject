from Score import *
#작업 선택 종류
SEARCH, LIST, STATS, DATAMG, END = ('1', '2', '3', '4', 'x')

def sel_task(): #작업 선택 메뉴
    print("_"*50)
    print("1:검색   2:현황   3:통계   4:데이터관리   x:종료")
    selno = input("<작업 선택> ")
    if len(selno) == 0:
        return 'x'
    else:
        return selno
def find_student():
    instid = input(">학번 입력: ")
    val = get_student(instid)
    sname, deptid = val #리스트 언팩킹
    dname = get_dept(deptid)
    print("학번: %s    성명: %s   소속학과: %s(%s)" %(instid, sname, dname, deptid))

def selmenu01_find():
    while True:
        print("_"*50)
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
        print("_"*50)
        print("1:학생 성적 현황(학생 성적 통지서) 2.과목별 성적 현황 3.복귀")
        selno = input("<작업 선택> ")
        if len(selno) == 0 or selno == '0':
            return
        if len(selno) >= 0 and type(int(selno)) is int:
            selno = int(selno)
            if selno == 1:
                all_List();
            elif selno == 2:
                find_dept()
            elif selno == 3:
                find_dept()
            else:
                print("!잘못된 입력!")

###########################################################2###################################################################
def find_student():
    instid = input(">학번 입력: ")
    val = get_student(instid)
    sname, deptid = val #리스트 언팩킹
    dname = get_dept(deptid)
    print("학번: %s    성명: %s   소속학과: %s(%s)" %(instid, sname, dname, deptid))

def find_dept():
    indeptid=input(">학과 번호 입력:")
    dname=get_dept(indeptid)
    print("학과명 :%s (%s)"%(dname,indeptid))

def find_prof():
    prof=input(">검색할 교수님을 입력:")
    dname=get_prof(prof)
    name,age=dname
    print("교수님 성함 :%s (%s)"%(name,age))

def find_subject():
    insubject=input(">검색할 과목을 입력:")
    subject=get_subject(insubject)
    study,time,fulltime,FirstName=subject
    print("[과목명:%s] [학점 : %s] [이수 시간:%s] [ProF:%s]"%(study,time,fulltime,FirstName))
def find_stscore():
    instscore=input(">[학번]을 입력 해주세요")
    for number,studynumber,score in stscore:
        if instscore == number:
            print("[번호 :%s] [과목 번호:%s] [점수:%s]"%(number,studynumber,score))

###########################################################2###################################################################
def all_List():
    instid = input(">학번 입력: ")
    val = get_student(instid)
    sname, deptid = val
    dname = get_dept(deptid)
    print("[학번: %s]    [성명: %s]   [소속학과: %s(%s)]" %(instid, sname, dname, deptid))


########## Main ################
while True:         #작업 선택
    selno = sel_task()      #작업 번호 선택
    if selno == SEARCH:
        selmenu01_find()
    elif selno == LIST:
        List01_find()
    elif selno == STATS:
        print(STATS)
    elif selno == DATAMG:
        selmenu04_up()
    elif selno == END:          #(x)끝내기
        break
    else:
        break
################################

