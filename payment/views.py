from django.http import JsonResponse
from payment.models import Payment


def save_payment(request):
    if request.method == 'POST':
        keys_to_delete = ['error_msg', 'pg_type', 'csrfmiddlewaretoken', 'buyer_tel', 'buyer_addr', 'buyer_postcode',
                          'bank_name', 'card_quota', 'currency', 'custom_data']
        converted_dict = {k: v for k, v in request.POST.items() if k not in keys_to_delete}
        converted_dict['user'] = request.user
        new_payment = Payment(**converted_dict)
        new_payment.save()
        return JsonResponse({'status': 'saved'})
    return JsonResponse({'status': 'fail'})
