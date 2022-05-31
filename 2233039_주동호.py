grades = (["A+", [100, 95]], ["A", [94, 90]],
          ["B+", [80, 85]], ["B", [84, 80]],
          ["C+", [79, 75]], ["C", [74, 70]],
          ["D+", [69, 65]], ["D", [64, 60]],
          ["F", [59, 0]])

members = (('choi', 93), ('han', 50),
           ('jung', 92), ('kang', 68),
           ('kim', 80),('lee', 90),
           ('moon', 65), ('na', 100),
           ('park', 75), ('song', 75))

def find_grade(inscore):
    for grade,zone in grades:
        if inscore>= zone[1] and inscore<= zone[0]:
            outgrade=grade
            return outgrade

for id,score in members:
    print("%10s:%3d [%2s]" %(id,score,find_grade(score)))
