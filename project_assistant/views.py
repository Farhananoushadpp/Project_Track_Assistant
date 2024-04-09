import json
from datetime import datetime

from django.core.files.storage import FileSystemStorage
from django.db.models import Q
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.
from project_assistant.models import *


def firstpg(request):
    return render(request,'login_index.html')

def login_post(request):
    username=request.POST['textfield']
    password=request.POST['textfield2']
    login_obj=logintable.objects.get(username=username,password=password)
    if login_obj.type=="admin":
        return HttpResponse('''<script>alert("admin_home");window.location="HODAdmin"</script>''')
    elif login_obj.type == "staff":
        request.session['lid']=login_obj.id
        return HttpResponse('''<script>alert("staff_home");window.location="staff"</script>''')

    else:
        return HttpResponse('''<script>alert("invalid");window.location="admin_home"</script>''')


def addstaff_post(request):
    fname=request.POST['textfield']
    lname=request.POST['textfield2']
    Phoneno=request.POST['textfield3']
    email=request.POST['textfield4']
    qualification=request.POST['textfield5']
    image=request.FILES['file']
    fs=FileSystemStorage()
    fp=fs.save(image.name,image)
    username=request.POST['textfield7']
    password=request.POST['textfield8']
    ob=logintable()
    ob.username=username
    ob.password=password
    ob.type="staff"
    ob.save()

    obb=stafftable()
    obb.fname=fname
    obb.LOGIN=ob
    obb.lname=lname
    obb.Phoneno=Phoneno
    obb.email=email
    obb.qualification=qualification
    obb.image=fp
    obb.save()
    return HttpResponse('''<script>alert("added succesfully");window.location="viewstaff"</script>''')


def addstudent_post(request):
    regno = request.POST['textfield']
    course = request.POST['textfield2']
    sem = request.POST['select']
    fname = request.POST['textfield4']
    lname = request.POST['textfield5']
    dob = request.POST['textfield6']
    gender = request.POST['radiobutton']
    place = request.POST['textfield8']
    post = request.POST['textfield9']
    pin = request.POST['textfield10']
    phoneno = request.POST['textfield11']
    email = request.POST['textfield12']
    year = request.POST['textfield13']
    image = request.FILES['file']

    fs=FileSystemStorage()
    fp=fs.save(image.name,image)

    username = request.POST['textfield14']
    password = request.POST['textfield15']

    ob = logintable()
    ob.username = username
    ob.password = password
    ob.type = "student"
    ob.save()

    obb = studenttable()
    obb.LOGIN=ob
    obb.RegisterNo=regno
    obb.COURSE=coursetable.objects.get(id=course)
    obb.semester=sem
    obb.fname = fname
    obb.lname = lname
    obb.dob=dob
    obb.gender=gender
    obb.place=place
    obb.post=post
    obb.pin=pin
    obb.Phoneno = phoneno
    obb.email = email
    obb.year=year
    obb.image = fp
    obb.save()
    return HttpResponse('''<script>alert("added succesfully");window.location="viewstudent"</script>''')


def addprojectnotifications_post(request):
    course=request.POST['select']
    details=request.POST['textfield2']
    year=request.POST['textfield3']
    date=request.POST['textfield4']
    lastdate=request.POST['textfield5']

    ob = projectnotificationstable()
    ob.COURSE=coursetable.objects.get(id=course)
    ob.details=details
    ob.year=year
    ob.date=date
    ob.lastdate=lastdate
    ob.save()
    return HttpResponse('''<script>alert("added succesfully");window.location="viewprojectnotifications"</script>''')

def adddataset(request):
    return render(request,"HOD-Admin/adddataset.html")

def adddataset_post(request):
    area=request.POST['textfield']
    keywords=request.POST['textfield2']

    ob = datasettable()
    ob.area=area
    ob.keywords=keywords
    ob.save()
    return HttpResponse('''<script>alert("added succesfully");window.location="mngdataset"</script>''')




def addcourse_post(request):
    course=request.POST['textfield']
    details=request.POST['textfield2']
    noofsem=request.POST['textfield3']


    ob=coursetable()
    ob.course=course
    ob.details=details
    ob.noofsem=noofsem
    ob.save()
    return HttpResponse('''<script>alert("added succesfully");window.location="viewcourse"</script>''')


