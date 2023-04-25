from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .models import MyText
from .forms import MyTextForm
from .services import main
from rest_framework.views import APIView
from my_app.serializers import MyTextSerializer
from rest_framework.response import Response

import nltk
from nltk import Tree

def index(request):
    my_obj = MyText.objects.last()
    context = {"paraphrase": main(my_obj.tree, my_obj.limit)}
    return render(request, 'my_app/base.html', context)


class PhraseCreateView(CreateView):
    model = MyText
    form_class = MyTextForm
    template_name = "my_app/intext.html"
    success_url = 'home'
    

class ParaphraseAPIView(APIView):
    serializer_class = MyTextSerializer
       
    def get(self, request):
        params = request.GET.dict()
        text = params.get('tree',"")
        my_tree = " ".join(nltk.Tree.fromstring(text).flatten())
        limit = params.get('limit', 20)
        res = list(main(my_tree, limit))
        return Response({'tree': res})
          
