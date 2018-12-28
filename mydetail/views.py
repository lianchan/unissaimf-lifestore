#!/bin/bash
# -*- encoding:utf-8 -*-
import json;

from django.http import HttpResponse

from common.Tools import generate_token

KEY_STR = 'STR';


def index(self):
    token = generate_token(KEY_STR);
    #print("token is " + token);
    return HttpResponse(token)


def say(request):
    name = request.GET.get('name', '');
    _data = {
        "code": 255,
        "message": "获取数据成功",
        "data": [
            ("pig", "dog"),
            ["1", 2, "get"],
            {"user": name},
            {
                "token": token()
            }
        ]
    };
    return HttpResponse(json.dumps(_data, ensure_ascii=False))


def token():
    token = generate_token(3600);
    print(token);
