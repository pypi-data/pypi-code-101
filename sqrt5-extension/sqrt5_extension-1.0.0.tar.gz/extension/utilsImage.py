# !/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Sqrt5


import numpy as np
from PIL import Image, ImageDraw, ImageFont

from .utils import *



class point:
    def __init__(self, x, y):
        """
        生成一个点类实例

        :param x: x坐标
        :param y: y坐标
        """
        self.x = x
        self.y = y


    @property
    def toTuple(self):
        """
        返回由(x, y)组成的tuple

        :param x: x坐标
        :returns: (x, y)
        """
        return self.x, self.y


    def set(self, x, y):
        """
        设置点的坐标

        :param x: x坐标
        :param y: y坐标
        """
        self.x = x
        self.y = y


    def offset(self, dx, dy):
        """
        对点进行偏移

        :param dx: x坐标偏移量
        :param dy: y坐标偏移量
        """
        self.x += dx
        self.y += dy


    def scale(self, transform_center, scale):
        """
        得到以某点为中心点放大后的新坐标

        :param transform_center: 变换中心点坐标
        :param scale: 放大比例
        """
        self.x = scale * (self.x - transform_center.x) + transform_center.x
        self.y = scale * (self.y - transform_center.y) + transform_center.y


    def rotate(self, transform_center, theta):
        """
        得到以某点为中心点旋转后的新坐标

        :param transform_center: 变换中心点坐标
        :param theta: 逆时针旋转角度(弧度)
        """
        p = point(self.x, self.y)
        p.offset(-transform_center.x, -transform_center.y)
        self.x = math.sin(theta) * p.y + math.cos(theta) * p.x
        self.y = math.cos(theta) * p.y - math.sin(theta) * p.x
        self.offset(transform_center.x, transform_center.y)


    def __eq__(self, other):
        assert type(self) == type(other)
        if self.x == other.x and self.y == other.y:
            return True
        return False


