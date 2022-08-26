
from xml.dom.expatbuilder import ElementInfo
from django.shortcuts import render
from distutils.log import info
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib import auth 
from .models import Student,Joined,Batch, Trainer
from datetime import date
def show(request):
    return render(request,'index.html')
def addstudent(request):
    username=request.POST['email']
    email=request.POST['email']
    fname=request.POST['fname']
    lname=request.POST['lname']
    password=request.POST['password']
    user=User.objects.create_user(username=username,first_name=fname,last_name=lname,email=email,password=password)
    user.save()
    s=Student()
    s.user=user
    s.name=fname
    s.mob=request.POST['mob']
    s.address=request.POST['address']
    s.course=request.POST['course']
    s.remarks=request.POST['remarks']
    s.edt=request.POST['edt']
    s.save()
    messages.info(request,'successfully added')
    return render(request,'index.html')
def showstudents(request):
    st=Student.objects.all()
    return render(request,'showstudents.html',{'st':st})
def updatestudent(request):
    id=request.POST['uid']
    s=Student.objects.filter(user_id=id).get()
    s.address=request.POST['address']
    s.mob=request.POST['mob']
    s.remarks=request.POST['remarks']
    s.course=request.POST['course']
    s.save()
    messages.info(request,'successfully updates')
    st=Student.objects.all()
    return render(request,'showstudents.html',{'st':st})
def searchstudent(request):
    if request.method=='POST':
        name=request.POST['name']
        course=request.POST['course']
        mob=request.POST['mob']
        fdt=request.POST['fdt']
        tdt=request.POST['tdt']
        st=Student.objects.all()
        if name!="" and name is not None:
            st=st.filter(name=name)
        if course!="" and course is not None:
            st=st.filter(course=course)
        if mob!="" and mob is not None:
            st=st.filter(mob=mob)
        if fdt!="" and fdt is not None:
            st=st.filter(edt__gte=fdt)
        if tdt!="" and tdt is not None:
             st=st.filter(edt__lte=tdt)
        
        return render(request,'showstudents.html',{'st':st})
    else: 
        return render(request,'searchstudent.html')
def joinstudent(request):
    if request.method=="POST":
        id=request.POST['student']
        student=Student.objects.filter(user_id=id).get()
        j=Joined()
        j.student=student
        j.joined_dt=request.POST['joined_dt']
        j.total=request.POST['total']
        j.first_ins=request.POST['first_ins']
        j.first_dt=request.POST['first_dt']
        j.last_ins=request.POST['last_ins']
        j.last_dt=request.POST['last_dt']
        j.duration=request.POST['duration']
        j.dues=request.POST['dues']
        j.save()
        messages.info(request,"successfully joined")
        return render (request,"showjoined.html")
    else:
        st=Student.objects.all()
        return render(request,'joinstudent.html',{'st':st})
def showjoined(request):
    jn=Joined.objects.all()
    return render(request,'showjoined.html',{'jn':jn})
def updatejoined(request):
    j=Joined()
    id=request.POST['uid']
    j=Joined.objects.filter(id=id).get()
    j.last_ins=request.POST['last_ins']
    j.last_dt=request.POST['last_dt']
    j.dues=request.POST['dues']
    j.save()
    messages.info(request,'successfully updated')
    jn=Joined.objects.all()
    return render(request,'showjoined.html',{'jn':jn,})
