# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 15:10:53 2020

@author: hmzzl
"""
import os
import re
for file in os.listdir():
    if file[-3:] == 'xml':
        with open(file, 'r+') as f:
            ori_txt = f.readlines()
            line_list = [i.strip(' ').strip("\n") for i in ori_txt]
            idx = line_list.index("<size>")
            w = int(line_list[idx+1].strip('<width>').strip('</width>'))
            h = int(line_list[idx+2].strip('<height>').strip('</height>'))
            box_idx = [i for i,v in enumerate(line_list) if v == "<bndbox>"]
            for idxx in box_idx:
                xmin = int(line_list[idxx+1].strip('<xmin>').strip('</xmin>'))
                ymin = int(line_list[idxx+2].strip('<ymin>').strip('</ymin>'))
                xmax = int(line_list[idxx+3].strip('<xmax>').strip('</xmax>'))
                ymax = int(line_list[idxx+4].strip('<ymax>').strip('</ymax>'))
                if xmin < 0:
                    xmin = 0
                    print("change",ori_txt[idxx+1],"to", xmin)
                    ori_txt[idxx+1] = re.sub(">-{0,1}\d*<",'>'+str(xmin)+'<',ori_txt[idxx+1])
                if ymin < 0:
                    ymin = 0
                    print("change",ori_txt[idxx+2],"to", ymin)
                    ori_txt[idxx+2] = re.sub(">-{0,1}\d*<",'>'+str(ymin)+'<',ori_txt[idxx+2])
                if xmax > w:
                    xmax = w
                    print("change",ori_txt[idxx+3],"to", xmax)
                    ori_txt[idxx+3] = re.sub(">-{0,1}\d*<",'>'+str(xmax)+'<',ori_txt[idxx+3])
                if ymax > h:
                    ymax = h
                    print("change",ori_txt[idxx+4],"to", ymax)
                    ori_txt[idxx+4] = re.sub(">-{0,1}\d*<",'>'+str(ymax)+'<',ori_txt[idxx+4])
                #print(xmin)
            f.seek(0)
            f.writelines(ori_txt)
                
                
                
            