def addintrestingareas_post(request):
    details=request.POST['textfield']

    ob=intrestingareastable()
    ob.details=details
    ob.STAFF=stafftable.objects.get(LOGIN__id=request.session['lid'])
    ob.save()
    return HttpResponse('''<script>alert("added succesfully");window.location="viewintrestingareas"</script>''')



def addcourse(request):
    return render(request,'HOD-Admin/addcourse.html')

def addprojectnotifications(request):
    ob=coursetable.objects.all()
    return render(request,'HOD-Admin/addprojectnotifications.html',{'val':ob})

def addstudent(request):
    ob=coursetable.objects.all()
    return render(request,'HOD-Admin/addstudent.html',{"val":ob})


def editdstudent(request,id):
    ob=coursetable.objects.all()
    ob1=studenttable.objects.get(id=id)
    request.session['kid']=id
    return render(request,'HOD-Admin/editstudent.html',{"val":ob,'vall':ob1,"dob":str(ob1.dob)})

def editstaff(request,id):
    ob=stafftable.objects.get(id=id)
    request.session['bid']=id
    return render(request,'HOD-Admin/editstaff.html',{"vall":ob})

def editcourse(request,id):
    ob=coursetable.objects.get(id=id)
    request.session['cid']=id
    return render(request,'HOD-Admin/editcourse.html',{"vall":ob})

def editprojectnotifications(request,id):
    ob1=coursetable.objects.all()
    ob=projectnotificationstable.objects.get(id=id)
    request.session['pid']=id
    return render(request,'HOD-Admin/editprojectnotifications.html',{"vall":ob,"val":ob1,"d":str(ob.date),"ldg":str(ob.lastdate)})

def editstudent_post(request):
    try:
        regno = request.POST['textfield']
        course = request.POST['textfield2']
        sem = request.POST['select']
        fname = request.POST['textfield4']
        lname = request.POST['textfield5']
        dob = request.POST['textfield6']
        gender = request.POST['radiobutton']
        place = request.POST['textfield8']
        post = request.POST['textfield9']
        pin = request.POST['textfield10']
        phoneno = request.POST['textfield11']
        email = request.POST['textfield12']
        year = request.POST['textfield13']
        image = request.FILES['file']

        fs=FileSystemStorage()
        fp=fs.save(image.name,image)

        obb = studenttable.objects.get(id= request.session['kid'])
        obb.RegisterNo=regno
        obb.COURSE=coursetable.objects.get(id=course)
        obb.semester=sem
        obb.fname = fname
        obb.lname = lname
        obb.dob=dob
        obb.gender=gender
        obb.place=place
        obb.post=post
        obb.pin=pin
        obb.Phoneno = phoneno
        obb.email = email
        obb.year=year
        obb.image = fp
        obb.save()
        return HttpResponse('''<script>alert("edited succesfully");window.location="viewstudent"</script>''')

    except:

        regno = request.POST['textfield']
        course = request.POST['textfield2']
        sem = request.POST['select']
        fname = request.POST['textfield4']
        lname = request.POST['textfield5']
        dob = request.POST['textfield6']
        gender = request.POST['radiobutton']
        place = request.POST['textfield8']
        post = request.POST['textfield9']
        pin = request.POST['textfield10']
        phoneno = request.POST['textfield11']
        email = request.POST['textfield12']
        year = request.POST['textfield13']

        obb = studenttable.objects.get(id=request.session['kid'])
        obb.RegisterNo = regno
        obb.COURSE = coursetable.objects.get(id=course)
        obb.semester = sem
        obb.fname = fname
        obb.lname = lname
        obb.dob = dob
        obb.gender = gender
        obb.place = place
        obb.post = post
        obb.pin = pin
        obb.Phoneno = phoneno
        obb.email = email
        obb.year = year
        obb.save()
        return HttpResponse('''<script>alert("edited succesfully");window.location="viewstaff"</script>''')



