# pdf-spilter

## Aim
The aim of the project is to save each page of multi-page pdfs by dividing them into 4 parts.

## Working logic
The imported pdf is first browsed page by page and saved as an image.
Then, the recorded images are read with the cv2 library to be divided into 4 parts each.
The read pictures are divided into 4 parts and saved in a temporary file.
They are read again from the saved temporary file to be converted to pdf and saved as pdf under the result folder.
thanks for reading

## Results :

![image3](https://user-images.githubusercontent.com/52994504/155983568-6de3febb-e45b-4e6a-b078-82f5a9d7fd9e.png)

