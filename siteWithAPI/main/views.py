from http.client import responses

from django.shortcuts import render
from .api import API
from .c_serializer import Serializer

api = API("http://127.0.0.1:8080/api/")

# def index(request):
#     return render(request, 'main/index.html')

def index(request):
    e = api.set_query(
        ('id', ''),
        ('username', ''),
        ('uniq_key', ''),
        ('role', '0'),
        table='users',
        method='read',
    )
    if isinstance(e, dict):
        return render(request, 'main/index.html', {"response": e})
    # response = api.send_request()
    ser = Serializer()
    serialized_response = ser.unpack(api.send_request())
    return render(request, 'main/index.html', {"response": serialized_response.response})

# def test_create_api(request):
#     if request.method == "POST":
#         response = request.POST
#         if not response["table"] or not response["username"] or not response["uniq_key"]:
#             return render(request, 'main/test_create_api.html', {"err": "All fields must be filled in!"})
#         r = requests.get(f"http://127.0.0.1:8080/api/request?table={response['table']}&method=create&id=&username={response['username']}&uniq_key={response['uniq_key']}&role=0")
#         json_response = r.json()
#         return render(request, 'main/test_create_api.html', {"response": json_response})
#     return render(request, 'main/test_create_api.html')


