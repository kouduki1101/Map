import os
import tempfile
import webbrowser
import pandas as pd
import numpy as np

import folium as folium

from django.shortcuts import render, redirect
from django.views import View

import requests
from bs4 import BeautifulSoup
import time



URL = 'http://www.geocoding.jp/api/'

my_data = dict()

i = 0


class SearchView(View):

    def get(self, request, *args, **kwargs):
        context = {

        }
        return render(request, 'search.html', context)

    def post(self, request, *args, **kwargs):

        name = request.POST['name']
        address = request.POST['address']
        add = name + '' + address
        # address = request.POST['address']

        url = 'http://www.geocoding.jp/api/'

        payload = {"v": 1.1, 'q': add}
        r = requests.get(url, params=payload)
        ret = BeautifulSoup(r.content, 'lxml')

        if ret.find('error'):
            raise ValueError(f"Invalid address submitted. {add}")
        else:
            lat = ret.find('lat').string
            lon = ret.find('lng').string
            time.sleep(10)

        context = {

            'name': request.POST['name'],
            'address': request.POST['address'],
            'lat': float(lat),
            'lon': float(lon),
        }

        global i
        my_data[i] = context

        i += 1

        map_osm = fmap(location=[lat, lon], zoom_start=18)

        j = 0



        for data1 in my_data.values():

            marker = folium.Marker(
                [data1.get("lat"), data1.get("lon")], tooltip=data1.get("name") + "<br/>" + data1.get("address")).add_to(
                map_osm)
            map_osm.add_child(marker)

        fmap.show(map_osm)

        # return render(request, 'list.html', context)
        return render(request, 'search.html', context)



search = SearchView.as_view()


class fmap(folium.Map):

    def __init__(self, **kw):
        super().__init__(**kw)
        self.listtf = list()

    def show(map_osm):
        tf = tempfile.NamedTemporaryFile(suffix='.html', delete=False)
        map_osm.save(tf)
        webbrowser.open(tf.name)

        # self.listtf.append(tf)

    def __del__(self):
        list(map(lambda tf: os.remove(tf.name), self.listtf))




