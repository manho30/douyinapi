'''
-*- encoding: utf-8 -*-
scraping the offcial website of DouYin and return in json format.
@author: manho
@time: 2020/06/03
@function: core of the program to scrap the offcial website of DouYin
'''

import requests
import json
import re

class Douyin:
    
    def __init__(self):
        self.headers = {
            'user-agent': 'Mozilla/5.0 (Linux; Android 8.0; Pixel 2 Build/OPD3.170816.012) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Mobile Safari/537.36 Edg/87.0.664.66'
        }
        
    
    def douyin(self, url):
        '''
        :description: get the json data by DouYin API.
        :param url: douyin video url
        :return json format
        '''
        try:
            
            # check is the url consist 'user'
            if 'user' in url:
                return {
                    'ok': False,
                    'status': '400',
                    'message': 'Batch parsing of homepage is not currently support yet.'
                }
            else:
                # original video url
                res = requests.get(url, headers=self.headers, allow_redirects=False)
                try:
                    # if there is a short url, then DOUYIN API will redirect to the url with video id.
                    vid_url = res.headers['Location']
                    
                    # check is the url consist 'user'
                    if 'user' in vid_url:
                        return {
                            'ok': False,
                            'status': '400',
                            'message': 'Batch parsing of homepage is not currently support yet.'
                        }
                except:
                    vid_url = url
                    
                '''
                get the video id
                # abit annoying, there is two type of url:
                # 1. https://www.douyin.com/video/123456789
                # 2. https://www.douyin.com/discover?modal_id=123456789
                '''
                try:
                    # the first type link.
                    
                    vid_id = re.findall('video/(\d+)?', vid_url)[0]
                    print('vid_id: ', vid_id)
                    
                except:
                    
                    vid_id = re.findall('modal_id=(\d+)', vid_url)[0]
                    print('vid_id: ', vid_id)
                
                # request to official DouYin API
                api = f'https://www.iesdouyin.com/web/api/v2/aweme/iteminfo/?item_ids={vid_id}'
                
                data = json.loads(((requests.get(api, headers=self.headers)).text))
                # check is the data consist of album
                if data['item_list'][0]['images'] is not None:
                    # handle the album
                    image = []
                    for i in data['item_list'][0]['images']:
                        image.append(i['url_list'][1])
                        
                    hashtag = []
                    for j in data['item_list'][0]['text_extra']:
                        hashtag.append(j['hashtag_name'])
                        
                    if data['item_list'][0]['music']['title']:
                        music = {
                            'title': str(data['item_list'][0]['music']['title']),
                            'url': str(data['item_list'][0]['music']['play_url']['url_list'][0]),
                            'author': str(data['item_list'][0]['music']['author']),
                            'duration': str(data['item_list'][0]['music']['duration'])
                        }
                    else:
                        music = {}
                    return {
                        'ok': True,
                        'status': '200',
                        'result': {
                            'author': {
                                'name': str(data['item_list'][0]['author']['nickname']),
                                'singnature': str(data['item_list'][0]['author']['signature']),
                                'avatar': str(data['item_list'][0]['author']['avatar_larger']['url_list'][0]),
                                'douyin_id': str(data['item_list'][0]['author']['unique_id'])
                            },
                            'album': {
                                'image_url': image,
                                'heigth': str(data['item_list'][0]['video']['height']),
                                'width': str(data['item_list'][0]['video']['width']),
                                'descriptions': str(data['item_list'][0]['desc']),
                            },
                            'statistics': {
                                'comment_count': str(data['item_list'][0]['statistics']['comment_count']),
                                'likes_count': str(data['item_list'][0]['statistics']['digg_count']),
                                'share_count': str(data['item_list'][0]['statistics']['share_count']),
                                'play_count': str(data['item_list'][0]['statistics']['play_count']),
                                'create_time': str(data['item_list'][0]['create_time']),
                                'hashtag': hashtag
                            },
                            'music': music,
                            'details': api
                        }
                    }
                else:
                    # handle the video
                    
                    hashtag = []
                    for j in data['item_list'][0]['text_extra']:
                        hashtag.append(j['hashtag_name'])
                    
                    vid_id = str(data['item_list'][0]['video']['vid'])
                    try:
                        r = requests.get("https://aweme.snssdk.com/aweme/v1/play/?video_id={}&radio=1080p&line=0".format(vid_id), headers=self.headers, allow_redirects=False)
                        free_watermark_1080p = r.headers['Location']
                    except:
                        free_watermark_1080p = "None"
                        
                    # original video with watermark
                    watermark = str(data['item_list'][0]['video']['play_addr']['url_list'][0])
                    
                    # water mark free video url
                    free_watermark = str(data['item_list'][0]['video']['play_addr']['url_list'][0]).replace('playwm', 'play')
                    
                    res = requests.get(url=free_watermark, headers=self.headers, allow_redirects=False)
                    free_watermark_720p = res.headers['Location']
                    
                    
                    if data['item_list'][0]['music']['title']:
                        music = {
                            'title': str(data['item_list'][0]['music']['title']),
                            'url': str(data['item_list'][0]['music']['play_url']['url_list'][0]),
                            'author': str(data['item_list'][0]['music']['author']),
                            'duration': str(data['item_list'][0]['music']['duration'])
                        }
                    else:
                        music = {}
                        
                    return {
                        'ok': True,
                        'status': '200',
                        'result': {
                            'author': {
                                'name': str(data['item_list'][0]['author']['nickname']),
                                'singnature': str(data['item_list'][0]['author']['signature']),
                                'avatar': str(data['item_list'][0]['author']['avatar_larger']['url_list'][0]),
                                'douyin_id': str(data['item_list'][0]['author']['unique_id'])
                            },
                            'video': {
                                'thumbnail_url': {
                                    'url_list': str(data['item_list'][0]['video']['cover']['url_list'][0]),
                                },
                                'video_url': {
                                    'watermark_url': watermark,
                                    'free_watermark_1080p': free_watermark_1080p,
                                    'free_watermark': free_watermark_720p,
                                },
                                'statistics': {
                                    'comment_count': str(data['item_list'][0]['statistics']['comment_count']),
                                    'likes_count': str(data['item_list'][0]['statistics']['digg_count']),
                                    'share_count': str(data['item_list'][0]['statistics']['share_count']),
                                    'play_count': str(data['item_list'][0]['statistics']['play_count']),
                                    'create_time': str(data['item_list'][0]['create_time']),
                                    'hashtag': hashtag
                                },
                                'descriptions': str(data['item_list'][0]['desc']),
                            },
                            'music': music,
                            'details': api
                        }
                    }
                    
        except Exception as e:
            return {
                'ok': False,
                'status': '500',
                'message': f'Internal server error. {e}'
            }
    def get_video(self, url):
        try:
            r = self.douyin(url)
            if r['ok']:
                return r['result']['video']['video_url']['free_watermark_1080p']
        except Exception as e:
            return {
                'ok': False,
                'status': '500',
                'message': f'Internal server error. {e}'
            }
# for debug only!

if __name__ == '__main__':
    douyin = Douyin()
    print(douyin.get_video("https://v.douyin.com/FEUgdxn/ "))
