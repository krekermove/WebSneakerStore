from django.shortcuts import redirect


def add_to_cart(request, id):
    if request.method == "POST":
        size = str(request.POST.get('size'))
        if size == "1":
            return redirect(request.POST.get('url_from'))

        if not request.session.get('cart'):
            request.session['cart'] = list()
        else:
            request.session['cart'] = list(request.session['cart'])

        cost = int(request.POST.get('cost')[:-3])

        item_exist = next((item for item in request.session['cart'] if item['size']==size and item['id']==id),False)
        data = {
            'id': id,
            'size': size,
            'cost': cost,
        }
        if not item_exist:
            request.session['cart'].append(data)
            request.session.modified = True
    return redirect(request.POST.get('url_from'))


def calc_total_price(request):
    return sum(request.session['cart']['cost'])


def remove_from_cart(request, id):
    if request.method == 'POST':
        size = str(request.POST.get('size'))
        for item in request.session['cart']:
            if item['id'] == id and size == item['size']:
                request.session['cart'].remove(item)

        if not request.session['cart']:
            del request.session['cart']

        request.session.modified = True
    return redirect(request.POST.get('url_from'))


def delete(request):
    if request.session['cart']:
        del request.session['cart']
    return redirect(request.POST.get('url_from'))
