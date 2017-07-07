from django.template.loader import get_template
from django.http import HttpResponse

def charpage(request):
    template = get_template("char.html")
    html = template.render()
    return HttpResponse(html)
