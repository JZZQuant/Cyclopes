FROM continuumio/miniconda3

RUN  conda config --add channels conda-forge
RUN  conda install -c conda-forge tensorflow
RUN  conda update conda
RUN  conda config --set always_yes true
RUN  conda config --set quiet true
RUN  conda install conda-build
