from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.template.response import TemplateResponse

from wagtail.core.models import Page
from wagtail.search.models import Query

from documents.models import DocumentPage


def search(request):
    search_query = request.GET.get('query', '')
    page = request.GET.get('page', 1)

    # Search
    search_results = DocumentPage.objects.live()
    if search_query:
        search_results = search_results.search(search_query, order_by_relevance=False)
        query = Query.get(search_query)

        # Record hit
        query.add_hit()
    # else:
        # search_results = Page.objects.none()
        

    # Pagination
    count_results = search_results.count
    paginator = Paginator(search_results, 10)
    try:
        search_results = paginator.page(page)
    except PageNotAnInteger:
        search_results = paginator.page(1)
    except EmptyPage:
        search_results = paginator.page(paginator.num_pages)

    return TemplateResponse(request, 'search/search.html', {
        'search_query': search_query,
        'search_results': search_results,
        'count_results': count_results,
    })
