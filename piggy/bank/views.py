from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from piggy.bank.models import MyPiggy

def index(request):
    piggies = MyPiggy.objects.all()
    return render_to_response('piggy/index.html', {'piggies': piggies})

def detail(request, piggy_id):
    piggy = get_object_or_404(MyPiggy, pk=piggy_id)
    return render_to_response('piggy/detail.html', {'piggy': piggy})

def donate(request, piggy_id):
    piggy = get_object_or_404(MyPiggy, pk=piggy_id)
    try:
        coin_value = float(request.POST['coin_value']);
        # qua ci vanno dei controlli sul parametro (ad esempio che sia positivo)
    except:
        return render_to_response('piggy/detail.html', {
            'piggy': piggy,
            'error_message': "oh oh",
        })
    else:
        piggy.deposit = str(coin_value + float(piggy.deposit))
        piggy.save()
        return HttpResponseRedirect(reverse('piggy.bank.views.detail', args=(piggy.id,)))
        # servirebbe magari una pagina di ringraziamento