class box:
    def __init__(self, name='', param1=0, param2=0, param3=0, param4=0, mode='center'):
        """
        生成一个框类实例
        """
        assert mode in ['center', 'lefttop', 'bbox']
        self.name = ''
        self.note = {}
        self.p = point(0, 0)
        self.w = 0
        self.h = 0
        if mode == 'center':
            self.setFromCenter(name, param1, param2, param3, param4)
        elif mode == 'lefttop':
            self.setFromLeftTop(name, param1, param2, param3, param4)
        elif mode == 'bbox':
            self.setFromBBox(name, param1, param2, param3, param4)


    def __repr__(self):
        return f'{self.bboxWithName()}'


    @property
    def area(self):
        """
        获得框的面积

        :returns: 框的面积
        """
        return self.w * self.h


    @property
    def x(self):
        """
        获得框中心点的x坐标

        :returns: 框中心点的x坐标
        """
        return self.p.x


    @property
    def y(self):
        """
        获得框中心点的y坐标

        :returns: 框中心点的y坐标
        """
        return self.p.y


    @property
    def xmin(self):
        """
        获得框最左侧的x坐标

        :returns: 框最左侧的x坐标
        """
        return self.p.x - self.w / 2


    @property
    def xmax(self):
        """
        获得框最右侧的x坐标

        :returns: 框最右侧的x坐标
        """
        return self.xmin + self.w


    @property
    def ymin(self):
        """
        获得框最上方的y坐标

        :returns: 框最上方的y坐标
        """
        return self.p.y - self.h / 2


    @property
    def ymax(self):
        """
        获得框最下方的y坐标

        :returns: 框最下方的y坐标
        """
        return self.ymin + self.h


    @property
    def p1(self):
        """
        获得框左上角点

        :returns: 框左上角点
        """
        return point(self.xmin, self.ymin)


    @property
    def p2(self):
        """
        获得框左下角点

        :returns: 框左下角点
        """
        return point(self.xmin, self.ymax)


    @property
    def p3(self):
        """
        获得框右下角点

        :returns: 框右下角点
        """
        return point(self.xmax, self.ymax)


    @property
    def p4(self):
        """
        获得框右上角点

        :returns: 框右上角点
        """
        return point(self.xmax, self.ymin)


    def expandAreaByChar(self, scale_w=0.1, scale_h=0.1):
        """
        按照现有框中的行列扩展相应比例

        :param scale_w: 宽度扩展比例
        :param scale_h: 高度扩展比例
        """
        return_char = '#' if box.name.count('\n') < box.name.count('#') else '\n'
        nrow = self.name.count(return_char)
        ncol = max([len(chars) for chars in self.name.split(return_char)])
        char_h = self.h / nrow
        char_w = self.w / ncol
        self.w = self.w * scale_w * char_w
        self.h = self.h * scale_h * char_h


    def setFromCenter(self, name, x, y, w, h):
        """
        设置框的各种信息

        :param name: 框名
        :param x: 中心x坐标
        :param y: 中心y坐标
        :param w: 宽度
        :param h: 高度
        """
        self.name = name
        self.p.set(x, y)
        self.w = w
        self.h = h


    def setFromLeftTop(self, name, x, y, w, h):
        """
        设置框的各种信息

        :param name: 框名
        :param x: 左上角x坐标
        :param y: 左上角y坐标
        :param w: 宽度
        :param h: 高度
        """
        self.setFromCenter(name, x + w / 2, y + h / 2, w, h)


    def setFromBBox(self, name, xmin, ymin, xmax, ymax):
        """
        设置框的各种信息

        :param name: 框名
        :param xmin: 左上角x坐标
        :param ymin: 左上角y坐标
        :param xmax: 右下角x坐标
        :param ymax: 右下角y坐标
        """
        self.setFromLeftTop(name, xmin, ymin, xmax - xmin, ymax - ymin)


    def bbox(self):
        """
        获取边框坐标(xmin, ymin, xmax, ymax)

        :returns: 边框坐标
        """
        return self.xmin, self.ymin, self.xmax, self.ymax


    def bboxWithName(self):
        """
        获取边框名字及坐标(name, xmin, ymin, xmax, ymax)

        :returns: 边框名字及坐标
        """
        return self.name, self.xmin, self.ymin, self.xmax, self.ymax


    def offset(self, dx, dy):
        """
        对框进行偏移

        :param dx: x坐标偏移量
        :param dy: y坐标偏移量
        """
        self.p.offset(dx, dy)


    def scale(self, transform_center=point(0, 0), scale=1):
        """
        得到以某点为中心点放大后的新框

        :param transform_center: 变换中心点坐标，默认为左上角
        :param scale: 放大比例，默认为1
        """
        self.p.scale(transform_center, scale)
        self.w = self.w * scale
        self.h = self.h * scale


    def rotate(self, transform_center=point(0, 0), theta=0):
        """
        得到以某点为中心点旋转后的新框，框的边缘与图像边缘平行

        :param transform_center: 变换中心点坐标，默认为左上角
        :param theta: 逆时针旋转角度(弧度)
        """
        p1 = self.p1
        p2 = self.p2
        p3 = self.p3
        p4 = self.p4
        p1.rotate(transform_center, theta)
        p2.rotate(transform_center, theta)
        p3.rotate(transform_center, theta)
        p4.rotate(transform_center, theta)
        self.setFromBBox(self.name, min(p1.x, p2.x, p3.x, p4.x), min(p1.y, p2.y, p3.y, p4.y),
                      max(p1.x, p2.x, p3.x, p4.x), max(p1.y, p2.y, p3.y, p4.y))


    def __eq__(self, other):
        assert type(self) == type(other)
        if self.p == other.p and self.name == other.name and self.w == other.w and self.h == other.h and self.note == other.note:
            return True
        return False


