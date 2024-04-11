from django.db.models import Q

from goods.models import Products

def q_search(query:str):

    if query.isdigit() and len(query) <= 5:
        return Products.objects.filter(id=int(query))
    
    keyword = [word for word in query if len(word) > 2]

    q_obj = Q()

    for token in keyword:

        q_obj |= Q(description__icontains=token)
        q_obj |= Q(name__icontains=token)



    return Products.objects.filter(q_obj)