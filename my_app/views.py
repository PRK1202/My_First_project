import re
from django.db.models import manager
from django.http.response import JsonResponse
from django.shortcuts import redirect, render
from .models import *
from django.views.decorators.csrf import csrf_exempt
import json
# Create your views here.
def index(request):
	if 'email' in request.session:
		user_id = user.objects.get(email=request.session['email'])
		context={
			'hrcount':HR.objects.all().count(),
			'managercount':Manager.objects.all().count(),
			'developercount':Developer.objects.all().count(),
			'testercount':Tester.objects.all().count(),
		}
		
		if user_id.role=="Tester":
				tester_id = Tester.objects.get(user_id=user_id)
				context['user']=tester_id
				return render(request,'index.html',context)
		elif user_id.role=="Developer":
			developer_id = Developer.objects.get(user_id=user_id)
			context['user']=developer_id
			return render(request,'index.html',context)
		elif user_id.role=="HR":
			hr_id = HR.objects.get(user_id=user_id)
			context['user']=hr_id
			return render(request,'index.html',context)
		elif user_id.role=="Manager":
			Manager_id = Manager.objects.get(user_id=user_id)
			context['user']=Manager_id
			return render(request,'index.html',context)
	else:
		return render(request,'login.html')
def login(request):
	if request.method=="POST":
		email = request.POST['email']
		password = request.POST['password']
		user_id = user.objects.get(email=email)
		if user_id.password==password:
			request.session['email']=user_id.email
			if user_id.role=="Tester":
				tester_id = Tester.objects.get(user_id=user_id)
				return render(request,'index.html',{'user':tester_id})
			elif user_id.role=="Developer":
				developer_id = Developer.objects.get(user_id=user_id)
				return render(request,'index.html',{'user':developer_id})
			elif user_id.role=="HR":
				hr_id = HR.objects.get(user_id=user_id)
				return render(request,'index.html',{'user':hr_id})
			elif user_id.role=="Manager":
				Manager_id = Manager.objects.get(user_id=user_id)
				return render(request,'index.html',{'user':Manager_id})
		else:
			msg = "Please enter valid password"
			return render(request,'login.html',{'msg':msg})
	else:
		if 'email' in request.session:
			user_id = user.objects.get(email=request.session['email'])
			context={
			'hrcount':HR.objects.all().count(),
			'managercount':Manager.objects.all().count(),
			'developercount':Developer.objects.all().count(),
			'testercount':Tester.objects.all().count(),
			}
			if user_id.role=="Tester":
				tester_id = Tester.objects.get(user_id=user_id)
				return render(request,'index.html',{'user':tester_id})
			elif user_id.role=="Developer":
				developer_id = Developer.objects.get(user_id=user_id)
				return render(request,'index.html',{'user':developer_id})
			elif user_id.role=="HR":
				hr_id = HR.objects.get(user_id=user_id)
				return render(request,'index.html',{'user':hr_id})
			elif user_id.role=="Manager":
				Manager_id = Manager.objects.get(user_id=user_id)
				return render(request,'index.html',{'user':Manager_id})
		else:
			return render(request,'login.html')

def registration(request):
	if request.method=='POST':
		role=request.POST['role']
		fname=request.POST['tbfirstname']
		lname=request.POST['tblastname']
		email=request.POST['tbemail']
		password=request.POST['tbpassword']
		c_password=request.POST['tbconfirmpassword']
		if c_password == password:
			uid=user.objects.create(email=email,password=password,role=role)
			uid=user.objects.get(email=email)
			if role=="HR":
				hrid=HR.objects.create(user_id=uid,first_name=fname,last_name=lname)
			elif role=="Manager": 
				manager_id=Manager.objects.create(user_id=uid,first_name=fname,last_name=lname)
			elif role=="Tester": 
				tester_id=Tester.objects.create(user_id=uid,first_name=fname,last_name=lname)
			elif role=="Developer": 
				developer_id=Developer.objects.create(user_id=uid,first_name=fname,last_name=lname)
			return render(request,'login.html')
		else:
			msg="Password and confirm password must be same"
		return render(request,'registration.html',{'msg':msg})
	else:
		if 'email' in request.session:
			user_id = user.objects.get(email=request.session['email'])
			return render(request,'index.html',{'user':user_id})
		else:
			
			return render(request,'registration.html')
