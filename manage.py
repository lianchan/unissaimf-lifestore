#!/usr/bin/env python
# -*- encoding:utf-8 -*- #utf-8编码
import os
import sys

if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mydetail.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "老表你还没安装Django扩展吧！"
        ) from exc
    execute_from_command_line(sys.argv)