def drawBox(image, boxes, with_text=True, with_score=False, text_in_box=True, thickness=2, box_color=(0, 255, 0), size=None, char_color=(255, 0, 0)):
    """
    在image中绘制框列表中的框

    :param image: pillow格式图片(RGB)
    :param boxes: 框列表
    :param with_text: 是否加入框名
    :param with_score: 是否加入分数
    :param text_in_box: 框名在框左上角的内侧还是外侧
    :param thickness: 框线厚度
    :param box_color: 框颜色
    :param char_color: 框名颜色
    :returns: 返回绘制好框的图片
    """
    font_file = os.path.join(os.path.split(__file__)[0], 'simhei.ttf')
    image_output = image.copy()
    image_output = image_output.convert('RGB')
    image_output_draw = ImageDraw.Draw(image_output)
    for box in boxes:
        nrow = max(box.name.count('#'), box.name.count('\n'))
        thickness = min(thickness, int(math.ceil(box.h / (nrow + 1) * 0.4))) # 获取框线厚度，厚度应该小于行高的40%
    for box in boxes:
        for i in range(thickness):
            image_output_draw.rectangle((box.xmin + i, box.ymin + i, box.xmax - i, box.ymax - i), outline=box_color) # 多次向内收缩绘制框
    if with_text:
        for box in boxes:
            box_name = 'NULL' if box.name == '' else box.name
            return_char = '#' if box.name.count('\n') < box.name.count('#') else '\n'
            char_size = size
            if size is None:
                nrow = box_name.count(return_char)
                ncol = max([len(chars) for chars in box_name.split(return_char)])
                char_size = min(32, int(math.ceil(box.h / (nrow + 1) * 0.6)), int(math.ceil(box.w / ncol)))
            font = ImageFont.truetype(font=font_file, size=char_size, encoding="utf-8")
            text = ''.join([char if char != return_char else '\n' for char in box_name])
            if with_score and 'score' in box.note:
                text = '%.2f|%s' % (box.note['score'] * 100, text)
            w, h = image_output_draw.textsize(text=text, font=font, spacing=0)
            xy = (box.xmin + thickness, box.ymin + thickness, box.xmin + thickness + w, box.ymin + thickness + h)
            if not text_in_box:
                if box.w >= box.h:
                    xy = (box.xmin, box.ymin - h, box.xmin + w, box.ymin)
                else:
                    xy = (box.xmin - w, box.ymin, box.xmin, box.ymin + h)
            image_output_draw.rectangle(xy=xy, fill=box_color)
            image_output_draw.multiline_text(xy=xy[0:2], text=text, fill=char_color, font=font, spacing=0)
    return image_output


def drawBoxCV(image, boxes, with_text=True, with_score=False, text_in_box=True, thickness=2, box_color=(0, 255, 0), size=None, char_color=(0, 0, 255)):
    """
    在image中绘制框列表中的框

    :param image: cv2格式图片(BGR)
    :param boxes: 框列表
    :param with_text: 是否加入框名
    :param with_score: 是否加入分数
    :param text_in_box: 框名在框左上角的内侧还是外侧
    :param thickness: 框线厚度
    :param box_color: 框颜色
    :param char_color: 框名颜色
    :returns: 返回绘制好框的图片
    """
    font_file = os.path.join(os.path.split(__file__)[0], 'simhei.ttf')
    image_output = image.copy()
    image_output = image_output.astype(np.uint8)
    if len(image_output.shape) == 2:
        image_output = cv2.cvtColor(image_output, cv2.COLOR_GRAY2BGR)
    thickness = min([thickness] + [int(math.ceil(box.h * 0.4)) for box in boxes]) # 获取框线厚度，厚度应该小于最小行高的40%
    for box in boxes:
        cv2.rectangle(
            image_output,
            intRound((box.xmin + thickness * 0.5, box.ymin + thickness * 0.5)),
            intRound((box.xmax - thickness * 0.5, box.ymax - thickness * 0.5)),
            box_color,
            thickness
        )
    if with_text:
        for box in boxes:
            box_name = 'NULL' if box.name == '' else box.name
            if with_score and 'score' in box.note:
                box_name = '%.2f|%s' % (box.note['score'] * 100, box_name)
            char_size = size
            if size is None:
                char_size = min(24, int(math.ceil(box.w / len(box_name))))
            scale = char_size / 20
            font = cv2.FONT_HERSHEY_SIMPLEX
            retval, baseline = cv2.getTextSize(box_name, font, scale, intRound(scale * 2))
            w, h = retval
            h = h + baseline * 1.2
            p1 = intRound((box.xmin + thickness, box.ymin + thickness))
            p2 = intRound((box.xmin + thickness + w, box.ymin + thickness + h))
            pt = intRound((box.xmin + thickness, box.ymin + thickness + h - baseline))
            if not text_in_box:
                if box.w < box.h and w < h:
                    p1 = intRound((box.xmin - w, box.ymin))
                    p2 = intRound((box.xmin, box.ymin + h))
                    pt = intRound((box.xmin - w, box.ymin + h - baseline))
                else:
                    p1 = intRound((box.xmin, box.ymin - h))
                    p2 = intRound((box.xmin + w, box.ymin))
                    pt = intRound((box.xmin, box.ymin - baseline))
            cv2.rectangle(image_output, p1, p2, box_color, -1)
            cv2.putText(image_output, box_name, pt, font, scale, char_color, intRound(scale * 2))
    return image_output


