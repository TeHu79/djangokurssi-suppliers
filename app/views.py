from django.shortcuts import render

def landingview(request):
    return render(request, 'landingpage.html')

def productlistview(request):
    return render(request, 'productlist.html')

def supplierlistview(request):
    return render(request, 'supplierlist.html')

#def supplierlistview(request):
    #muuttuja = "Tämä on merkkijono"
    #context = {'x': muuttuja}
    #return render(request, 'supplierlist.html', context)
