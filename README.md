# pdf_to_img
Convert PDF files into images.

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
#### Increase page resolution by \<zoom>. The default value is 3.
```bash
python pdf_to_img.py <pdf_input_path_folder> <img_output_path_folder> <zoom>
```
#### Save image as a \<mode> type. The default is RGB. See [modes](https://pillow.readthedocs.io/en/stable/handbook/concepts.html#concept-modes).
```bash
python pdf_to_img.py <pdf_input_path_folder> <img_output_path_folder> <zoom> <mode>
```
