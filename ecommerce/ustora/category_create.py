from django import forms 
from .models import categories,products
from datetime import datetime
class categoryForm(forms.ModelForm):
	class Meta:
		model = categories
		fields = [

			
			"c_name",
			"c_image",
			

		]
		labels ={


			"c_name":"Category Name",
			"c_image":"Category Image"
		}


class productForm(forms.ModelForm):
	class Meta:
		model = products
		

		fields =[

			"p_id",
			"p_name",
			"p_image",
			"p_desc",
			"p_quantity",
			"p_price",
			"p_tags",
			"p_discount",
			"p_category",

		]
		labels ={

			"p_name":"Product Name",
			"p_image":"Product Image",
			"p_desc":"Description",
			"p_quantity":"Quantity",
			"p_price":"Price",
			"p_tags":"Tags",
			"p_discount":"Discount",
			"p_category":"Category",


		}
