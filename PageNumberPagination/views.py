from django.shortcuts import render
from rest_framework import generics
from .models import student
from . import serializers
from rest_framework.pagination import PageNumberPagination,LimitOffsetPagination,CursorPagination
# Create your views here.

class MyPageNumberPagination(PageNumberPagination):
    page_size=10
    page_query_param='p' #used to modify parameter in url 
    #http://127.0.0.1:8000/?page=1 ---> http://127.0.0.1:8000/?p=1

    page_size_query_param='records'
    #This is used to get no.of records,client wants to get
    #Ex: #http://127.0.0.1:8000/?records=100
    #Now each page will have 100 records..

    #if we gave the power to the client to to get as many
    #records as they want,someone may missuse the feature 
    #we can limit this by setting max_page_size attr
    max_page_size=100

    """we can get the last_page by using http://127.0.0.1:8000/?page=last
    if we want to change the last to something like end 
    we can do that by using last_page_strings attr
    """
    # last_page_strings='end'
    

class PageView(generics.ListAPIView):
    serializer_class=serializers.StudentSerializer
    queryset=student.objects.all()
    pagination_class=MyPageNumberPagination
    # PageNumberPagination.page_size=10


    # to set the page_size you need to 
    #create a class by extending PageNumebrPagination
    # and use that class as pagination_class 
    #instaed pagination_class=PageNumberPagination or else
    # PageNumberPagination.page_size=10


class MyLimitOffsetPagination(LimitOffsetPagination):
    default_limit=50 #same as pagesize
    limit_query_param='l'  #--> used to change query attr in url for limit
    """Making a request http://127.0.0.1:8000/2?offset=20&limit=30

    where offset=where to start the page ,
    limit=how many records to show in that page 

    """
    max_limit=50 #user can't access more than 50 records 
                 #even ih he used limit=100 only 50 will be displayed



class LimitOffsetView(generics.ListAPIView):
    serializer_class=serializers.StudentSerializer
    queryset=student.objects.all()
    pagination_class=MyLimitOffsetPagination
    

class CurserView(generics.ListAPIView):
    serializer_class=serializers.StudentSerializer
    queryset=student.objects.all()
    pagination_class=CursorPagination

    """by default the records orering will be based on a field 
    called created(it assumes that this field is there in the model you choose)
    if it is not there and you want to order according to the other fields 
    override the ordering in a new class or do like this """
    
    CursorPagination.ordering='id'
    
    
