# Merge PDFs

## About

Simple tool to merge all pdfs from one folder into a single pdf file locally. 

## install
1.      git clone https://github.com/slolow/mergePDF.git
2. move to mergePDF folder
3.      pipenv install -r requirements.txt

## how to use

1.      pipenv run mergePDFs.py
2.  provide folder with pdfs to merge ⚠️ **All pdf files of this folder will be merged into a single one in the given folder order** ⚠️
3. provide the path where to save the merged pdf ⚠️ **provide the path ending with the wanted name of the merged file, e.g. merged.pdf** ⚠️