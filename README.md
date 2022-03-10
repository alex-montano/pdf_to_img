# pdf_to_img
Script to convert PDF files into images.

## Installations
```bash
python -m pip install --upgrade pip
python -m pip install PyMuPDF
python -m pip install Pyllow
```

## Usages
```bash
python pdf_to_img.py <pdf_input_path_folder> <img_output_path_folder>
```
#### Considerations
- For PDFs that has only one page, it will save as a JPG with the name of the PDF.
- For PDFs that has more than one page, it will create a folder with the name of the PDF, and each image will have the page number at the end of the file.

## Other usages
Increase page resolution by __\<zoom>__. The default value is 3.
```bash
python pdf_to_img.py <pdf_input_path_folder> <img_output_path_folder> <zoom>
```
Save image as a __\<mode>__ type. The default is RGB. See [PIL modes](https://pillow.readthedocs.io/en/stable/handbook/concepts.html#concept-modes).
```bash
python pdf_to_img.py <pdf_input_path_folder> <img_output_path_folder> <zoom> <mode>
```