def searchjoined(request):
    if request.method=='POST':
        
        joined_dt=request.POST['joined_dt']
        total=request.POST['total']
        first_ins=request.POST['first_ins']
        first_dt=request.POST['first_dt']
        last_ins=request.POST['last_ins']
        last_dt=request.POST['last_dt']
        duration=request.POST['duration']
        dues=request.POST['dues']
        jn=Joined.objects.all()
       
        if joined_dt!="" and joined_dt is not None:
            jn=jn.filter(joined_dt=joined_dt)
        if total!="" and total is not None:
            jn=jn.filter(total=total)
        if first_ins!="" and first_ins is not None:
            jn=jn.filter(first_ins=first_ins)
        if first_dt!="" and first_dt is not None:
             jn=jn.filter(first_dt=first_dt)
        if last_ins!="" and last_ins is not None:
             jn=jn.filter(last_ins=last_ins)
        if last_dt!="" and last_dt is not None:
             jn=jn.filter(last_dt=last_dt)
        if duration!="" and duration is not None:
             jn=jn.filter(duration=duration)
        if dues=='No_Dues':
             jn=jn.filter(dues=0)
        elif dues=="Remaining_Dues":
             jn=jn.filter(dues__gte=1)       
        
        return render(request,'showjoined.html',{'jn':jn, })
    else: 
        return render(request,'searchjoined.html')

def addbatch(request):
    if request.method=="POST":
        id=request.POST['students']
        jn=Joined.objects.filter(id=id).get()
        b=Batch()
        b.start_dt=request.POST['start_dt']
        b.trainer=request.POST['trainer']
        b.bname=request.POST['bname']
        b.save()
        messages.info(request,"successfully added")
        return render (request,'showbatch.html')
    else:
        jn=Joined.objects.all()
        ba=Batch.objects.all()
        return render(request,'addbatch.html',{'ba':ba,'jn':jn}) 
def showbatch(request):
    ba=Batch.objects.all()
    jn=Joined.objects.all()
    return render(request,'showbatch.html',{'ba':ba,'jn':jn})
def updatebatch(request):
    b=Batch()
    b.id=request.POST['id']
    b.start_dt=request.POST['start_dt']
    b.trainer=request.POST['trainer']
    b.bname=request.POST['bname']
    b.save()
    students=request.POST.getlist('student')
    for id in students:
        j=Joined.objects.filter(id=id).get()
        b.students.add(j)
    messages.info(request,'successfully updated')
    jn=Joined.objects.all()
    ba=Batch.objects.all()
    return render(request,'showbatch.html',{'ba':ba,'jn':jn})
def searchbatch(request):
    if request.method=='POST':
        start_dt=request.POST['start_dt']
        trainer=request.POST['trainer']
        bname=request.POST['bname']
        ba=Batch.objects.all()
        if start_dt!="" and start_dt is not None:
            ba=ba.filter(start_dt=start_dt)
        if trainer!="" and trainer is not None:
            ba=ba.filter(trainer=trainer)
        if bname!="" and bname is not None:
            ba=ba.filter(bname=bname)
        return render(request,'showbatch.html',{'ba':ba })
    else: 
        return render(request,'searchbatch.html')

def addtrainer(request):
    if request.method=="POST":
        t=Trainer()
        t.tname=request.POST['tname']
        t.languages=request.POST['languages']
        t.sal=request.POST['sal']
        t.joined_dt=request.POST['joined_dt']
        t.timings=request.POST['timings']
        t.save()
        messages.info(request,"successfully added")
        return render (request,'showtrainer.html')
    else:
        tr=Trainer.objects.all()
        return render(request,'addtrainer.html',{'tr':tr}) 
def showtrainer(request):
    tr=Trainer.objects.all()
    return render(request,'showtrainer.html',{'tr':tr})
def searchtrainer(request):
    if request.method=='POST':
        tname=request.POST['tname']
        languages=request.POST['languages']
        sal=request.POST['sal']
        joined_dt=request.POST['joined_dt']
        timings=request.POST['timings']
        tr=Trainer.objects.all()
        if tname!="" and tname is not None:
            tr=tr.filter(tname=tname)
        if languages!="" and languages is not None:
            tr=tr.filter(languages=languages)
        if sal!="" and sal is not None:
            tr=tr.filter(sal=sal)
        if joined_dt!="" and joined_dt is not None:
            tr=tr.filter(joined_dt=joined_dt) 
        if timings!="" and timings is not None:
            tr=tr.filter(timings=timings)       
        return render(request,'showtrainer.html',{'tr':tr })
    else: 
        return render(request,'searchtrainer.html')
    
    
    
    
