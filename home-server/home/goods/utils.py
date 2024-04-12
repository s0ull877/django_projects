from django.contrib.postgres.search import SearchQuery, SearchRank, SearchVector

from goods.models import Products


def q_search(query:str):

    if query.isdigit() and len(query) <= 5:
        return Products.objects.filter(id=int(query))

    # add in installed apps 'django.contrib.postgre 
    vector = SearchVector("name", "description")
    query = SearchQuery(query)
    
    return Products.objects.annotate(rank=SearchRank(vector, query)).order_by('-rank')


# my search
# from django.db.models import Q

    # keyword = [word for word in query.split() if len(word) > 2]

    # q_obj = Q()

    # for token in keyword:

    #     q_obj |= Q(description__icontains=token)
    #     q_obj |= Q(name__icontains=token)


    # return Products.objects.filter(q_obj)
