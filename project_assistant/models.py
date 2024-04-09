from django.db import models

# Create your models here.
class logintable(models.Model):
    username=models.CharField(max_length=20)
    password=models.CharField(max_length=20)
    type=models.CharField(max_length=20)

class coursetable(models.Model):
    course = models.CharField(max_length=50)
    details = models.CharField(max_length=200)
    noofsem = models.CharField(max_length=20)

class studenttable(models.Model):
    LOGIN=models.ForeignKey(logintable,on_delete=models.CASCADE)
    RegisterNo=models.IntegerField()
    COURSE=models.ForeignKey(coursetable,on_delete=models.CASCADE)
    fname=models.CharField(max_length=50)
    lname=models.CharField(max_length=50)
    semester=models.IntegerField()
    dob=models.DateField()
    gender=models.CharField(max_length=100)
    place=models.CharField(max_length=50)
    post=models.CharField(max_length=50)
    pin=models.IntegerField()
    Phoneno=models.BigIntegerField()
    email=models.CharField(max_length=100)
    year=models.CharField(max_length=100)
    image=models.FileField()

class stafftable(models.Model):
     LOGIN = models.ForeignKey(logintable, on_delete=models.CASCADE)
     fname = models.CharField(max_length=50)
     lname = models.CharField(max_length=50)
     Phoneno = models.BigIntegerField()
     email=models.CharField(max_length=200)
     image = models.FileField()
     qualification = models.CharField(max_length=200)



class projectnotificationstable(models.Model):
    COURSE=models.ForeignKey(coursetable,on_delete=models.CASCADE)
    details=models.CharField(max_length=200)
    year=models.CharField(max_length=100)
    date=models.DateField()
    lastdate=models.DateField()

class datasettable(models.Model):
    area = models.CharField(max_length=50)
    keywords=models.CharField(max_length=100)


class topicstable(models.Model):
    STUDENT=models.ForeignKey(studenttable,on_delete=models.CASCADE)
    heading = models.CharField(max_length=50)
    file = models.FileField()
    date=models.DateField()
    status=models.CharField(max_length=100)
    staff=models.ForeignKey(stafftable,on_delete=models.CASCADE)

class chattable(models.Model):
    FROMID = models.ForeignKey(logintable, on_delete=models.CASCADE,related_name='ll')
    TOID=models.ForeignKey(logintable ,on_delete=models.CASCADE,related_name='jj')
    message=models.CharField(max_length=500)
    date=models.DateField()

class feedbacktable(models.Model):
    STUDENT = models.ForeignKey(studenttable, on_delete=models.CASCADE)
    feedback=models.CharField(max_length=500)
    date=models.DateField()

class complainttable(models.Model):
    STUDENT = models.ForeignKey(studenttable, on_delete=models.CASCADE)
    complaint=models.CharField(max_length=500)
    reply=models.CharField(max_length=500)
    date=models.DateField()

class intrestingareastable(models.Model):
    STAFF = models.ForeignKey(stafftable, on_delete=models.CASCADE)
    details=models.CharField(max_length=200)
















































