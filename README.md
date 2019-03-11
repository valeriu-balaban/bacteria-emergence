# Quantifying emergence and self-organisation of Enterobacter cloacae microbial communities

This repository contains supporting Jupyter Notebook for paper ["Quantifying emergence and self-organisation of Enterobacter cloacae microbial communities"](https://www.nature.com/articles/s41598-018-30654-9#data-availability)

To reproduce the results, clone this repository and install python dependencies using [conda](https://conda.io/projects/conda/en/latest/user-guide/install/index.html):

```
git clone https://github.com/valeriu-balaban/bacteria-emergence
cd bacteria-emergence

conda create -n bacteria-emergence python=3 jupyterlab scikit-image scipy seaborn matplotlib pandas numpy
conda activate bacteria-emergence
jupyter lab
```

Next, access jupyter lab webpage in browser to run the code to analyze bacteria images in processed data folder.
