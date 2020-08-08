import http.client
import json

class MovieMiddleware:
    def __init__(self, get_response):
        self.get_responce = get_response
        con = http.client.HTTPSConnection("imdb8.p.rapidapi.com")
        headers = {
            "x-rapidapi-host": "imdb8.p.rapidapi.com",
            "x-rapidapi-key": "4422ecdd22msh0284eaac7d64721p1d830ejsn5fc033392fd1"
        }
        con.request("GET","/title/auto-complete?q=game%20of%20thr0", headers=headers)
        res = con.getresponse()
        data = res.read()
        x = data.decode("utf-8")
        dict_data = json.loads(x)
        json.dump(dict_data,open("app/raw/movies.json", "w"))

    def __call__(self,request, *args, **kwargs):
        response = self.get_responce(request)
        return response