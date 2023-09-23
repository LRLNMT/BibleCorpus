# BibleCorpus
This repository contains the code to download and align Bible data used in the paper [Leveraging Auxiliary Domain Parallel Data in Intermediate Task Fine-tuning for Low-resource Translation](https://arxiv.org/pdf/2306.01382.pdf), published at Practical Machine Learning for Developing Countries Workshop, ICLR 2023.

## Data
There are 5 languages for which we download/scrape data from the web and then align them. These are Kannada, Hindi, Gujarati, Tamil, Sinhala. We download the the data for the first four languages from [ebible.org](https://ebible.org/download.php). Since data from Sinhala is not available here we scrape it from [WordProject]( https://www.wordproject.org/bibles/si/index.htm). 

## Download and Align data
The following steps have to be followed to get the data set.

- Go to [ebible.org](https://ebible.org/download.php)
- Search for Kannada and click on the Indian Revised Version of the bible.
- You will visit a page like [this](https://ebible.org/details.php?id=kan2017). Download the readaloud version (kan2017_readaloud.zip) from this page.
- Repeat similar steps for other languages (Hindi, Gujarati, Tamil). For English we have used the [Basic English version of the Bible](https://ebible.org/details.php?id=engBBE). But you are free to choose the version you want. 
- Extract all the folders and rename them with their respective laguage tags and save them in the data folder.
- Now run the `parse_and_align.py` script. This should create one file for each language. 

## Method
The data created is multiway parallel for the languages mentioned above. After extracting the files you will see that there are many subfiles for each language which correspond to different chapters of the Bible. We check each of the subfiles and ensure that the number of sentence in that file is the same as that in the corresponding files in other languages. If not, we discard the whole file. For subfiles where the number of sentences are same, we observe that each sentence in a particular language has a 1:1 mapping with a sentence in other languages, which helps us in aligning the data easily. We also manually verify this on a small number of samples. The script `parse_and_align.py` uses the above mentioned logic to create the corpus.

We will soon add the menthod to scrape and create the Sinhala-English data. If you need the data urgently please contact shravannayak.p@gmail.com.

## Citation
If you use our model or code, please cite the following:

```
@article{nayak2023leveraging,
  title={Leveraging Auxiliary Domain Parallel Data in Intermediate Task Fine-tuning for Low-resource Translation},
  author={Nayak, Shravan and Ranathunga, Surangika and Thillainathan, Sarubi and Hung, Rikki and Rinaldi, Anthony and Wang, Yining and Mackey, Jonah and Ho, Andrew and Lee, En-Shiun Annie},
  journal={arXiv preprint arXiv:2306.01382},
  year={2023}
}
```