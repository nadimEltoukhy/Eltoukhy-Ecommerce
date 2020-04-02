from django.shortcuts import render,redirect,get_object_or_404
from .category_create import categoryForm,productForm
from django.http import HttpResponseRedirect
from .models import products,categories,cart,checkout
from datetime import datetime
from django.contrib.auth.models import User
import re
from django.core.paginator import Paginator
from .users_form import userloginform,userregisterform
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib.auth import(

			authenticate,
			get_user_model,
			login,
			logout,

	)

@login_required(login_url='/login/')
def category_create(request):
	if request.user.is_superuser:



	
		form = categoryForm(request.POST or None,request.FILES or None)

		title ="Add Category"

		if form.is_valid():
			instance = form.save(commit=False)
			instance.save()
			return redirect("/products/")
		
		context ={

			"form":form,
			"title":title,
		}
		return render(request,"form.html",context)

	else:
		return redirect("/admin/")




@login_required(login_url='/login/')
def category_edit(request,id=None):
	

	if request.user.is_superuser:
		instance=get_object_or_404(categories,c_id=id)
		form = categoryForm(request.POST or None,request.FILES or None,instance=instance)
		
		title = "Edit Category"

		if form.is_valid():

			
			instances = form.save(commit=False)
			instances.save()
			return redirect("/admin/categories_list/")

		context ={

			"form":form,
			"title":title,
			"instance":instance
		}
		return render(request,"form.html",context)
	else:
		return redirect("/admin/")

@login_required(login_url='/login/')
def category_delete(request,id=None):
	instance=get_object_or_404(categories,c_id=id)
	instance.delete()
	return redirect("/admin/categories_list/")


@login_required(login_url='/login/')
def product_create(request):
	

	if request.user.is_superuser:
		form = productForm(request.POST or None,request.FILES or None)
		
		title = "Add Product"

		if form.is_valid() and request.user.is_superuser():

			
			instance = form.save(commit=False)
			instance.save()
			return redirect("/products/")

		context ={

			"form":form,
			"title":title,
		}
		return render(request,"form.html",context)
	else:
		return redirect("/admin/")

@login_required(login_url='/login/')
def product_edit(request,id=None):
	

	if request.user.is_superuser:
		instance=get_object_or_404(products,p_id=id)
		form = productForm(request.POST or None,request.FILES or None,instance=instance)
		
		title = "Edit Product"

		if form.is_valid():

			
			instances = form.save(commit=False)
			instances.save()
			return redirect("/admin/products_list/")

		context ={

			"form":form,
			"title":title,
			"instance":instance
		}
		return render(request,"form.html",context)
	else:
		return redirect("/admin/")

@login_required(login_url='/login/')
def product_delete(request,id=None):
	instance=get_object_or_404(products,p_id=id)
	instance.delete()
	return redirect("/admin/productslist/")


def products_list(request):
	queryset = products.objects.all()
	paginator = Paginator(queryset, 10)
	
	
	page_number = request.GET.get('page',1)
	page_obj = paginator.page(page_number)

	context = {


		"queryset":queryset,
		"page_obj":page_obj,

	}

	return render(request,"shop.html",context)


def product_details(request,id=None):
	latest=[]
	pro =products.objects.all().values()
	
	details = get_object_or_404(products,p_id=id)
	mystr = details.p_tags
	tagsList = re.sub("[^\w]", " ",  mystr).split()
	p_title = details.p_name
	pro_id = details.p_id
	rel_products = products.objects.filter(p_category=details.p_category).values()
	for i in range(0,len(pro)):
		latest.append(pro[i])

	
	
	
	context = {"details":details,"tagsList":tagsList,"rel_products":rel_products,"latest":latest,"title":p_title,"pro_id":pro_id,}
	return render(request,"single-product.html",context)


def category(request):

	queryset = categories.objects.all()
	context={


		"queryset":queryset,

	}


	return render(request,"category.html",context)


def categoryProducts(request,id=None):
	details = get_object_or_404(categories,c_id=id)
	title = details.c_name
	c_products = products.objects.filter(p_category=details.c_id).values()
	paginator = Paginator(c_products, 10)
	
	
	page_number = request.GET.get('page',1)
	page_obj = paginator.page(page_number)

	context ={

		"details":details,
		"c_products":c_products,
		"page_obj":page_obj,
		"title":title,

	}
	return render(request,"categoryProducts.html",context)

def login_view(request):
	title="Login"


	form = userloginform(request.POST or None)
	if form.is_valid():
		username=form.cleaned_data.get("username")
		password=form.cleaned_data.get("password")

		user = authenticate(username=username,password=password)
		login(request,user)
		x=request.user.id
		if user.is_superuser:
			return redirect("/dashboard/")

		else:
			return redirect("/products/")


	return render(request,"form.html",{"form":form,"title":title})