def readRatioFile(file_name, image, id2name, split_char=' '):
    """
    从yolo格式的文件中读取框并形成列表(id, [score], x / img_w, y / img_h, w / img_w, h / img_h)

    :param file_name: 文件名
    :param image: 对应图片，主要为获取宽高
    :param id2name: 码表，用以存储中文名
    :param split_char: 分割字符
    :returns: 返回框列表
    """
    w, h = image.size
    boxes = []
    with codecs.open(file_name, 'r', 'utf-8') as f:
        for line in f:
            elems = line.strip().split(split_char)
            assert len(elems) in [5, 6]
            b = box()
            if len(elems) == 5:
                b.setFromCenter(id2name[int(elems[0])], float(elems[1]) * w, float(elems[2]) * h, float(elems[3]) * w, float(elems[4]) * h)
            else:
                b.setFromCenter(id2name[int(elems[0])], float(elems[2]) * w, float(elems[3]) * h, float(elems[4]) * w, float(elems[5]) * h)
                b.note['score'] = float(elems[1])
            boxes.append(b)
    return boxes


def readPixelFile(file_name, split_char=' '):
    """
    从标注工具格式的文件中读取框并形成列表(name, [score], xmin, ymin, w, h)

    :param file_name: 文件名
    :param split_char: 分割字符
    :returns: 返回框列表
    """
    boxes = []
    with codecs.open(file_name, 'r', 'utf-8') as f:
        for line in f:
            elems = line.strip().split(split_char)
            assert len(elems) in [5, 6]
            b = box()
            if len(elems) == 5:
                b.setFromLeftTop(elems[0], float(elems[1]), float(elems[2]), float(elems[3]), float(elems[4]))
            else:
                b.setFromLeftTop(elems[0], float(elems[2]), float(elems[3]), float(elems[4]), float(elems[5]))
                b.note['score'] = float(elems[1])
            boxes.append(b)
    return boxes


def readBBoxFile(file_name, split_char=' '):
    """
    从边框格式的文件中读取框并形成列表(name, [score], xmin, ymin, xmax, ymax)

    :param file_name: 文件名
    :param split_char: 分割字符
    :returns: 返回框列表
    """
    boxes = []
    with codecs.open(file_name, 'r', 'utf-8') as f:
        for line in f:
            elems = line.strip().split(split_char)
            assert len(elems) in [5, 6]
            b = box()
            if len(elems) == 5:
                b.setFromBBox(elems[0], float(elems[1]), float(elems[2]), float(elems[3]), float(elems[4]))
            else:
                b.setFromBBox(elems[0], float(elems[2]), float(elems[3]), float(elems[4]), float(elems[5]))
                b.note['score'] = float(elems[1])
            boxes.append(b)
    return boxes


def writeRatioFile(file_name, boxes, image, name2id, split_char=' ', with_score=False):
    """
    从边框列表写入yolo格式的文件中(id, [score], x / img_w, y / img_h, w / img_w, h / img_h)

    :param file_name: 文件名
    :param boxes: 框列表
    :param image: 图片
    :param name2id: 码表，用以转成标签编号
    :param split_char: 分割字符
    """
    if with_score:
        for box in boxes:
            assert 'score' in box.note, 'score not in box'
    w, h = image.size
    with codecs.open(file_name, 'w', 'utf-8') as fout:
        for box in boxes:
            if with_score:
                fout.write('%d%s%f%s%f%s%f%s%f%s%f\n' % (
                    name2id[box.name], split_char,
                    box.note['score'], split_char,
                    box.x / w, split_char,
                    box.y / h, split_char,
                    box.w / w, split_char, box.h / h
                ))
            else:
                fout.write('%d%s%f%s%f%s%f%s%f\n' % (
                    name2id[box.name], split_char,
                    box.x / w, split_char,
                    box.y / h, split_char,
                    box.w / w, split_char, box.h / h
                ))
    return


