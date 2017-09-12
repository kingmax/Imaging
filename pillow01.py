#!/usr/bin/env python
#coding:utf-8
"""
Author:  iJasonLee (kingmax_res@163.com;184327932@qq.com)
Purpose: Pillow study (http://docs.python-guide.org/en/latest/scenarios/imaging/)
Created: 2017/9/13
Tutorial: https://pillow.readthedocs.io/en/3.0.x/handbook/tutorial.html
"""

import unittest

from PIL import Image, ImageFilter

f = 'model_s.png'
im = Image.open(f)
#im.show()

print im.format, im.size, im.mode

import os, sys
#----------------------------------------------------------------------
def convert2JPG(files):
    """"""
    for infile in files:
        f, e = os.path.splitext(infile)
        outfile = f + '.jpg'
        if infile != outfile:
            try:
                Image.open(infile).save(outfile)
                print('[OK] convert %s'%infile)
            except IOError:
                print('cannot convert %s'%infile)

#----------------------------------------------------------------------
def create_thumbnail(infile, size=(128, 128)):
    """"""
    outfile = os.path.splitext(infile)[0] + ".thumbnail"
    if infile != outfile:
        try:
            im = Image.open(infile)
            im.thumbnail(size)
            im.save(outfile, 'JPEG')
            print('[OK] create thumbnail %s'%infile)
        except IOError:
            print('cannot create thumbnail for %s'%infile)
    

if __name__ == '__main__':
    if len(sys.argv) > 1:
        files = sys.argv[1:]
        convert2JPG(files)
    else:
        files = os.listdir('.')
        convert2JPG(files)
        for f in files:
            create_thumbnail(f)
    
    unittest.main()