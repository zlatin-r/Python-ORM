 from django.core.paginator import Paginator

  # Paginate queryset with 10 objects per page
  paginator = Paginator(queryset, per_page=10)
  page_number = 2
  print([x for x in paginator.get_page(2)])