def writePixelFile(file_name, boxes, split_char=' ', with_score=False):
    """
    从边框列表写入标注工具格式的文件中(name, [score], xmin, ymin, w, h)

    :param file_name: 文件名
    :param boxes: 框列表
    :param split_char: 分割字符
    """
    if with_score:
        for box in boxes:
            assert 'score' in box.note, 'score not in box'
    with codecs.open(file_name, 'w', 'utf-8') as fout:
        for box in boxes:
            if with_score:
                fout.write('%s%s%f%s%f%s%f%s%f%s%f\n' % (
                    box.name, split_char,
                    box.note['score'], split_char,
                    box.xmin, split_char,
                    box.ymin, split_char,
                    box.w, split_char,
                    box.h
                ))
            else:
                fout.write('%s%s%f%s%f%s%f%s%f\n' % (
                    box.name, split_char,
                    box.xmin, split_char,
                    box.ymin, split_char,
                    box.w, split_char,
                    box.h
                ))


def writeBBoxFile(file_name, boxes, split_char=' ', with_score=False):
    """
    从边框列表写入边框格式的文件中(name, [score], xmin, ymin, xmax, ymax)

    :param file_name: 文件名
    :param boxes: 框列表
    :param split_char: 分割字符
    """
    if with_score:
        for box in boxes:
            assert 'score' in box.note, 'score not in box'
    with codecs.open(file_name, 'w', 'utf-8') as fout:
        for box in boxes:
            if with_score:
                fout.write('%s%s%f%s%f%s%f%s%f%s%f\n' % (
                    box.name, split_char,
                    box.note['score'], split_char,
                    box.xmin, split_char,
                    box.ymin, split_char,
                    box.xmax, split_char,
                    box.ymax
                ))
            else:
                fout.write('%s%s%f%s%f%s%f%s%f\n' % (
                    box.name, split_char,
                    box.xmin, split_char,
                    box.ymin, split_char,
                    box.xmax, split_char,
                    box.ymax
                ))


def getWI(box1, box2):
    """
    获取两框横向交叠长度

    :param box1: 框1
    :param box2: 框2
    :returns: 横向交叠长度
    """
    dw = min(box1.xmax, box2.xmax) - max(box1.xmin, box2.xmin)
    return max(0, dw)


def getHI(box1, box2):
    """
    获取两框纵向交叠长度

    :param box1: 框1
    :param box2: 框2
    :returns: 纵向交叠长度
    """
    dh = min(box1.ymax, box2.ymax) - max(box1.ymin, box2.ymin)
    return max(0, dh)


def getI(box1, box2):
    """
    获取两框交叠区域面积

    :param box1: 框1
    :param box2: 框2
    :returns: 交叠区域面积
    """
    area = getWI(box1=box1, box2=box2) * getHI(box1=box1, box2=box2)
    return area


def getU(box1, box2):
    """
    获取两框交叠区域面积

    :param box1: 框1
    :param box2: 框2
    :returns: 两个box区域面积和
    """
    area = getI(box1=box1, box2=box2)
    return box1.area + box2.area - area


def getIoU(box1, box2):
    """
    获取两框交叠区域面积

    :param box1: 框1
    :param box2: 框2
    :returns: 交叠区域面积占总面积比例
    """
    area = getI(box1=box1, box2=box2)
    return area / max(1e-6, (box1.area + box2.area - area))


def getDistance(p1, p2):
    """
    获取两点区域

    :param box1: 点1
    :param box2: 点2
    :returns: 两点距离
    """
    return math.sqrt((p2.x - p1.x) ** 2 + (p2.y - p1.y) ** 2)


def mergeBoxes(boxes, with_name=False):
    box_output = box()
    xmin = min([b.xmin for b in boxes])
    ymin = min([b.ymin for b in boxes])
    xmax = max([b.xmax for b in boxes])
    ymax = max([b.ymax for b in boxes])
    name = ''
    if with_name:
        name = '&'.join(list(set([b.name for b in boxes])))
    box_output.setFromBBox(name, xmin, ymin, xmax, ymax)
    return box_output


