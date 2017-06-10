# Python Workshop Materials
This repo contains a series of introductory tutorials for the Python programming language. The materials were originally written by Sam Zorowitz for an Intro to Python Workshop for the Columbia Quantitative Methods in the Social Sciences (QMSS) masters program in summer, 2017. The tutorials are broken into five sequential modules and cover the following topics:

| # | Topic                                     | Description                                                                                                                                                                                                                                                                                                                                     | Packages Covered                                   |
|---|-------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------|
| 1 | Intro to Python & Numpy                   | An overview of the Python language, including basic types, control flow, defining functions, and basic scripting. Also introduces the NumPy library and its core functions.                                                                                                                                                                     | numpy                                              |
| 2 | DataFrames, Statistics, and Visualization | Introduces the Pandas library for generating, manipulating, and saving DataFrames. Basic statistical functions with Scipy and Statsmodels are also covered. Examples of data visualization with Matplotlib and Seaborn are provided.                                                                                                            | scipy, pandas, statsmodels, matplotlib, seaborn    |
| 3 | Machine Learning                          | An overview of machine learning in Python with the Scikit-Learn library. Topics covered include preprocessing and standardizing data; unsupervised learning (PCA, K-means, agglomerative clustering); supervised learning (linear models, SVMs, decision trees, random forests, and neural networks); and cross-validation.                     | scikit-learn                                       |
| 4 | Text Processing                           | The Natural Language Toolkit (NLTK) library is introduced. Steps in processing text are described, including encoding, tokenizing, word-stopping, stemming/lemmatizing, and spellchecking. Machine learning models useful for text analysis are also discussed using Scikit-Learn (naive Bayes classifiers, Latent Dirichlet Allocation model). | nltk, scikit-learn                                 |
| 5 | API Wrappers & Webscraping                | Python wrappers for several major APIs (Facebook, Twitter, Reddit) are discussed. Links to Python wrappers other major APIs are provided but not further discussed. Webcrawling and webscraping with BeautifulSoup are also discussed.                                                                                                          | facebook-sdk, twython, praw, BeautifulSoup, scrapy |

## Contents
All modules are broken into three parts: (1) **notes**, which provide overviews and use cases for the python libraries covered; (2) **exercises**, which provide example problems for learners to work on; and (3) **solutions**, which provide solutions to the exercises.

To further motivate the topics, many of the modules include and make use of real datasets collected from various online repositories. These are detailed below and in their respective folders. 

## Prerequisites
The tutorials are all written in Jupyter-Notebooks as part of the Anaconda python v3.6 distribution. Please visit its [this page](https://www.continuum.io/downloads) to download and install the Anaconda distribution (python version 3.6). 

# References
## Essential Texts
The following references were instrumental in writing these tutorials and provided tremendous insight in introducing topics, structuring walkthroughs, and describing functions. They are exceptional guides to their respective topics and are cited repeatedly. I extend my sincere thanks to the authors.

Kevin Sheppard. *Introduction to Python for Econometrics, Statistics, and Data Analysis, 3rd Edition.* https://www.kevinsheppard.com/Python_for_Econometrics.

Andreas Muller & Sarah Guido. *Introduction to Machine Learning with Python: A Guide for DAta Scientists.* http://shop.oreilly.com/product/0636920030515.do.

Steven Bird, Ewan Klein, Edward Loper. *Natural Language Processing with Python.* http://victoria.lviv.ua/html/fl5/NaturalLanguageProcessingWithPython.pdf. 

## Datasets
Gambling Dataset (Module 2)
* Publication: https://www.ncbi.nlm.nih.gov/pubmed/17255512
* Download: https://openfmri.org/dataset/ds000005/

Stroop Dataset (Module 2)
* Publication: https://www.ncbi.nlm.nih.gov/pubmed/25143543
* Download: https://openfmri.org/dataset/ds000164/

Iris Dataset (Module 3)
* Publication: https://www.jstor.org/stable/2394164
* Download: https://archive.ics.uci.edu/ml/datasets/iris

Diabetes Dataset (Module 3)
* Publication: https://projecteuclid.org/euclid.aos/1083178935
* Download: http://www4.stat.ncsu.edu/~boos/var.select/diabetes.html

Phenotype Dataset (Module 3)
* Publication: https://www.nature.com/articles/sdata2016110
* Download: https://openfmri.org/dataset/ds000030/

Wine Dataset (Module 3)
* Publication: http://www.sciencedirect.com/science/article/pii/S0167923609001377
* Download: https://archive.ics.uci.edu/ml/datasets/Wine+Quality

NSF Abstracts Dataset (Module 4)
* Publication: https://arxiv.org/abs/1409.7591
* Download: https://www.nsf.gov/awardsearch/download.jsp

Amazon Food Reviews (Module 4)
* Publication: http://i.stanford.edu/~julian/pdfs/www13.pdf
* Download: http://snap.stanford.edu/data/web-FineFoods.html
