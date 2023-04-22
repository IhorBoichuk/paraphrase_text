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
       
    def post(self, request):
        data = (json.loads(request.body))
        serializer = MyTextSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            my_obj = MyText.objects.get(tree=data['tree'])
            return Response({
                'hash': MyTextSerializer(my_obj).data['tree'],
                'valid_to' : MyTextSerializer(my_obj).data['expires']
                })
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)    
