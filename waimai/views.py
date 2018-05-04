from django.shortcuts import render

def home_page(request):

	if request.method == 'POST':
		food = request.POST.get('food')
		address= reqeust.POST.get('address')

		return render(reqeust,'waimai/home_page.html',{'food':fodd,'address':address})

	return render(request, 'waimai/home_page.html')
