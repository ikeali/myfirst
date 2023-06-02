from django.shortcuts import render,redirect
# from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login
from .models import*
from .forms import*
from datetime import date

# Create your views here.
def home(request):
    return render(request, 'index.html')


def user_login(request):
    if request.method== 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request,user)
            messages.success(request, 'you are now signed in')
            return redirect('user_homepage')
        else:
            messages.info(request, 'username/password is not correct')
            return redirect('user_login')
        
    return render(request,'user_login.html')

            

def signup(request):
    customer = CustomerForm()
    if request.method == 'POST':
        contact_number = request.POST['contact_number']    
        gender = request.POST['gender'] 
        # male = request.POST['male']   
        # female = request.POST['female']   
        profile_picture = request.POST['profile_picture'] 
        customer = CustomerForm(request.POST)
        if customer.is_valid():
            user = customer.save()
            newuser = Applicant()   
            newuser.user = user 
            newuser.username =user.username                        
            newuser.first_name =user.first_name                         
            newuser.last_name =user.last_name  
            newuser.email =user.email   
            newuser.contact_number =contact_number 
            # newuser.male =male
            # newuser.female =female
            newuser.profile_picture = profile_picture
            newuser.save() 
            messages.success(request,f'dear {user} your account is created successfully')
            return redirect('home')
        else:
            messages.error(request, customer.errors)
            return redirect('signup')
    
    return render(request, 'signup.html') 


def user_homepage(request):
    if request.method== 'POST':
        applicant = Applicant.objects.get(user=request.user)
        email = request.POST['email']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        phone = request.POST['phone']
        # gender = request.POST['gender']
        
        applicant.user.email =email
        applicant.user.first_name= first_name
        applicant.user.last_name = last_name
        applicant.user.phone = phone
        # applicant.user.gender =gender
        applicant.save()
        applicant.user.save()

        try:
            image= request.FILE['image']
            applicant.image = image
            applicant.save()
        except:
            pass
        alert =True

    return render (request, 'user_homepage.html')
       
    # return render(request, 'user_homepage.html')   


def all_jobs(request):
    jobs = Job.objects.all().order_by ('start_date')
    # applicant = Applicant.objects.get(user=request.user)
    # apply = Application.objects.filter(applicant=applicant)
    # data = ['']

    # for i in apply:
    #     data.append(i.job.id)


    return render(request,'all_jobs.html', {'jobs':jobs})
    # return render(request,'all_jobs.html', {'jobs':jobs, 'apply':apply})


def job_detail(request,id):
    job = Job.objects.get(pk=id)

    context = {
        'job':job,
       
    }
    return render(request,'job_detail.html', context)


def job_apply(request, myid):
    applicant = Applicant.objects.get(user=request.user)
    job = Job.objects.get(id= myid)
    date1 = date.today()

    if job.end_date < date1:
        closed =True

        return render (request, 'job_apply.html',{'closed':closed})
    
    elif job.start_date > date1:
        notopen =True
        return render (request, 'job_apply.html',{'notopen':notopen})
        

    else:
        if request.method =='POST':
            resume = request.FILES['resume'] 
            Application.objects.create(job=job,company =job.company,applicant =applicant, resume=resume,apply_date=date.today())
            alert = True
            return render(request, 'job_apply.html', {'alert':alert})
            
    return render(request, 'job_apply.html', {'job':job})

        