def logout(request):
	if 'email' in request.session:
		del request.session['email']
		return render(request,'login.html')
	else:
		return render(request,'login.html')
def profile(request):
	if 'email' in request.session:
		user_id = user.objects.get(email=request.session['email'])
		return render(request,'profile.html',{'user':user_id})
	else:
		return render(request,'login.html')
def edit_profile(request):
	if 'email' in request.session:
		if request.method=="POST":
			fname=request.POST['firstname']
			lname=request.POST['lastname']
			dob=request.POST['dob']
			gender=request.POST['gender']
			address=request.POST['address']
			state=request.POST['state']
			country=request.POST['country']
			pincode=request.POST['pincode']
			phnumber=request.POST['phone_number']
			
			user_id = user.objects.get(email=request.session['email'])
			if user_id.role=="Developer":
				Developer_id=Developer.objects.get(user_id=user_id)
				Developer_id.dob=dob
				Developer_id.gender=gender
				Developer_id.address=address
				Developer_id.state=state
				Developer_id.country=country
				Developer_id.pincode=pincode
				Developer_id.phone_number=phnumber
				Developer_id.save()
				return render(request,'profile.html',{'user':Developer_id})
			elif user_id.role=="Manager":
				manager_id=Manager.objects.get(user_id=user_id)
				manager_id.dob=dob
				manager_id.gender=gender
				manager_id.address=address
				manager_id.state=state
				manager_id.country=country
				manager_id.pincode=pincode
				manager_id.phone_number=phnumber
				manager_id.save()
				return render(request,'profile.html',{'user':manager_id})
			elif user_id.role=="HR":
				HR_id=HR.objects.get(user_id=user_id)
				HR_id.dob=dob
				HR_id.gender=gender
				HR_id.address=address
				HR_id.state=state
				HR_id.country=country
				HR_id.pincode=pincode
				HR_id.phone_number=phnumber
				HR_id.save()
				return render(request,'profile.html',{'user':HR_id})
			elif user_id.role=="Tester":
				Tester_id=Tester.objects.get(user_id=user_id)
				Tester_id.dob=dob
				Tester_id.gender=gender
				Tester_id.address=address
				Tester_id.state=state
				Tester_id.country=country
				Tester_id.pincode=pincode
				Tester_id.phone_number=phnumber
				Tester_id.save()
				return render(request,'profile.html',{'user':Tester_id})
		else:
			user_id = user.objects.get(email=request.session['email'])
			if user_id.role=="Manager":
				mid=Manager.objects.get(user_id=user_id)
				return render(request,'profile.html',{'user':mid})
			elif user_id.role=="Tester":
				tid=Tester.objects.get(user_id=user_id)
				return render(request,'profile.html',{'user':tid})
			elif user_id.role=="HR":
				hrid=HR.objects.get(user_id=user_id)
				return render(request,'profile.html',{'user':hrid})
			elif user_id.role=="Developer":
				did=Developer.objects.get(user_id=user_id)
				return render(request,'profile.html',{'user':did})
	else:
		return render(request,'login.html')

def allemployees(request):
	if 'email' in request.session:
		user_id=user.objects.get(email=request.session['email'])
		all_hr=HR.objects.all()
		all_manager=Manager.objects.all()
		all_testers=Tester.objects.all()
		all_developers=Developer.objects.all()
		context={
			'testers':all_testers,
			'developers':all_developers,
			'managers':all_manager,
			'hr':all_hr,
		}
		if user_id.role=="Tester":
				tester_id = Tester.objects.get(user_id=user_id)
				context['user']=tester_id
				return render(request,'allemployees.html',context)
		elif user_id.role=="Developer":
			developer_id = Developer.objects.get(user_id=user_id)
			context['user']=developer_id
			return render(request,'allemployees.html',context)
		elif user_id.role=="HR":
			hr_id = HR.objects.get(user_id=user_id)
			context['user']=hr_id
			return render(request,'allemployees.html',context)
		elif user_id.role=="Manager":
			Manager_id = Manager.objects.get(user_id=user_id)
			context['user']=Manager_id
			return render(request,'allemployees.html',context)
	else:
		return render(request,'login.html')
def check_email(request):
	if 'POST' in request.method:
		email=request.POST['email']
		uid=user.objects.filter(email=email)
		if uid:
			status="Email found"
			JsonResponse({'status':status})
		else:
			status="Email not found"
			JsonResponse({'status':status})
	else:
		return redirect('/login')