def editstaff_post(request):
    try:
        fname=request.POST['textfield']
        lname=request.POST['textfield2']
        Phoneno=request.POST['textfield3']
        email=request.POST['textfield4']
        qualification=request.POST['textfield5']
        image=request.FILES['file']
        fs=FileSystemStorage()
        fp=fs.save(image.name,image)


        obb=stafftable.objects.get(id=request.session['bid'])
        obb.fname=fname
        obb.lname=lname
        obb.Phoneno=Phoneno
        obb.email=email
        obb.qualification=qualification
        obb.image=fp
        obb.save()
        return HttpResponse('''<script>alert("edited succesfully");window.location="viewstaff"</script>''')
    except:
        fname = request.POST['textfield']
        lname = request.POST['textfield2']
        Phoneno = request.POST['textfield3']
        email = request.POST['textfield4']
        qualification = request.POST['textfield5']


        obb = stafftable.objects.get(id=request.session['bid'])
        obb.fname = fname
        obb.lname = lname
        obb.Phoneno = Phoneno
        obb.email = email
        obb.qualification = qualification
        obb.save()
        return HttpResponse('''<script>alert("edited succesfully");window.location="viewstaff"</script>''')


def editcourse_post(request):
    course=request.POST['textfield']
    details=request.POST['textfield2']
    noofsem=request.POST['textfield3']

    ob = coursetable.objects.get(id=request.session['cid'])

    ob.course=course
    ob.details=details
    ob.noofsem=noofsem
    ob.save()
    return HttpResponse('''<script>alert("edited succesfully");window.location="viewcourse"</script>''')




def editprojectnotifications_post(request):
    course=request.POST['select']
    details=request.POST['textfield2']
    year=request.POST['textfield3']
    date=request.POST['textfield4']
    lastdate=request.POST['textfield5']

    ob = projectnotificationstable.objects.get(id=request.session['pid'])

    ob.COURSE=coursetable.objects.get(id=course)
    ob.details=details
    ob.year=year
    ob.date=date
    ob.lastdate=lastdate
    ob.save()
    return HttpResponse('''<script>alert("edited succesfully");window.location="viewprojectnotifications"</script>''')



def HODAdmin(request):
    return render(request,'HOD-Admin/admin_index.html')

def insertstaff(request):
    return render(request,'HOD-Admin/insertstaff.html')

def mngdataset(request):
    ob=datasettable.objects.all()
    return render(request,'HOD-Admin/mng dataset.html',{"val":ob})


def viewcomplaintsendreply(request):
    ob=complainttable.objects.all()
    return render(request,'HOD-Admin/viewcomplaints&sendreply.html',{"val":ob})

def viewcourse(request):
    ob=coursetable.objects.all()
    return render(request,'HOD-Admin/viewcourse.html',{'val':ob})

def viewprojectnotifications(request):
    ob=projectnotificationstable.objects.all()
    return render(request,'HOD-Admin/viewprojectnotifications.html',{"val":ob})

def viewprojecttopics(request):
    ob=topicstable.objects.all()
    return render(request,'HOD-Admin/viewprojecttopics.html',{"val":ob})

def accept(request,id):
    ob=topicstable.objects.get(id=id)
    ob.status='accepted'
    ob.save()
    return HttpResponse('''<script>alert("Accepted succesfully");window.location="/viewprojecttopics"</script>''')

def reject(request,id):
    ob=topicstable.objects.get(id=id)
    ob.status='rejected'
    ob.save()
    return HttpResponse('''<script>alert("Rejected succesfully");window.location="/viewprojecttopics"</script>''')



def viewstaff(request):
    ob=stafftable.objects.all()
    return render(request,'HOD-Admin/viewstaff.html',{'val':ob})

def viewstaffsrch(request):
    name=request.POST['textfield']
    ob=stafftable.objects.filter(fname__icontains=name)
    return render(request,'HOD-Admin/viewstaff.html',{'val':ob})

def viewstudentsrch(request):
    name=request.POST['textfield']
    ob=studenttable.objects.filter(fname__icontains=name)
    return render(request,'HOD-Admin/viewstudent.html',{'val':ob})

def viewcoursesrch(request):
    name=request.POST['textfield']
    ob=coursetable.objects.filter(course__icontains=name)
    return render(request,'HOD-Admin/viewcourse.html',{'val':ob})

def viewprojectnotificationsrch(request):
    name=request.POST['textfield']
    ob=projectnotificationstable.objects.filter(date=name)
    return render(request,'HOD-Admin/viewprojectnotifications.html',{'val':ob})

def viewprojecttopicssrch(request):
    name=request.POST['textfield']
    ob=topicstable.objects.filter(heading__icontains=name)
    return render(request,'HOD-Admin/viewprojecttopics.html',{'val':ob})

def viewcomplaintsendreplysrch(request):
    name=request.POST['textfield']
    ob=complainttable.objects.filter(complaint__icontains=name)
    return render(request,'HOD-Admin/viewcomplaints&sendreply.html',{'val':ob})

