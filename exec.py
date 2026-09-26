import torch
from util.data import *
from mci.search import Search
from mci.util import *


config = {
    'chi2pdf': {
        'domain': 'statistics',
        'idx_inputs': [0, 1],
        'idx_target': 2
    },
    'fhst': {
        'domain': 'polymer science',
        'idx_inputs': [0, 1, 2],
        'idx_target': 3
    },
    'hhm': {
        'domain': 'mathematical biology',
        'idx_inputs': [0, 1, 2, 3, 4],
        'idx_target': 5
    }
    'ndo': {
        'domain': 'physics',
        'idx_inputs': [0, 1, 2],
        'idx_target': 3
    },
    'nnn': {
        'domain': 'machine learning',
        'idx_inputs': [0, 1],
        'idx_target': 2
    },
    'ecbg': {
        'domain': 'mathematical biology',
        'idx_inputs': [0, 1, 2, 3],
        'idx_target': 4
    },
    'msb': {
        'domain': 'materials science',
        'idx_inputs': [0, 1],
        'idx_target': 2
    },
    'bdc': {
        'domain': 'materials science',
        'idx_inputs': [0, 1, 2, 3, 4, 5],
        'idx_target': 7
    },
    'sfl': {
        'domain': 'materials science',
        'idx_inputs': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
        'idx_target': 10
    },
    'nomc': {
        'domain': 'organic chemistry',
        'idx_inputs': [0, 1, 2, 3, 4, 5],
        'idx_target': 10
    }
}


device = torch.device('cuda:0')
task_domain = 'polymer science'
dataset_name = 'fhst'


if __name__ == '__main__':
    dataset_train = load_dataset('dataset/{}/train.csv'.format(dataset_name),
                                 idx_inputs=config[dataset_name]['idx_inputs'],
                                 idx_target=config[dataset_name]['idx_target'])
    dataset_test = load_dataset('dataset/{}/test_id.csv'.format(dataset_name),
                                idx_inputs=config[dataset_name]['idx_inputs'],
                                idx_target=config[dataset_name]['idx_target'])
    instruction = read_problem_instruction('res/instruction_{}.txt'.format(dataset_name))

    search = Search(task_domain, dataset_train, instruction, num_agents=50, device=device, llm=LLM_MIXTRAL)
    best_solution = search.run(max_iters=100, log_file='exec_log_{}.txt'.format(dataset_name))