def logout_view(request):

	logout(request)

	return redirect("/")



def register_view(request):
	title="Signup"
	form = userregisterform(request.POST or None)

	if form.is_valid():

		user=form.save(commit=False)
		print("\n\n\n",request.user.is_authenticated(),"\n\n\n")
		username = form.cleaned_data.get('username')
		password=form.cleaned_data.get('password')
		user.set_password(password)
		user.save()
		new_user =authenticate(username=username,password=password)

		login(request,new_user)
		print("\n\n\n",request.user.is_authenticated(),"\n\n\n")
		
		return redirect("/products/")

	context ={

			"form":form,
			"title":title,


		}



	return render(request,"form.html",context)



@login_required(login_url='/login/')
def addcart_view(request,id=None):
	
	product = get_object_or_404(products,p_id=id)
	product_instance=products.objects.filter(p_id=id).values()
	carts=cart()
	carts.user=request.user
	carts.cart_products= product
	carts.save()
	
	
	

	
	return redirect("/mycart/")


@login_required(login_url='/login/')
def cart_view(request):
	cart_object = cart.objects.filter(user=request.user).values()
	
	pro=[]
	
	
	for dic in cart_object:
		dic['product']=products.objects.filter(p_id=dic['cart_products_id']).values()
		pro.append(dic)

	
	
	context = {


			"cart":pro,

	}
	
	

	
	return render(request,"cart.html",context)


@login_required(login_url='/login/')
def cart_delete(request,id=None):
	instance=get_object_or_404(cart,cart_id=id)
	instance.delete()
	return redirect("/mycart/")



@login_required(login_url='/login/')
def checkout_view(request):
	queryset=cart.objects.filter(user=request.user).values()
	queryset2=cart.objects.filter(user=request.user)
	cartcheck =[]
	checkproducts=[]
	check_dic={}
	for dic in queryset:
		dic['product']=products.objects.filter(p_id=dic['cart_products_id']).values()
		cartcheck.append(dic)


	for dic in queryset:
		dic['product']=products.objects.filter(p_id=dic['cart_products_id'])
		checkproducts.append(dic)

	


	check_dic['carts']=queryset2
	check_dic['products']=checkproducts
	if request.method =='POST':
		user = request.user
		first_name=request.POST.get('billing_first_name')
		last_name =request.POST.get('billing_last_name')
		fullname=first_name + " " + last_name
		address=request.POST.get('billing_address_1')
		email=request.POST.get('billing_email')
		phone= request.POST.get('billing_phone')

		for x in range(0,len(queryset2)):
			check = checkout()
			check.cart=queryset2[x]
			check.checkout_products=checkproducts[x]['product'][0]
			


			check.check_user=user
			check.u_name = fullname
			check.u_email=email
			check.u_number=phone
			check.u_address=address
			check.save()

		

		return redirect("/admin/")
	

	return render(request,"checkout.html")

@login_required(login_url='/login/')
def dashboard(request):
	if request.user.is_superuser:
		admin = request.user

		productcount=len(products.objects.all())
		categorycount=len(categories.objects.all())
		checkoutcount=len(checkout.objects.all())
		userscount=len(User.objects.all())

	else:
		return redirect("/admin/")

	context={

		"p":productcount,
		"c":categorycount,
		"ch":checkoutcount,
		"u":userscount,
		"admin":admin,

	}



	return render(request,"dashboard.html",context)


@login_required(login_url='/login/')
def adminProducts_list(request):
	if request.user.is_superuser:


		queryset=products.objects.all()

	else:
		return redirect("/admin/")

	context={

		"products":queryset,

	}


	return render(request,"productlist.html",context)
@login_required(login_url='/login/')
def adminCategories_list(request):
	if request.user.is_superuser:



		queryset=categories.objects.all()

	else:
		return redirect("/admin/")

	context={

		"categories":queryset,

	}


	return render(request,"categorylist.html",context)

@login_required(login_url='/login/')
def adminUsers_list(request):
	if request.user.is_superuser:


		queryset=User.objects.all()

	else:
		return redirect("/admin/")

	context={

		"users":queryset,

	}


	return render(request,"userslist.html",context)


@login_required(login_url='/login/')
def checkout_list(request):
	if request.user.is_superuser:


		queryset=checkout.objects.all()

	else:
		return redirect("/admin/")

	context={

		"checkouts":queryset,

	}


	return render(request,"checkoutlist.html",context)








	
	



	




	
	

# Create your views here.
