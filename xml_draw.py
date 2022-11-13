import os
import os.path
import xml.etree.cElementTree as ET
import cv2
def draw(image_path, xml_path, root_saved_path):
    """
    图片根据标注画框
    """
    src_img_path = image_path
    src_ann_path = xml_path
    for file in os.listdir(src_ann_path):
        # print(file)
        file_name, suffix = os.path.splitext(file)
        # import pdb
        # pdb.set_trace()
        if suffix == '.xml':
            # print(file)
            xml_path = os.path.join(src_ann_path, file)
            image_path = os.path.join(src_img_path, file_name+'.jpg')
            img = cv2.imread(image_path)
            tree = ET.parse(xml_path)
            root = tree.getroot()
            # import pdb
            # pdb.set_trace()
            for obj in root.iter('object'):
                name = obj.find('name').text
                xml_box = obj.find('bndbox')
                x1 = int(xml_box.find('xmin').text)
                x2 = int(xml_box.find('xmax').text)
                y1 = int(xml_box.find('ymin').text)
                y2 = int(xml_box.find('ymax').text)
                cv2.rectangle(img, (x1, y1), (x2, y2), (255, 0, 0), thickness=2)
                # 字为绿色
                # cv2.putText(img, name, (x1, y1), cv2.FONT_HERSHEY_COMPLEX, 0.7, (0, 255, 0), thickness=2)
            cv2.imwrite(os.path.join(root_saved_path, file_name+'.jpg'), img)


if __name__ == '__main__':
    image_path = "./Datasets/COCO/images/val"
    xml_path = "./Datasets/COCO/xml_annotations/val"
    root_saved_path = "/home/xx/faceDetection/data/xml_output"
    draw(image_path, xml_path, root_saved_path)
