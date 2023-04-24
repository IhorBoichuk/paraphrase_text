from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .models import MyText
from .forms import MyTextForm
from .services import main
from rest_framework.views import APIView
from my_app.serializers import MyTextSerializer
from rest_framework.response import Response
import json
from rest_framework import status
from rest_framework import generics
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
    

class ParaphraseAPIView(generics.ListAPIView):
    
    serializer_class = MyTextSerializer
       
    def get(self, request):
        
        my_tree = nltk.Tree.fromstring(request.GET['tree'])
        try:
            limit = int(nltk.Tree.fromstring(request.GET['limit']))
        except:
            limit = 20

        text = " ".join(my_tree.flatten())

        res = list(main(text, limit))
        print(res)
        
        return Response({'tree': MyTextSerializer(res, many=True).data})
          
