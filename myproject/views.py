from django.shortcuts import render

def custom_404_view(request, exception):
    return render(request, '404.html', status=404) #why status 404 needed here , because we have to tell in http response as 404 page not found otherwise it should return like 200 success like that 
