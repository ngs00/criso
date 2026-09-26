# Convergent Decision Processes of Collective Reasoning Intelligence for Explainable Scientific Discovery

## Abstract

Deriving extrapolatable symbolic laws from empirical observations remains a central bottleneck in AI-driven scientific discovery. We propose collective reasoning intelligence for symbolic optimization (CRISO), a multi-agent framework for autonomous equation discovery without expert feedback, task-specific finetuning, or external scientific tools and knowledge bases. CRISO distills collectively selected best hypothesis into reusable scientific statements, accumulates them as shared context, and broadcasts to a population of reasoning agents, thereby implementing a collectively evolving symbolic regression. Consequently, CRISO evolves the hypothesis search toward promising regions without additional finetuning of the backbone LLM. Across ten nonlinear, stochastic, or previously uncharacterized scientific systems, CRISO outperformed or matched state-of-the-art combinatorial and recent LLM-based symbolic regression methods, including under out-of-distribution evaluation. On an in-house chemical reactor whose dynamics lie beyond the backbone LLM's prior knowledge, CRISO derived a symbolic equation with 38.02% lower generalization error than all baselines, demonstrating its scientific discovery capability beyond static LLM priors.

---

## Run
- Please download and install Ollama from https://ollama.com/download.
- Download the Mixtral:8x7b model via https://ollama.com/library/mixtral.
- Execute ``exec.py`` in this repository.

---

## Benchmark Symbolic Degression Datasets

- The training and evaluation datasets of the Chi2PDF, NNN, FHST, NOMC, and HHM problems are available at this repository.
- The training and evaluation datasets of the NDO, MSB, and ECGB problems are available at https://github.com/deep-symbolic-mathematics/LLM-SR. The original problem names of NDO, MSB, and ECBG in the LLM-SR repository are oscillator2, stressstrain, and bactgrow, respectively.
- The original data source of the BDC problem is https://github.com/alg-x/Battery-Capacity-Prediction-Using-Regression.
- The original dataset of the SFL problem is available at https://link.springer.com/article/10.1186/2193-9772-3-8#MOESM1.

---

## Run with User-Defined Datasets

- You need to prepare ``training`` and ``test`` datasets for deriving equations and evaluating them, respectively.
- Then, add the configuration of your dataset into the ``config`` variable in ``exec.py`` and write an instruction of the problem.
- Finally, set the values of the ``task_domain`` and ``dataset_name`` variables in ``exec.py``.
- ``dataset`` and ``res`` folders provide examples of the datasets and associated instructions.
