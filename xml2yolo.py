# 坐标xml转txt
import xml.etree.ElementTree as ET
import os


classes = ['face']  # 输入缺陷名称，必须与xml标注名称一致


train_file = './Datasets/YOLO/images_val.txt'  
train_file_txt = ''

wd = os.getcwd()

def convert(size, box):
    dw = 1. / size[0]
    dh = 1. / size[1]
    box = list(box)
    box[1] = min(box[1], size[0])   # 限制目标的范围在图片尺寸内
    box[3] = min(box[3], size[1])
    x = ((box[0] + box[1]) / 2.0) * dw
    y = ((box[2] + box[3]) / 2.0) * dh
    w = (box[1] - box[0]) * dw
    h = (box[3] - box[2]) * dh
    return (x, y, w, h)   


def convert_annotation(image_id):
    in_file = open('./Datasets/COCO/xml_annotations/val/%s.xml' % (image_id))  # 读取xml文件路径

    out_file = open('./Datasets/YOLO/labels/val/%s.txt' % (image_id), 'w')  # 需要保存的txt格式文件路径
    tree = ET.parse(in_file)
    root = tree.getroot()
    size = root.find('size')
    w = int(size.find('width').text)
    h = int(size.find('height').text)

    for obj in root.iter('object'):
        cls = obj.find('name').text
        if cls not in classes:  # 检索xml中的缺陷名称
            continue
        cls_id = classes.index(cls)
        
        # if cls_id == 0 or cls_id == 11:
        #     continue
        xmlbox = obj.find('bndbox')
        b = (float(xmlbox.find('xmin').text), float(xmlbox.find('xmax').text), float(xmlbox.find('ymin').text),
             float(xmlbox.find('ymax').text))
        bb = convert((w, h), b)
        out_file.write(str(cls_id) + " " + " ".join([str(a) for a in bb]) + '\n')


image_ids_train = open('./Datasets/COCO/name_vval.txt').read().strip().split()  # 读取xml文件名索引

for image_id in image_ids_train:
    convert_annotation(image_id)

anns = os.listdir('./Datasets/COCO/xml_annotations/val/')
for ann in anns:
    ans = ''
    outpath = './Datasets/YOLO/labels_temp/val/' + ann
    if ann[-3:] != 'xml':
        continue
    train_file_txt = train_file_txt + './Datasets/YOLO/images/val/' + ann[:-3] + 'jpg\n'
    # import pdb
    # pdb.set_trace()

with open(train_file, 'w') as outfile:
    outfile.write(train_file_txt)
