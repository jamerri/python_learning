# -*- coding: utf-8 -*-
# @Time : 2021/8/5 23:26
# @Author : Jamerri
# @File : 8-7.py


def make_album(singer_name, album_name, num=''):
    if num != '':
        name = {'singer': singer_name, 'album': album_name, 'songs_num': num}
    else:
        name = {'singer': singer_name, 'album': album_name}
    return name


music_name = make_album('Lin JJ', 'Ten years', 10)
print(music_name)