def viewintrestingareasrch(request):
    name=request.POST['textfield']
    ob=intrestingareastable.objects.filter(details__icontains=name)
    return render(request,'staff/viewintrestingareas.html',{'val':ob})

def viewassignedtopicsrch(request):
    name=request.POST['textfield']
    ob=topicstable.objects.filter(STUDENT__fname__icontains=name)
    return render(request,'staff/viewassignedtopics.html',{'val':ob})








def deletestaff(request,id):
    ob=logintable.objects.get(id=id)
    ob.delete()
    return HttpResponse('''<script>alert("deleted succesfully");window.location="/viewstaff"</script>''')





def viewstudent(request):
    ob=studenttable.objects.all()
    return render(request,'HOD-Admin/viewstudent.html',{'val':ob})

def deletestudent(request,id):
    ob=logintable.objects.get(id=id)
    ob.delete()
    return HttpResponse('''<script>alert("deleted succesfully");window.location="/viewstudent"</script>''')

def deletecourse(request,id):
    ob=coursetable.objects.get(id=id)
    ob.delete()
    return HttpResponse('''<script>alert("deleted succesfully");window.location="/viewcourse"</script>''')

def deleteprojectnotifications(request,id):
    ob=projectnotificationstable.objects.get(id=id)
    ob.delete()
    return HttpResponse('''<script>alert("deleted succesfully");window.location="/viewprojectnotifications"</script>''')

def deleteviewintrestingareas(request,id):
    ob=intrestingareastable.objects.get(id=id)
    ob.delete()
    return HttpResponse('''<script>alert("deleted succesfully");window.location="/viewintrestingareas"</script>''')

def deletedataset(request,id):
    ob=datasettable.objects.get(id=id)
    ob.delete()
    return HttpResponse('''<script>alert("deleted succesfully");window.location="/mngdataset"</script>''')


def send_reply(request,id):
    ob=complainttable.objects.get(id=id)
    request.session['cid']=id
    return render(request,'HOD-Admin/sendreply.html',{'val':ob})


def add_reply_post(request):
    replys=request.POST['textfield']
    ob=complainttable.objects.get(id=request.session['cid'])
    ob.reply=replys
    ob.date=datetime.now()
    ob.save()
    return HttpResponse('''<script>alert("send succesfully");window.location="/viewcomplaintsendreply"</script>''')





def addintrestingareas(request):
    return render(request,'staff/addintrestingareas.html')

def staff(request):
    return render(request,'staff/staff.html')

def viewassignedtopics(request):
    ob=topicstable.objects.all()
    return render(request,'staff/viewassignedtopics.html',{"val":ob})

def viewintrestingareas(request):
    ob=intrestingareastable.objects.all()
    return render(request,'staff/viewintrestingareas.html',{"val":ob})


def viewprojectnotifications1(request):
    ob=projectnotificationstable.objects.all()
    return render(request,'staff/viewprojectnotifications.html',{"val":ob})


def student(request):
    return render(request,'student/Student.html')

def studentupload(request):
    return render(request,'upload.html')





def studentupload_post(request):
    cv=request.FILES['file']
    import base64
    timestr = datetime.now().strftime("%Y%m%d-%H%M%S")
    print(timestr)


    # a = base64.b64decode(cv)
    # fh = open(r"C:/Users/anton/Desktop/PROJECT FINAL/Career_Guidance_project\media\\" + timestr + ".pdf", "wb")
    path = timestr + ".pdf"
    fs=FileSystemStorage()
    fsave=fs.save(path,cv)
    # fh.write(a)
    # fh.close()
    # fn=FileSystemStorage()
    # fs=fn.save(cv.name,cv)
    save_image_path = './media/' + path
    resume_text = read_pdf(save_image_path).lower()

    print(resume_text)

    with open(r"C:\Users\hp\PycharmProjects\project_track_assistant\static\example.txt", "w",encoding="utf-8") as file:
        # Write the data to the file
        file.write(resume_text)
    print(resume_text)
    # res = predict(resume_text)
    # print(res,"=================================================")
    qus = resume_text.lower()
    vector1 = text_to_vector(qus)
    # cmd.execute("select Question,lid from dataset")
    # sss = cmd.fetchall()
    sss=datasettable.objects.all()
    print("s--", sss)
    res = []

    max_sim=0
    sid=0

    for d in sss:
        vector2 = text_to_vector(str(d.keywords).lower())
        cosine = get_cosine(vector1, vector2)
        if cosine>max_sim:
            max_sim=cosine
            sid=d.id
        print("cosine",cosine)

        res.append(cosine)
    print("========",sid)

    ob=datasettable.objects.get(id=sid)

    areob=intrestingareastable.objects.filter(details__contains=ob.area)
    data=[]
    for i in areob:
        row={"staff name":i.STAFF.fname+" "+i.STAFF.lname}

    data.append(row)




    return HttpResponse(data)

