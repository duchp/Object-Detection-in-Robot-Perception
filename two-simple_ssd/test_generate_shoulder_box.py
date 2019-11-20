from __future__ import print_function
import sys
import os
import argparse
import torch
import torch.nn as nn
import torch.backends.cudnn as cudnn
import torchvision.transforms as transforms
from torch.autograd import Variable
from data import VOC_ROOT, VOC_shoulder_CLASSES as labelmap
from PIL import Image
from data import VOCAnnotationTransform_shoulder, VOCDetection_shoulder, BaseTransform, VOC_shoulder_CLASSES
import torch.utils.data as data
from ssd import build_ssd
import csv

parser = argparse.ArgumentParser(description='Single Shot MultiBox Detection')
parser.add_argument('--trained_model', default='weights_shoulder/VOC.pth',
                    type=str, help='Trained state_dict file path to open')
parser.add_argument('--save_folder', default='shoulder_csv/', type=str,
                    help='Dir to save results')
parser.add_argument('--visual_threshold', default=0.6, type=float,
                    help='Final confidence threshold')
parser.add_argument('--cuda', default=True, type=bool,
                    help='Use cuda to train model')
parser.add_argument('--voc_root', default=VOC_ROOT, help='Location of VOC root directory')
parser.add_argument('-f', default=None, type=str, help="Dummy arg so we can load in Jupyter Notebooks")
args = parser.parse_args()

if args.cuda and torch.cuda.is_available():
    torch.set_default_tensor_type('torch.cuda.FloatTensor')
else:
    torch.set_default_tensor_type('torch.FloatTensor')

if not os.path.exists(args.save_folder):
    os.mkdir(args.save_folder)


def test_net(save_folder, net, cuda, testset, transform, thresh):
    # dump predictions and assoc. ground truth to text file for now
    filename = save_folder+'test_shoulder.csv'
    num_images = len(testset)
    with open(filename,'a') as csvfile:
        f = csv.writer(csvfile)
        f.writerow(["img_id","cood_xmin","cood_ymin","cood_xmax","cood_ymax"])
        for i in range(num_images):
            print('Testing image {:d}/{:d}....'.format(i+1, num_images))
            img = testset.pull_image(i)
            img_id, annotation = testset.pull_anno(i)
            x = torch.from_numpy(transform(img)[0]).permute(2, 0, 1)
            x = Variable(x.unsqueeze(0))
            
            if cuda:
                x = x.cuda()
    
            y = net(x)      # forward pass
            detections = y.data
            # scale each detection back up to the image
            scale = torch.Tensor([img.shape[1], img.shape[0],
                                 img.shape[1], img.shape[0]])
            
            for i in range(detections.size(1)):
                j = 0
                while detections[0, i, j, 0] >= 0.6:
                    score = detections[0, i, j, 0]
                    label_name = labelmap[i-1]
                    pt = (detections[0, i, j, 1:]*scale).cpu().numpy()
                    coords = (pt[0], pt[1], pt[2], pt[3])
                    f.writerows([[img_id,int(pt[0]),int(pt[1]),int(pt[2]),int(pt[3])]])
                    j += 1


def test_voc():
    # load net
    num_classes = len(VOC_shoulder_CLASSES) + 1 # +1 background
    net = build_ssd('test', 300, num_classes) # initialize SSD
    net.load_state_dict(torch.load(args.trained_model))
    net.eval()
    print('Finished loading model!')
    # load data
    testset = VOCDetection_shoulder(args.voc_root, [('hand', 'test')], None, VOCAnnotationTransform_shoulder())
    if args.cuda:
        net = net.cuda()
        cudnn.benchmark = True
    # evaluation
    test_net(args.save_folder, net, args.cuda, testset,
             BaseTransform(net.size, (104, 117, 123)),
             thresh=args.visual_threshold)

if __name__ == '__main__':
    test_voc()
