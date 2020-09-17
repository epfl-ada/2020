# 00 - Intro to Tools

This tutorial should get you up and running with your Python environment, plus give you the basics of Jupyter notebooks. Please complete part 1 before the exercise session on Friday, September 18. 

## Disclaimer - Important

We don't care which platform you use to produce the Jupyter Notebook files that you will submit for grading. These instructions will help you get started with Anaconda's local installation, but feel free to use [Google Colab](https://colab.research.google.com/notebooks/intro.ipynb) (or [EPFL Noto](https://noto.epfl.ch/)). It is part of your responsibility to have a working environment for the homework and final exam.


## Part 1: Setting up your environment (IF you want a local/offline installation)

* Install Anaconda, Python 3.8 version: [Anaconda](https://www.anaconda.com/distribution/#download-section).

*For Linux*: Open a terminal, go to the Downloads folder and execute:

```
bash ./Anaconda3-2020.07-Linux-x86_64.sh -b -p $HOME/Anaconda3
```

Check that `conda` is in your path. If `which conda` returns something like `/home/YOURUSERNAME/Anaconda3/bin/conda`, you are good to go. Otherwise execute
`echo 'export PATH="$HOME/Anaconda3/bin/:$PATH"' >> $HOME/.bashrc`. Next close the terminal and open a new window. Check `which conda` again.

* IF conda is already installed, run `conda update conda`.

---


* Install Git:

*For Ubuntu/Debian*: `sudo apt-get install git`

*For Fedora*: `sudo dnf install git`

*For Windows*:
Install it following this download link: [Git](https://git-scm.com/downloads). To execute Git commands, use the Git bash: home key - type "git bash" - enter.

[Git cheatsheet](http://rogerdudler.github.io/git-guide/)

---

* Clone the tutorials repo into a local folder:

```
git clone https://github.com/epfl-ada/2020 ADA2020
cd ADA2020
```
<!-- 
* or pull new changes if you already have it (from the local folder):

```
git pull
``` -->

---

* Create a new environment:

*For Windows*: 
To execute Anaconda commands, use the Anaconda prompt: home key - type "anaconda prompt" - enter.
Also note that while it is possible to use Git commands on Anaconda prompt, we advise against it.

```
conda create -y -n ada python=3.8 scipy pandas numpy matplotlib
```

* Activate it:
    
```
conda activate ada
```

* List your environments:
    
```
conda env list
```

* To deactivate the current environment and remove an environment. (Do not run the remove command, as it will remove the environment you just installed ...)
    
```
conda deactivate
conda remove --name ada --all
```

[more info on managing environments](https://conda.io/docs/user-guide/tasks/manage-environments.html)

* Install [JupyterLab](https://jupyterlab.readthedocs.io/en/stable/) using conda (the ada environment needs to be activated):
    
```
conda install jupyterlab bokeh seaborn nb_conda_kernels
```

* [Optional] Install some extensions using the Python package manager:
    
```
pip install jupyter_nbextensions_configurator
```

---

* Run a Jupyter notebook server (be sure to be at the tutorial's folder -- `cd path/to/folder/`). A browser window should open up for you.

```
jupyter lab
```

---


* To shut down the server, close the window on your browser, then do CTRL+C in the terminal.

## Part 2: Overview of Jupyter notebooks

In [this tutorial](Intro%20to%20Jupyter%20Notebooks.ipynb) we explore the functionalities of the Jupyter notebooks. In this repository you can find the notebook we use during the tutorial.

Credits to [saloot](https://github.com/saloot) and [Michele Catasta](https://github.com/pirroh), on whose material this version is based.

## Part 3: Good coding practices - Python

This is a small guide on how-to-code. Although it's quite succint, there are a few things you should know.
Please read [this tutorial](good_coding_practices.ipynb).


## Part 4: Homework 0

Access Homework 0 (OPTIONAL and UNGRADED) [here](https://github.com/epfl-ada/2020/tree/master/Homework/00%20-%20Optional%20Homework). Clone the repo locally and take the opportunity to freshen up your Python skills, or to acquire them.

## Common issues


* IF when activating the environment you get an error that look like:

```
CommandNotFoundError: Your shell has not been properly configured to use 'conda activate'.
```

Follow the instructions as select the shell that you are currently using (powershell in Windows, typically bash or zsh on Linux and OSX).

* IF you get an error about packages requiring cython and PyHamcrest, try the following:
```
pip install cython PyHamcrest jupyter_nbextensions_configurator
```

* IF you have warnings about missing fonts, in Ubuntu the missing fonts are in `fonts-humor-sans` (to install them: `sudo apt install fonts-humor-sans`). You may also have to clean `matplotlib`'s font cache (~/.cache/matplotlib/) and restart your current Jupyter session, for matplotlib to take notice of the changes.


* IF you have problems with widgets (conda version might not be the latest one!):
    
```
pip install --upgrade ipywidgets
    
jupyter nbextension enable --py widgetsnbextension
    
jupyter nbextension enable --py --sys-prefix widgetsnbextension
```

* IF you still have problems with widgets:

```
jupyter serverextension enable --sys-prefix jupyter_nbextensions_configurator nb_conda nb_anacondacloud nbpresent
```