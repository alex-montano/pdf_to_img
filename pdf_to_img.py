import sys
import glob
import os
import getopt

import fitz
from PIL import Image

def pdf_to_img(pdf_path, zoom = 3, mode = 'RGB'):
    # Transforms the PDF pages into images and returns it
    doc = fitz.open(pdf_path)
    mat = fitz.Matrix(zoom, zoom)
    images = []
    for page in doc:
        pix = page.get_pixmap(matrix = mat)
        images.append(Image.frombytes(mode, [pix.width, pix.height], pix.samples))
    return images

def get_pdfs(pdfs_path):
    # Returns a tuple containing a list of each PDF path and a list of each PDF name
    pdf_path_files = glob.glob(pdfs_path + '/*.pdf')
    pdf_file_names = [os.path.basename(x) for x in pdf_path_files]
    if pdf_path_files and pdf_file_names:
        return pdf_path_files, pdf_file_names
    else:
        raise Exception('Could not find any PDF in the folder')
    return pdf_path_files, pdf_file_names

if __name__ == '__main__':
    if len(sys.argv) > 2:
        pdf_path_files, pdf_file_names = get_pdfs(sys.argv[1])
    else:
        raise Exception('You must specify two path arguments: input and output folder')
    images = []
    for i, pdf_path in enumerate(pdf_path_files):
        if len(sys.argv) > 3:
            try:
                images = pdf_to_img(pdf_path, int(sys.argv[3]))
            except:
                raise Exception('The third argument must be an integer')
        else:
            images = pdf_to_img(pdf_path)
        images_path = sys.argv[2]
        if len(images) > 1:
            folder_name = pdf_file_names[i].split('.')[0]
            images_path = images_path + '/' + folder_name
            if not os.path.exists(images_path):
                os.makedirs(images_path)
        for j, image in enumerate(images):
            if len(sys.argv) > 4:
                possible_modes = ['1', 'L', 'RGB']
                if sys.argv[4] in possible_modes:
                    image = image.convert(sys.argv[4])
                else:
                    raise Exception('Possibles modes are: ' + str(possible_modes))
            if len(images) > 1:
                image_path_file = images_path + '/' + pdf_file_names[i].split('.')[0] + '-' + str(j + 1) + '.jpg'
            else:
                image_path_file = images_path + '/' + pdf_file_names[i].split('.')[0] + '.jpg'
            image.save(
                image_path_file
            )
        