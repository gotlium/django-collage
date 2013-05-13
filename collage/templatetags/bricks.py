# -*- coding: utf-8 -*-

from PIL import Image

from sorl.thumbnail import get_thumbnail
from django.conf import settings
from settings import *


class Collage(object):

    def __init__(self):
        self.height = IMAGE_HEIGHT
        self.margin = MARGIN
        self.maxInRow = MAX_IN_ROW
        self.rowWidth = ROW_WIDTH
        self.sizes = []

        self.cnt = 0
        self.rowI = []

    def _init(self, images):
        self.images = images
        self.count = len(images)
        for image in self.images:
            try:
                image = '%s/%s' % (settings.MEDIA_ROOT, image)
                self.sizes.append(Image.open(image).size)
            except IOError:
                pass

    def run(self, images):
        self._init(images)
        if len(self.sizes) == len(images):
            self._scan()
            return self._process()

    def _scan(self):
        h = self.height
        wcTemp = 0
        tCnt = 0
        for i in range(self.cnt, self.count):
            b = 1
            wTemp = (h * self.sizes[i][0] / self.sizes[i][1]) + self.margin * 2
            if (wcTemp + wTemp) < self.rowWidth:
                wcTemp += wTemp
                self.cnt += 1
                tCnt += 1
                if tCnt == self.maxInRow:
                    if i == (self.count - 2):
                        self.cnt += 1
                        tCnt += 1
                    self.rowI.append([tCnt, b])
                    return self._scan()
            else:
                if i == (self.count - 1):
                    self.cnt += 1
                    tCnt += 1
                    b = -1
                self.rowI.append([tCnt, b])
                return self._scan()
            if i == (self.count - 1):
                self.rowI.append([tCnt, b])

    def __getW(self, b, e, n):
        h = self.height

        def gw(h):
            ww = 0
            for i in range(b, b + e):
                ww += h * self.sizes[i][0] / self.sizes[i][1]

            if n > 0:
                if ww < self.rowWidth - e * self.margin * 2:
                    h += 1
                    return gw(h)
                else:
                    h -= 1
                    return h
            else:
                if ww > self.rowWidth - e * self.margin * 2:
                    h -= 1
                    return gw(h)
                else:
                    h -= 1
                    return h

        h = gw(h)
        return h

    def _data(self, src, d):
        img = get_thumbnail(
            src, '%(width)dx%(height)d' % d, crop='center', quality=90)
        d['height'] = '%dpx' % d['height']
        d['width'] = '%dpx' % d['width']
        o = type('lamdbaobject', (object,), {})()
        o.url = img.url
        o.src = '%s%s' % (settings.MEDIA_URL, src)
        o.css = '; '.join(['%s: %s' % (str(k), str(v)) for k, v in d.items()])
        return o

    def _process(self, cnt=0, cnt1=0):
        configs = []
        for index, data in enumerate(self.rowI):
            a, b = data
            item = self.__getW(cnt1, a, b)
            cnt1 += a
            for i in range(cnt, self.rowI[index][0] + cnt):
                configs.append(self._data(
                    self.images[i], {
                        'height': item,
                        'width': item * self.sizes[i][0] / self.sizes[i][1],
                        'margin': '%dpx' % self.margin,
                        'display': 'block',
                        'float': 'left'
                    }
                ))

            cnt += self.rowI[index][0]
        return configs
