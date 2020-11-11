from django.shortcuts import render
from django.http  import HttpResponse, JsonResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import  Ussd
from django.views.decorators.csrf import csrf_exempt
from .serializer import UssdSerializer
from rest_framework import status
from rest_framework import generics, mixins
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.
def welcome(request):
    # if request.method == 'GET':
            
    response = " Welcome \n"
    response += "1. Transfer Money \n"
    response += "2. Withdraw Money \n"
    response += "3. Deposit Money \n"
    response += "4. Account Balance \n"
    response += "00. End session"

    return HttpResponse(response)

@csrf_exempt
def ussd (request):
    # FreeFlow = "FB"
    if request.method == 'POST':
        # freeflow = request.headers.get('FB')
        msisdn = request.POST.get('msisdn')
        session_id = request.POST.get('session_id')
        newreq = request.POST.get('newreq')
        input = request.POST.get('input')
        # headers = request.headers['FreeFlow']= "FC"
        response = "1. My phone number is "+ str(msisdn) + "\n 2. My session id is " + str(session_id) + "\n 3. new request is " + str(newreq) + "\n 4. with input of " + str(input)
        return HttpResponse(response)
    # msg="1. My phone number is "+ str(msisdn) + "\n 2. My session id is " + str(session_id) + "\n 3. new request is " + str(newreq) + "\n 4. with input of " + str(input)
    # print(freeflow)
    # print(msg)


# print(msisdn, session_id)

    # return HttpResponse("{}".format(msg))
        # return HttpResponse.get(headers, alternate=None)

# class UssdList(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin, mixins.DestroyModelMixin):
#     queryset = Ussd.objects.all()
#     serializer_class = UssdSerializer
#     def get(self, request, *args, **kwargs):
#         headers = {'FreeFlow': "FC"}
#         return self.list( request, *args, **kwargs, headers = headers)

#     def post(self, request, *args, **kwargs):
#         headers = {'FreeFlow': "FC"}
        # user = request.user
        #request.data['created_by'] = str(user.id)
        # return self.create(request, *args, **kwargs, headers = headers)


    # def delete(self, request, *args, **kwargs):
    #     return self.destroy(request, *args, **kwargs)



class UssdList(APIView):
    def get(self, request, format=None):
        serializers = UssdSerializer(data=request.data)
        msisdn = request.data.get('msisdn')
        session_id = request.data.get('session_id')
        newreq = request.data.get('newreq')
        input = request.data.get('input')
        msg="1. My phone number is "+ str(msisdn) + "\n 2. My session id is " + str(session_id) + "\n 3. new request is " + str(newreq) + "\n 4 with input of " + str(input)
        # session_id =
        headers = {'FreeFlow': "FC"}
        if serializers.is_valid():
              # msg = my phone number is
            serializers.save()
            return Response({"{}".format(msg)}, headers = headers, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, headers = headers,status=status.HTTP_400_BAD_REQUEST)

    def post(self, request, format=None):
        serializers = UssdSerializer(data=request.data)
        msisdn = request.data.get('msisdn')
        session_id = request.data.get('session_id')
        newreq = request.data.get('newreq')
        input = request.data.get('input')
        msg="My phone number is "+ msisdn + ". My session id is " + session_id + ". new request is " + newreq + ". with input of " + input
        headers = {'FreeFlow': "FC"}
        if serializers.is_valid():
            # msg = my phone number is
            serializers.save()
            return Response({"{}".format(msg)},headers = headers, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, headers = headers,status=status.HTTP_400_BAD_REQUEST)