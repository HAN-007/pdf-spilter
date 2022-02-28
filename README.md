# pdf-spilter

## Aim
The aim of the project is to save each page of multi-page pdfs by dividing them into 4 parts.

## Working logic
The imported pdf is first browsed page by page and saved as an image.
Then, the recorded images are read with the cv2 library to be divided into 4 parts each.
The read pictures are divided into 4 parts and saved in a temporary file.
They are read again from the saved temporary file to be converted to pdf and saved as pdf under the result folder.
thanks for reading
