from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import get_object_or_404, redirect, render
from .models import BuisnessStream, Company, CompanyImage
from django.views.decorators.csrf import csrf_exempt
# Create your views here.


def number_cmpy():
    try:
        no_of_compy = Company.objects.all()
    except(ObjectDoesNotExist):
        return None
    return no_of_compy.count()


@csrf_exempt
def create_comp(request):

    try:
        bus_obj = BuisnessStream.objects.all()
    except(ObjectDoesNotExist):
        bus_obj = None

    if request.method == "POST":
        stream_name = request.POST['b_stream']
        bus_obj = get_object_or_404(
            BuisnessStream, buisness_stream_name=stream_name)
        c_name = request.POST['c_name']
        c_descrip = request.POST['c_descrip']
        estab_date = request.POST['estab_date']
        company_website = request.POST['company_website']
        c_image = request.FILES.get('company_image')
        cmpy = Company(stream=bus_obj, name=c_name, prof_description=c_descrip,
                       estab_date=estab_date, company_website=company_website)

        cmpy.save()
        cmpy_img = CompanyImage(company=cmpy, image=c_image)
        cmpy_img.save()

        return redirect('./')

    return render(request, 'company/company_entry.html', context={
        'b_stream': bus_obj,
        'contxt': 'company_contxt'
    })
