<img src="https://github.com/Nixtla/nixtla/blob/master/nbs/indx_imgs/nixtla_logo.png">

# Deep Learning for Time Series Forecasting
> [nikstla] (noun, nahuatl) Period of time.

[![Python 3.7](https://img.shields.io/badge/python-3.7-blue.svg)](https://www.python.org/downloads/release/python-370/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://github.com/kdgutier/esrnn_torch/blob/master/LICENSE)

State-of-the-art time series forecasting for pytorch.

Nixtla is a python library for time series forecasting with deep learning. 
It provides dataset loading utilities, evaluation functions and pytorch implementations of state of the art deep learning forecasting models.


## Documentation
XXX Here is a link to the [documentation](https://pypi.org).


## Installation

### Stable version

This code is a work in progress, any contributions or issues are welcome on
GitHub at: https://github.com/Nixtla/nixtla.

You can install the *released version* of `Nixtla` from the [Python package index](https://pypi.org) with:

```python
pip install nixtla
```

(installing inside a python virtualenvironment or a conda environment is recommended).


#### Development version in development mode

If you want to make some modifications to the code and see the effects in real time (without reinstalling), follow the steps below:

```bash
git clone https://github.com/Nixtla/nixtla.git
cd nixtla
nbdev_build_lib
pip install -e .
```

## Current available models

* [Exponential Smoothing Recurrent Neural Network (ES-RNN)](https://www.sciencedirect.com/science/article/pii/S0169207019301153): A hybrid model that combines the expressivity of non linear models to capture the trends while it normalizes using a Holt-Winters inspired model for the levels and seasonals.  This model is the winner of the M4 forecasting competition.

* [Neural Basis Expansion Analysis (N-BEATS)](https://arxiv.org/abs/1905.10437): A model from Element-AI (Yoshua Bengio’s lab) that has proven to achieve state of the art performance on benchmark large scale forecasting datasets like Tourism, M3, and M4. The model is fast to train an has an interpretable configuration.

* [Neural Basis Expansion Analysis with Exogenous Variables (N-BEATSx)](https://arxiv.org/abs/2104.05522): The neural basis expansion with exogenous variables is an extension to the original N-BEATS that allows it to include time dependent covariates.

## Authors
This repository began with joint efforts from AutonLab researchers at Carnegie Mellon University and Abraxas data scientists.

## License
This project is licensed under the MIT License - see the [LICENSE](https://github.com/nixtla/nixtla/blob/master/LICENSE) file for details.

## How to cite

If you use `Nixtla` in a scientific publication, we encourage you to add
the following references to the related papers:


```bibtex
@article{nixtla_arxiv,
  author  = {XXXX},
  title   = {{Nixtla: Deep Learning for Time Series Forecasting}},
  journal = {arXiv preprint arXiv:XXX.XXX},
  year    = {2021}
}
```
