# -*- coding: utf-8 -*-
# @Time : 2021/8/6 16:19
# @Author : Jamerri
# @File : 8-8.py


def make_album(singer_name, album_name, num=''):
    if num != '':
        name = {'singer': singer_name, 'album': album_name, 'songs_num': num}
    else:
        name = {'singer': singer_name, 'album': album_name}
    return name


while True:
    print("------Please input singer_name and album_name------")
    print("(ebter 'q' at any time to quit)")

    singer_name = input("singer_name is:")
    if singer_name == 'q':
        break

    album_name = input("album_name is:")
    if album_name == 'q':
        break

    music_name = make_album(singer_name, album_name)
    print(music_name)