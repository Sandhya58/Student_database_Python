def imply(lhs,rhs):
    return((not lhs) or rhs)

# student sat'd course prereq's with B or better

def studentGotAorB(ssn, dcode, cno, transcript):
    aOrB = list()
    for s in student:
        for t in transcript:
            if (t["ssn"] == s["ssn"] and t["grade"] == ("A" or "B")):
                aOrB.append(t)
    return(aOrB)

def studentSatCoursePrereqs(ssn,dcode,cno,univDB):

    prereqsSatisfied = "tbd"
    return(prereqsSatisfied)

def ha2(univDB):
    tables = univDB["tables"]
    department = tables["department"]
    course = tables["course"]
    prereq = tables["prereq"]
    class_ = tables["class"]
    faculty = tables["faculty"]
    student = tables["student"]
    enrollment = tables["enrollment"]
    transcript = tables["transcript"]

# boolean queries
    boolQuery_a = any([ (t["ssn"] == 82 and t["dcode"] == "CS" and t["cno"] == 530)
    for t in transcript])

    boolQuery_b = any([ (t["ssn"] == s["ssn"] and s["name"] == "John Smith" and t["dcode"] == "CS" and t["cno"] == 530)
    for s in student
        for t in transcript])


    boolQuery_c = all([
    any([t["ssn"] == s["ssn"] and t["dcode"] == "CS" and t["cno"] == 530 and s["name"] == "John Smith"
    for t in transcript])
    for s in student
        if s["name"] == "John Smith"])



    boolQuery_d = any([all([all([all([any([t["dcode"] == pq["pcode"] and t["cno"] == pq["pno"] and (t["grade"] == "A" or t["grade"] == "B") and t["ssn"] == s["ssn"]
    for t in transcript])
    for pq in prereq
    if pq["dcode"] == cl["dcode"] and pq["cno"] == cl["cno"]])
    for cl in class_
    if e["class"] == cl["class"]])
    for e in enrollment
    if s["ssn"] == e["ssn"]])
    for s in student
        if s["ssn"] == 82])


    boolQuery_e = all([all([all([all([any([t["dcode"] == pq["pcode"] and t["cno"] == pq["pno"] and (t["grade"] == "A" or t["grade"] == "B") and t["ssn"] == s["ssn"]
    for t in transcript])
    for pq in prereq
    if pq["dcode"] == cl["dcode"] and pq["cno"] == cl["cno"]])
    for cl in class_
    if e["class"] == cl["class"]])
    for e in enrollment
    if s["ssn"] == e["ssn"]])
    for s in student])


    boolQuery_f = all([all([all([all([any([t["dcode"] == pq["pcode"] and t["cno"] == pq["pno"] and (t["grade"] == "A" or t["grade"] == "B") and t["ssn"] == s["ssn"]
    for t in transcript])
    for pq in prereq
    if pq["dcode"] == cl["dcode"] and pq["cno"] == cl["cno"]])
    for cl in class_
    if e["class"] == cl["class"]])
    for e in enrollment
    if s["ssn"] == e["ssn"]])
    for s in student
    if s["major"] == "CS"])


    boolQuery_g = any([any([any([all([any([t["dcode"] == pq["pcode"] and t["cno"] == pq["pno"] and (t["grade"] == "A" or t["grade"] == "B") and t["ssn"] == s["ssn"]
    for t in transcript])
    for pq in prereq
    if pq["dcode"] == cl["dcode"] and pq["cno"] == cl["cno"]])
    for cl in class_
    if e["class"] == cl["class"]])
    for e in enrollment
    if s["ssn"] == e["ssn"]])
    for s in student
    if s["name"] == "John Smith"])




    boolQuery_h = any([all([co["dcode"] != pq["dcode"] and co["cno"] != pq["cno"]
    for pq in prereq])
    for co in course])


    boolQuery_i = all([any([cl["dcode"] == pq["dcode"] and cl["cno"] == pq["cno"]
    for pq in prereq])
    for cl in class_])


    boolQuery_j = any([all([(t["grade"] == "A" or t["grade"] == "B")
    for t in transcript
    if t["ssn"] == s["ssn"]])
    for s in student])


    boolQuery_k = all([all([all([any([ s["major"] == "CS" and s["ssn"] == en["ssn"]
    for s in student])
    for en in enrollment
    if cl["class"] == en["class"]])
    for cl in class_
    if f["ssn"] == cl["instr"]])
    for f in faculty
    if f["name"] == "Brodsky"])


    boolQuery_l = any([any([any([any([ s["major"] == "CS" and s["ssn"] == en["ssn"]
    for s in student])
    for en in enrollment
    if cl["class"] == en["class"]])
    for cl in class_
    if f["ssn"] == cl["instr"]])
    for f in faculty
    if f["name"] == "Brodsky"])


    dataQuery_a = [{"ssn": s["ssn"], "name": s["name"], "major": s["major"], "status": s["status"]}
            for s in student
            for t in transcript
                if any([t["ssn"] == s["ssn"] and t["dcode"] == "CS" and t["cno"] == 530])
                ]


    dataQuery_b = list()
    for t in transcript:
        for s in student:
            if all([t["ssn"] == s["ssn"] and t["dcode"] == "CS" and t["cno"] == 530 and s["name"] == "John"]):
                dataQuery_b.append(s)
                dataQuery_b.sort(key = lambda s: s["ssn"])



    dataQuery_c = [{ "ssn": s["ssn"], "name": s["name"], "major": s["major"], "status": s["status"]}
    for s in student
        if all([
                any([t["dcode"] == pq["pcode"]
                    and t["cno"] == pq["pno"]
                    and (t["grade"] == "A" or t["grade"] == "B")
                    and t["ssn"] == s["ssn"]
                for t in transcript
                ])
                for e in enrollment
                for cl in class_
                    for pq in prereq
                        if e["ssn"] == s["ssn"] and e["class"] == cl["class"] and cl["dcode"] == pq["dcode"] and cl["cno"] == pq["cno"]])]


    dataQuery_d = [{ "ssn": s["ssn"], "name": s["name"], "major": s["major"], "status": s["status"]}
        for s in student
            if not
                all([
                    any([t["dcode"] == pq["pcode"]
                        and t["cno"] == pq["pno"]
                        and (t["grade"] == "A" or t["grade"] == "B")
                        and t["ssn"] == s["ssn"]
                    for t in transcript
                    ])
                    for e in enrollment
                    for cl in class_
                        for pq in prereq
                            if e["ssn"] == s["ssn"] and e["class"] == cl["class"] and cl["dcode"] == pq["dcode"] and cl["cno"] == pq["cno"]])]



    dataQuery_e = [{ "ssn": s["ssn"], "name": s["name"], "major": s["major"], "status": s["status"]}
        for s in student
        if s["name"] == "John"
            if not
                all([
                    any([t["dcode"] == pq["pcode"]
                        and t["cno"] == pq["pno"]
                        and (t["grade"] == "A" or t["grade"] == "B")
                        and t["ssn"] == s["ssn"]
                    for t in transcript
                    ])
                    for e in enrollment
                    for cl in class_
                        for pq in prereq
                            if e["ssn"] == s["ssn"] and e["class"] == cl["class"] and cl["dcode"] == pq["dcode"] and cl["cno"] == pq["cno"]])]



    dataQuery_f = [{"dcode": co["dcode"], "cno": co["cno"]}
    for co in course
        if not(any([
                co["dcode"] == p["dcode"] and co["cno"] == p["cno"]
                for p in prereq
                ]))
    ]
    dataQuery_f.sort(key= lambda t: [t["dcode"], t["cno"]])

    dataQuery_g = [{"dcode": co["dcode"], "cno": co["cno"]}
    for co in course
    if any([
            co["dcode"] == p["dcode"] and co["cno"] == p["cno"]
            for p in prereq])]


    dataQuery_h = [{"class": cl["class"], "dcode": cl["dcode"], "cno": cl["cno"], "instr": cl["instr"]}
    for cl in class_
    if  any([
        cl["dcode"] == p["dcode"] and cl["cno"] == p["cno"]
        for p in prereq])]

    dataQuery_i = [{"ssn": s["ssn"], "name": s["name"], "major": s["major"], "status": s["status"]}
            for s in student
            if not(any([
                    t["ssn"] == s["ssn"] and (t["grade"] == "C" or t["grade"] == "F")
                    for t in transcript
                    ]))
    ]
    dataQuery_j = [{"ssn": s["ssn"], "name": s["name"], "major": s["major"], "status": s["status"]}
            for s in student
            if s["major"] == "CS"
            if any([
                    f["name"] == "Brodsky" and cl["instr"] == f["ssn"] and e["class"] == cl["class"] and e["ssn"] == s["ssn"]
                    for f in faculty
                    for cl in class_
                    for e in enrollment])
                    ]

    return({
        "boolQuery_a": boolQuery_a,
        "boolQuery_b": boolQuery_b,
        "boolQuery_c": boolQuery_c,
        "boolQuery_d": boolQuery_d,
        "boolQuery_e": boolQuery_e,
        "boolQuery_f": boolQuery_f,
        "boolQuery_g": boolQuery_g,
        "boolQuery_h": boolQuery_h,
        "boolQuery_i": boolQuery_i,
        "boolQuery_j": boolQuery_j,
        "boolQuery_k": boolQuery_k,
        "boolQuery_l": boolQuery_l,
        "dataQuery_a": dataQuery_a,
        "dataQuery_b": dataQuery_b,
        "dataQuery_c": dataQuery_c,
        "dataQuery_d": dataQuery_d,
        "dataQuery_e": dataQuery_e,
        "dataQuery_f": dataQuery_f,
        "dataQuery_g": dataQuery_g,
        "dataQuery_h": dataQuery_h,
        "dataQuery_i": dataQuery_i,
        "dataQuery_j": dataQuery_j
    })
