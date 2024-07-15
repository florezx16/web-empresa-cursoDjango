from .models import Link

def context_dict(request):
    link_info = {link.key:link.url for link in Link.objects.all()}
    return link_info