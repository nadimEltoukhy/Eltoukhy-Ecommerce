from django.conf.urls import url
from .views import(

	category_create,
	product_create,
	products_list,
	product_details,
	category,
	categoryProducts,
	login_view,
	register_view,
	logout_view,
	addcart_view,
	cart_view,
	cart_delete,
	checkout_view,
	dashboard,
	adminProducts_list,
	product_delete,
	product_edit,
	category_edit,
	category_delete,
	adminCategories_list,
	adminUsers_list,
	checkout_list,

	)


urlpatterns=[


		url(r'^$',products_list),
		url(r'^add_category/$',category_create),
		url(r'^add_product/$',product_create ,name='add_product'),
		url(r'^products/$',products_list),
		url(r'^product_id/(?P<id>\d+)/$',product_details,name ='detail'),
		url(r'^category/$',category),
		url(r'^category_id/(?P<id>\d+)/$',categoryProducts,name ='category'),
		url(r'^login/$',login_view),
		url(r'^signup/$',register_view,name='register'),
		url(r'^logout/$',logout_view),
		url(r'^addcart/(?P<id>\d+)/$',addcart_view,name ='cart'),
		url(r'^mycart/',cart_view,name='mycart'),
		url(r'^cart_delete/(?P<id>\d+)/$',cart_delete,name='cart_delete'),
		url(r'^checkout/',checkout_view),
		url(r'^dashboard/',dashboard),
		url(r'^admin/productslist/',adminProducts_list),
		url(r'^product_delete/(?P<id>\d+)/$',product_delete,name='product_delete'),
		url(r'^product_edit/(?P<id>\d+)/$',product_edit,name='product_edit'),
		url(r'^category_delete/(?P<id>\d+)/$',category_delete,name='category_delete'),
		url(r'^category_edit/(?P<id>\d+)/$',category_edit,name='category_edit'),
		url(r'^admin/categorylist/',adminCategories_list),
		url(r'^admin/userslist/',adminUsers_list),
		url(r'^admin/checkoutslist/',checkout_list),

		









]