def getPrintCaptcha(chars, font_file='', font_size=48, chars_interval=0, char_color=(255, 255, 255), back_color=(0, 0, 0)):
    """
    获取印刷体文字

    :param chars: 字符串
    :param font_file: 字体文件(需要和chars配合避免超出范围)
    :param font_size: 字体大小
    :param chars_interval: 字符间距
    :param char_color: 字符颜色
    :param back_color: 背景颜色，后续获取掩码图片需要用到
    :returns: array格式的图片
    """
    assert math.ceil(-font_size / 8) <= chars_interval <= math.floor(font_size / 3)
    if not font_file:
        font_file = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'simhei.ttf')
    font = ImageFont.truetype(font_file, font_size, encoding='utf-8')
    image = Image.new('RGB', (int(math.ceil(font_size / 4)), font_size))
    draw = ImageDraw.Draw(image)
    w, h = draw.textsize(chars, font=font)
    w, h = w * 4, h * 4 # 需要根据字体，字号，字符间距动态调整，避免生成图片无法cover住字符
    if w > 0 and h > 0:
        image = Image.new('RGB', (w, h), color=back_color)
        stroke_width = random.choice([0, 0, 0, 0, 1])
        w_sum = 0
        for char in chars:
            ImageDraw.Draw(image).text((w_sum, 0), char, font=font, fill=char_color, stroke_width=stroke_width)
            w, h = font.getsize(char)
            w_sum += (w + chars_interval)
        bbox = image.getbbox()
        if bbox is not None and bbox[2] - bbox[0] > 10 and bbox[3] - bbox[1] > 10:
            image = image.crop(bbox)
    image = np.array(image).astype(np.uint8)
    return image


def getMask(image, back_color=(0, 0, 0), mode='foreground'):
    """
    获取掩码图片

    :param image: array格式图片
    :param back_color: 背景颜色
    :returns: array格式的掩码图片，前景区域为1，背景区域为0
    """
    assert mode in ['foreground', 'background']
    mask = np.array(np.array(image == back_color).sum(axis=2) != 3).astype(np.bool)
    if mode == 'foreground':
        return mask
    else:
        return ~mask


def addOnImage(image_background, image, mask=None, offset=(0, 0), back_color=(0, 0, 0)):
    """
    将图片使用替换方法粘贴到背景图片上，粘贴效果

    :param image_background: array格式背景图片
    :param image: array格式图片
    :param offset: 偏移量(width, height)
    :param back_color: 背景颜色
    :returns: array格式结果图片
    """
    image_background = image_background.copy()
    image = image.copy()

    h, w = image.shape[:2]
    xmin, ymin = offset
    xmax, ymax = tuple(map(sum, zip(offset, (w, h))))

    if mask is None:
        mask = getMask(image, back_color, 'foreground') # 获取前景掩码
    else:
        mask = getMask(mask, back_color, 'foreground') # 获取前景掩码
    image_background[ymin:ymax, xmin:xmax][mask] = image[mask]

    return np.array(image_background).astype(np.uint8)


def multiOnImage(image_background, image, mask=None, offset=(0, 0), back_color=(0, 0, 0)):
    """
    将图片使用乘法乘到背景图片上，加盖效果

    :param image_background: array格式背景图片
    :param image: array格式图片
    :param offset: 偏移量(width, height)
    :param back_color: 背景颜色
    :returns: array格式结果图片
    """
    image_background = image_background.copy()
    image = image.copy()

    h, w = image.shape[:2]
    xmin, ymin = offset
    xmax, ymax = tuple(map(sum, zip(offset, (w, h))))

    if mask is None:
        mask = getMask(image, back_color, 'background') # 获取背景掩码
    else:
        mask = getMask(mask, back_color, 'background') # 获取背景掩码
    image[mask, :] = (255, 255, 255) # 背景补白(亮度最强，相乘不减弱)
    image_background[ymin:ymax, xmin:xmax] = image.astype(np.float32) * image_background.astype(np.float32)[ymin:ymax, xmin:xmax] / 255

    return np.array(image_background).astype(np.uint8)


def pillow2cv(image, is_bgr=True):
    image_np = np.array(image).astype(np.uint8)
    if is_bgr:
        image_np = cv2.cvtColor(image_np, cv2.COLOR_RGB2BGR)
    return image_np


def cv2pillow(image, is_bgr=True):
    if is_bgr:
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image = Image.fromarray(image)
    return image


def showImage(image, name='', size=(800, 600)):
    """
    显示图片

    :param image: 图片
    :param name: 图片名(仅支持英文)
    :param size: 图片尺寸(width, height)
    """
    image = image.copy()
    image = np.array(image).astype(np.uint8)
    h, w = image.shape[:2]
    scale = min(size[0] / w, size[1] / h)
    image = cv2.resize(image, (0, 0), fx=scale, fy=scale)
    cv2.imshow(name, image)
    cv2.waitKey(0)
    return
