from django.urls import path

from project_assistant import views

urlpatterns=[
    path('', views.firstpg, name='firstpg'),
    path('login_post', views.login_post, name='login_post'),
    path('HODAdmin', views.HODAdmin, name='HODAdmin'),

    path('addcourse',views.addcourse,name='addcourse'),
    path('addprojectnotifications', views.addprojectnotifications, name='addprojectnotifications'),
    path('addstudent', views.addstudent, name='addstudent'),
    path('HOD-Admin', views.HODAdmin, name='HODAdmin'),
    path('insertstaff', views.insertstaff, name='insertstaff'),
    path('viewcomplaintsendreply', views.viewcomplaintsendreply , name='viewcomplaintsendreply'),
    path('viewcourse', views.viewcourse, name='viewcourse'),
    path('viewcourse1', views.viewcourse1, name='viewcourse1'),
    path('viewstaff1', views.viewstaff1, name='viewstaff1'),
    path('viewprojectnotifications', views.viewprojectnotifications , name='viewprojectnotifications'),
    path('viewprojecttopics', views.viewprojecttopics , name='viewprojecttopics'),
    path('viewstaff', views.viewstaff, name='viewstaff'),
    path('viewstudent', views.viewstudent, name='viewstudent'),
    path('mngdataset', views.mngdataset, name='mngdataset'),
    path('adddataset', views.adddataset, name='adddataset'),
    path('deletedataset/<int:id>', views.deletedataset, name='deletedataset'),


path('chatwithuser', views.chatwithuser, name='chatwithuser'),
path('chatview', views.chatview, name='chatview'),
path('coun_msg/<int:id>', views.coun_msg, name='coun_msg'),
path('coun_insert_chat/<str:msg>/<int:id>', views.coun_insert_chat, name='coun_insert_chat'),



    path('view_message2', views.view_message2, name='view_message2'),
    path('in_message2', views.in_message2, name='in_message2'),
    path('add_reply_post', views.add_reply_post, name='add_reply_post'),
    path('adddataset_post', views.adddataset_post, name='adddataset_post'),
    path('viewstaffsrch', views.viewstaffsrch, name='viewstaffsrch'),
    path('viewstudentsrch', views.viewstudentsrch, name='viewstudentsrch'),
    path('viewcoursesrch', views.viewcoursesrch, name='viewcoursesrch'),
    path('viewprojectnotificationsrch', views.viewprojectnotificationsrch, name='viewprojectnotificationsrch'),
    path('viewprojecttopicssrch', views.viewprojecttopicssrch, name='viewprojecttopicssrch'),
    path('viewcomplaintsendreplysrch', views.viewcomplaintsendreplysrch, name='viewcomplaintsendreplysrch'),
    path('viewintrestingareasrch', views.viewintrestingareasrch, name='viewintrestingareasrch'),
    path('viewassignedtopicsrch', views.viewassignedtopicsrch, name='viewassignedtopicsrch  '),
    path('send_reply/<int:id>', views.send_reply, name='send_reply'),
    path('editstudent_post', views.editstudent_post, name='editstudent_post'),
    path('editstaff_post', views.editstaff_post, name='editstaff_post'),
    path('editcourse_post', views.editcourse_post, name='editcourse_post'),
    path('editprojectnotifications_post', views.editprojectnotifications_post, name='editprojectnotifications_post'),
    path('accept/<int:id>', views.accept, name='accept'),
    path('reject/<int:id>', views.reject, name='reject'),
    path('deletestaff/<int:id>', views.deletestaff, name='deletestaff'),
    path('deletestudent/<int:id>', views.deletestudent, name='deletestudent'),
    path('deletecourse/<int:id>', views.deletecourse, name='deletecourse'),
    path('deleteprojectnotifications/<int:id>', views.deleteprojectnotifications, name='deleteprojectnotifications'),
    path('deleteviewintrestingareas/<int:id>', views.deleteviewintrestingareas, name='deleteviewintrestingareas'),
    path('editdstudent/<int:id>', views.editdstudent, name='editdstudent'),
    path('editstaff/<int:id>', views.editstaff, name='editstaff'),
    path('editcourse/<int:id>', views.editcourse, name='editcourse'),
    path('editprojectnotifications/<int:id>', views.editprojectnotifications, name='editprojectnotifications'),

    path('addintrestingareas', views.addintrestingareas , name='addintrestingareas'),
    path('staff', views.staff , name='staff'),
    path('viewassignedtopics', views.viewassignedtopics , name='viewassignedtopics'),
    path('viewintrestingareas', views.viewintrestingareas , name='viewintrestingareas'),
    path('viewprojectnotificationss', views.viewprojectnotificationss , name='viewprojectnotificationss'),
    path('viewprojectnotifications1', views.viewprojectnotifications1 , name='viewprojectnotifications1'),
    path('Student', views.student , name='student'),


    path('addstaff_post', views.addstaff_post , name='addstaff_post'),
    path('addstudent_post', views.addstudent_post, name='addstudent_post'),
    path('addprojectnotifications_post', views.addprojectnotifications_post, name='addprojectnotifications_post'),
    path('addcourse_post', views.addcourse_post, name='addcourse_post'),
    path('addintrestingareas_post', views.addintrestingareas_post, name='addintrestingareas_post'),

    path('studentupload', views.studentupload, name='studentupload'),
    path('studentupload_post', views.studentupload_post, name='studentupload_post'),
    path('viewprevioustopics ', views.viewprevioustopics , name='viewprevioustopics '),

    path('logincode', views.logincode, name='logincode'),
    path('sendfeedback', views.sendfeedback, name='sendfeedback'),
    path('sendcomplaint', views.sendcomplaint, name='sendcomplaint'),
    path('submittopic', views.submittopic, name='submittopic'),
    path('viewprevioustopics', views.viewprevioustopics, name='viewprevioustopics'),
    path('viewtopicstatus', views.viewtopicstatus, name='viewtopicstatus'),
    path('viewreply', views.viewreply, name='viewreply'),
    path('viewfeedback', views.viewfeedback, name='viewfeedback'),

]