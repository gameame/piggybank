from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from piggy.bank.models import MyPiggy
from django.utils.translation import ugettext_lazy as _
from django.template import RequestContext


def index(request, language_code):
    piggies = MyPiggy.objects.all()
    return render_to_response('index.html', {'piggies': piggies}, context_instance=RequestContext(request))

def detail(request, language_code, piggy_id):
    piggy = get_object_or_404(MyPiggy, pk=piggy_id)
    return render_to_response('detail.html', {'piggy': piggy}, context_instance=RequestContext(request))

def donate(request, language_code, piggy_id):
    piggy = get_object_or_404(MyPiggy, pk=piggy_id)
    try:
        coin_value = float(request.POST['coin_value'])
        # qua ci vanno dei controlli sul parametro (ad esempio che sia positivo)
    except:
        return render_to_response('detail.html', {
            'piggy': piggy,
            'error_message': _(u"oh oh"),
        }, context_instance=RequestContext(request))
    else:
        piggy.deposit = str(coin_value + float(piggy.deposit))
        piggy.save()
        return HttpResponseRedirect(reverse('piggy.bank.views.detail', args=(language_code, piggy.id)))
        # servirebbe magari una pagina di ringraziamento