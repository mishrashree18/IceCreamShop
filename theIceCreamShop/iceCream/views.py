from django.shortcuts import render
from .forms import icecreamForm, MultiplePizzaForm
from django.forms import formset_factory
from .models import icecream

# Create your views here.
def home(request):
    return render(request, 'iceCream/home.html')

def order(request):
    multiple_form = MultiplePizzaForm()
    if request.method == 'POST':
        filled_form = icecreamForm(request.POST)
        if filled_form.is_valid():
            # created_icecream = filled_form.save()
            # created_pizza_pk = created_icecream.id
            note = 'Thanks For Ordering! Your %s flavoured %s ice cream with %s is on its way!' %(filled_form.cleaned_data['flavour1'], filled_form.cleaned_data['type'], filled_form.cleaned_data['additionals'],)
            new_form = icecreamForm()
            return render(request, 'iceCream/order.html', {'icecreamForm':new_form, 'note':note, 'multiple_form':multiple_form})
    else:
        form = icecreamForm()
        return render(request, 'iceCream/order.html', {'icecreamForm':form, 'multiple_form':multiple_form})


def icecreams(request):
    number_of_icecreams = 2
    filled_multiple = MultiplePizzaForm(request.GET)
    if filled_multiple.is_valid():
        number_of_icecreams = filled_multiple.cleaned_data['number']
    IcecreamFormSet = formset_factory(icecreamForm, extra = number_of_icecreams)
    formset = IcecreamFormSet()
    if request.method == 'POST':
        filled_formset = IcecreamFormSet(request.POST)
        if filled_formset.is_valid():
            for form in filled_formset:
                print(form.cleaned_data['flavour1'])
            note = 'Ordered'
        else:
            note = 'no'
        return render(request, 'iceCream/icecreams.html', {'note':note, 'formset':formset})
    else:
        return render(request, 'iceCream/icecreams.html', {'formset':formset})

# def edit_order(request, pk):
#     icecream = icecream.objects.get(pk=pk)
#     form = icecreamForm(instance=icecream)
#     if request.method == 'POST':
#         filled_form = icecreamForm(request.POST,instance=icecream)
#         if filled_form.is_valid():
#             filled_form.save()
#             form = filled_form
#     return render(request, 'iceCream/edit_order.html', {'pizzaform':form, 'icecream':icecream})
