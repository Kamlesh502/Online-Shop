from django.http import JsonResponse

# Create your views here.
def home(request):
    return JsonResponse({'info':'Django app','name':'Kamlesh Store'})
