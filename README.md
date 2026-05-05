# Ergodic Decision Process of Collective Reasoning Intelligence for Explainable Scientific Discovery

## Abstract

Deriving governing equations from empirical observations is a longstanding challenge in science. However, the discovery of explainable and extrapolatable equations remains a fundamental limitation of modern AI, posing a central bottleneck for AI-driven scientific discovery. In this paper, we propose collective reasoning intelligence for symbolic optimization (CRISO), an ergodic collective decision process for autonomous discovery of explainable and extrapolatable scientific equations through evolutionary hypothesis generation, evaluation, critique, and consolidation across multiple reasoning agents. Across scientific systems governed by deterministic, stochastic, and previously uncharacterized dynamics, CRISO autonomously recovered the underlying governing equations and achieved state-of-the-art accuracy without any human feedback and additional finetuning. The resulting equations reduced extrapolation error by up to six orders of magnitude relative to deep neural networks, while condensing 0.5-1 million model parameters into just 5–40 constants.

---

## Run
- Please download and install Ollama from https://ollama.com/download.
- Download the Mixtral:8x7b model via https://ollama.com/library/mixtral.
- Execute ``exec.py`` in this repository.

---

## Benchmark Symbolic Degression Datasets

- The training and evaluation datasets of the Chi2PDF, NNN, FHST, NOMC, and HHM problems are available at https://github.com/ngs00/mci.
- The training and evaluation datasets of the NDO, MSB, and ECGB problems are available at https://github.com/deep-symbolic-mathematics/LLM-SR. The original problem names of NDO, MSB, and ECBG in the LLM-SR repository are oscillator2, stressstrain, and bactgrow, respectively.
- The original data source of the BDC problem is https://github.com/alg-x/Battery-Capacity-Prediction-Using-Regression.
- The original dataset of the SFL problem is available at https://link.springer.com/article/10.1186/2193-9772-3-8#MOESM1.

---

## Run with User-Defined Datasets

- You need to prepare ``train`` and ``test`` datasets for deriving equations and evaluating them, respectively.
- Then, add the configuration of your dataset into the ``config`` variable in ``exec.py``.
- Finally, set the values of the ``tast_domain`` and ``dataset_name`` variables in ``exec.py``.
