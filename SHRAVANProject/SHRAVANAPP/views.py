from django.shortcuts import render
from django.http import HttpResponse;
def display(request): #view-function
    
    ss='''		
        <center>
        <h2 style="color:blue;background-color:yellow;">
        ***Hello KASULA SHRAVANKUMAR, Welcome to Django SHRAVANPROJECT-SHRAVANAPP***
        </h2>
        <hr />
        </center>
    ''';
    return HttpResponse(ss);
    
    
    
def show(request):
	ss = '''
	HTML Webpage to display 'Welcome-Message' with different Headings 
	(D:\DJANGO\SHRAVANProject\html\welcome.html)
        '''


	return render(request,'html/welcome.html'); 

print("welcome/url is requested and display() is executed");    
        
    