def read_pdf(file_path):
    import PyPDF2
    with open(file_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        num_pages = len(reader.pages)
        txt = ""
        for page_number in range(num_pages):
            page = reader.pages[page_number]
            text = page.extract_text()
            txt = txt + text + " "
        return txt

from collections import Counter
import re,math

WORD = re.compile(r'\w+')


def text_to_vector(text):
    words = WORD.findall(text)
    return Counter(words)

def get_cosine(vec1, vec2):
    intersection = set(vec1.keys()) & set(vec2.keys())
    numerator = sum([vec1[x] * vec2[x] for x in intersection])
    sum1 = sum([vec1[x] ** 2 for x in vec1.keys()])
    sum2 = sum([vec2[x] ** 2 for x in vec2.keys()])
    denominator = math.sqrt(sum1) * math.sqrt(sum2)

    if not denominator:
        return 0.0
    else:
        return float(numerator) / denominator


# ///////////////////////////////// webservice ////////////////////////////////////

def logincode(request):
    print(request.POST)
    un = request.POST['uname']
    pwd = request.POST['pass']
    print(un, pwd)
    try:
        users = logintable.objects.get(username=un, password=pwd)

        if users is None:
            data = {"task": "invalid"}
        else:
            print("in user function")
            data = {"task": "valid", "id": users.id}
        r = json.dumps(data)
        print(r)
        return HttpResponse(r)
    except:
        data = {"task": "invalid"}
        r = json.dumps(data)
        print(r)
        return HttpResponse(r)


def sendfeedback(request):
    lidd=request.POST['lid']
    feedbacks=request.POST['Feedback']
    feed=feedbacktable()
    date = datetime.today()
    feed.feedback=feedbacks
    feed.date=date
    feed.STUDENT=studenttable.objects.get(LOGIN__id=lidd)
    feed.save()
    data = {"task": "valid"}
    r = json.dumps(data)
    print(r)
    return HttpResponse(r)


def viewfeedback (request):
    lid=request.POST['lid']
    ob = feedbacktable.objects.filter(STUDENT__LOGIN=lid)
    data=[]
    for i in ob:
        row={"id":i.id,"date":i.date,"feedback":i.feedback}
        data.append(row)
    r=json.dumps(data)
    return HttpResponse(r)

def viewprevioustopics (request):
    lid=request.POST['lid']
    print(lid,"%%%")
    ob = topicstable.objects.filter(STUDENT__LOGIN__id=lid)
    data=[]
    for i in ob:
        row={"id":i.id,"date":str(i.date),"heading":i.heading,"file":i.file.url}
        data.append(row)
    r=json.dumps(data)
    print(r,'%%%%%%%%%%%%%%%%%%%')
    return HttpResponse(r)

def viewprojectnotificationss(request):
    idd=request.POST['id']
    ob = projectnotificationstable.objects.filter(COURSE__id=idd)
    data=[]
    for i in ob:
        row={"id":i.id,"date":str(i.date),"lastdate":str(i.lastdate),"details":i.details,"year":i.year}
        data.append(row)
    r=json.dumps(data)
    return HttpResponse(r)


def viewcourse1(request):
    lid=request.POST['lid']
    ob = studenttable.objects.filter(LOGIN__id=lid)
    data=[]
    for i in ob:
        row={"id":i.COURSE.id,"course":i.COURSE.course,"details":i.COURSE.details,"noofsem":i.COURSE.noofsem}
        data.append(row)
    r=json.dumps(data)
    return HttpResponse(r)

def viewstaff1(request):
    ob = stafftable.objects.all()
    data=[]
    for i in ob:
        row={"id":i.LOGIN.id,"name":i.fname+" "+i.lname,'image':i.image.url}
        data.append(row)
    r=json.dumps(data)
    return HttpResponse(r)

def viewtopicstatus (request):
    lid=request.POST['lid']
    ob = topicstable.objects.filter(STUDENT__LOGIN=lid)
    data=[]
    for i in ob:
        row={"id":i.id,"date":i.date,"heading":i.heading,"file":i.file,"status":i.status}
        data.append(row)
    r=json.dumps(data)
    return HttpResponse(r)


def sendcomplaint(request):
    lidd=request.POST['lid']
    complaintss=request.POST['complaint']
    complaint=complainttable()
    date = datetime.today()
    complaint.complaint=complaintss
    complaint.date=date
    complaint.reply="pending"
    complaint.STUDENT=studenttable.objects.get(LOGIN__id=lidd)
    complaint.save()
    data = {"task": "valid"}
    r = json.dumps(data)
    print(r)
    return HttpResponse(r)


def viewreply (request):
    lid=request.POST['lid']
    ob = complainttable.objects.filter(STUDENT__LOGIN=lid)
    data=[]
    for i in ob:
        row={"id":i.id,"date":str(i.date),"complaint":i.complaint,"reply":i.reply}
        data.append(row)
    r=json.dumps(data)
    return HttpResponse(r)




    # fs=FileSystemStorage()
    # fsave=fs.save(file.name,file)


    #____________________________________________________


    import base64
    timestr = datetime.now().strftime("%Y%m%d-%H%M%S")
    print(timestr)

    # a = base64.b64decode(cv)
    # fh = open(r"C:/Users/anton/Desktop/PROJECT FINAL/Career_Guidance_project\media\\" + timestr + ".pdf", "wb")
    path = timestr + ".pdf"
    fs = FileSystemStorage()
    fsave = fs.save(path, file)
    # fh.write(a)
    # fh.close()
    # fn=FileSystemStorage()
    # fs=fn.save(cv.name,cv)
    save_image_path = './media/' + path
    resume_text = read_pdf(save_image_path).lower()

    print(resume_text)

    with open(r"C:\Users\hp\PycharmProjects\project_track_assistant\static\example.txt", "w", encoding="utf-8") as file:
        # Write the data to the file
        file.write(resume_text)
    print(resume_text)
    # res = predict(resume_text)
    # print(res,"=================================================")
    qus = resume_text.lower()
    vector1 = text_to_vector(qus)
    # cmd.execute("select Question,lid from dataset")
    # sss = cmd.fetchall()
    sss = datasettable.objects.all()
    print("s--", sss)
    res = []

    max_sim = 0
    sid = 0

    for d in sss:
        vector2 = text_to_vector(str(d.keywords).lower())
        cosine = get_cosine(vector1, vector2)
        if cosine > max_sim:
            max_sim = cosine
            sid = d.id
        print("cosine", cosine)

        res.append(cosine)
    print("========", sid)

    ob = datasettable.objects.get(id=sid)

    areob = intrestingareastable.objects.filter(details__contains=ob.area)
    data = []
    for i in areob:
        row = {"staff name": i.STAFF.fname + " " + i.STAFF.lname}

    data.append(row)


    #________________________________________________________

def submittopic(request):
    lidd = request.POST['lid']
    heading = request.POST['heading']
    cv = request.FILES['file']
    import base64
    timestr = datetime.now().strftime("%Y%m%d-%H%M%S")
    print(timestr)

    # a = base64.b64decode(cv)
    # fh = open(r"C:/Users/anton/Desktop/PROJECT FINAL/Career_Guidance_project\media\\" + timestr + ".pdf", "wb")
    path = timestr + ".pdf"
    fs = FileSystemStorage()
    fsave = fs.save(path, cv)
    # fh.write(a)
    # fh.close()
    # fn=FileSystemStorage()
    # fs=fn.save(cv.name,cv)
    save_image_path = './media/' + path
    resume_text = read_pdf(save_image_path).lower()

    print(resume_text)

    with open(r"C:\Users\hp\PycharmProjects\project_track_assistant\static\example.txt", "w", encoding="utf-8") as file:
        # Write the data to the file
        file.write(resume_text)
    print(resume_text)
    # res = predict(resume_text)
    # print(res,"=================================================")
    qus = resume_text.lower()
    vector1 = text_to_vector(qus)
    # cmd.execute("select Question,lid from dataset")
    # sss = cmd.fetchall()
    sss = datasettable.objects.all()
    print("s--", sss)
    res = []

    max_sim = 0
    sid = 0

    for d in sss:
        vector2 = text_to_vector(str(d.keywords).lower())
        cosine = get_cosine(vector1, vector2)
        if cosine > max_sim:
            max_sim = cosine
            sid = d.id
        print("cosine", cosine)

        res.append(cosine)
    print("========", sid)

    ob = datasettable.objects.get(id=sid)

    areob = intrestingareastable.objects.filter(details__contains=ob.area)
    data = []
    for i in areob:
        row = {"staffname": i.STAFF.fname + " " + i.STAFF.lname,"sid":i.STAFF.id}

    data.append(row)




    submittopic = topicstable()
    submittopic.date = datetime.today()
    submittopic.heading =heading
    submittopic.file =fsave
    submittopic.STUDENT = studenttable.objects.get(LOGIN__id=lidd)
    submittopic.staff = areob[0].id
    submittopic.save()
    data = {"task": "success"}
    r = json.dumps(data)
    print(r)
    return HttpResponse(r)




#____________________WEB CHAT____________________________




def chatwithuser(request):
    ob = studenttable.objects.all()
    return render(request,"staff/fur_chat.html",{'val':ob})




def chatview(request):
    ob = studenttable.objects.all()
    d=[]
    for i in ob:
        r={"name":i.fname+" "+i.lname,'photo':i.image.url,'email':i.email,'loginid':i.LOGIN.id}
        d.append(r)
    return JsonResponse(d, safe=False)




def coun_insert_chat(request,msg,id):
    print("===",msg,id)
    ob=chattable()
    ob.FROMID=logintable.objects.get(id=request.session['lid'])
    ob.TOID=logintable.objects.get(id=id)
    ob.message=msg
    ob.date=datetime.now().strftime("%Y-%m-%d")
    ob.save()

    return JsonResponse({"task":"ok"})
    # refresh messages chatlist



def coun_msg(request,id):

    ob1=chattable.objects.filter(FROMID__id=id,TOID__id=request.session['lid'])
    ob2=chattable.objects.filter(FROMID__id=request.session['lid'],TOID__id=id)
    combined_chat = ob1.union(ob2)
    combined_chat=combined_chat.order_by('id')
    res=[]
    for i in combined_chat:
        res.append({"from_id":i.FROMID.id,"msg":i.message,"date":str(i.date),"chat_id":i.id})

    obu=studenttable.objects.get(LOGIN__id=id)


    return JsonResponse({"data":res,"name":obu.fname+" "+obu.lname,"photo":obu.image.url,"user_lid":obu.LOGIN.id})




def in_message2(request):
    print(request.POST)
    fromid = request.POST['fid']
    print("fromid",fromid)
    toid = request.POST['toid']
    print("toid",toid)

    message=request.POST['msg']
    ob=chattable()
    ob.FROMID=logintable.objects.get(id=fromid)
    ob.TOID=logintable.objects.get(id=toid)
    ob.message=message
    ob.date=datetime.today()
    # ob.time=datetime.datetime.now()
    ob.save()
    data = {"status": "send"}
    r = json.dumps(data)
    return HttpResponse(r)

#     # qry = "INSERT INTO `chat` VALUES(NULL,%s,%s,%s,CURDATE())"
#     # value = (fromid, toid, message)
#     # print("pppppppppppppppppp")
#     # print(value)
#     # iud(qry, value)
#     # return jsonify(status='send')
#
#
def view_message2(request):
    print(request.POST)
    fromid=request.POST['fid']
    toid=request.POST['toid']
    mid=request.POST['lastmsgid']
    print(mid,"jjjjjjjjjjj")
    ob1=chattable.objects.filter(FROMID__id=fromid,TOID__id=toid,id__gt=mid)
    ob2=chattable.objects.filter(FROMID__id=toid,TOID__id=fromid,id__gt=mid)
    ob=ob1.union(ob2)
    print(ob1)
    ob=ob.order_by("id")
    data=[]
    for i in ob:
        r={"msgid":i.id,"date":str(i.date),"message":i.message,"fromid":i.FROMID.id}
        data.append(r)
        print(data,"%%%%%%%%")
    if len(data)>0:
        return JsonResponse({"status":"ok","res1":data})

    else:
        return JsonResponse({"status":"no"})

