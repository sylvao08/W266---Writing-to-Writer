# Constants for use by other modules.

# START_TOKEN = u"<s>"
# END_TOKEN   = u"</s>"
# UNK_TOKEN   = u"<unk>"

MAX_SEQUENCE_LENGTH = 500
MAX_NUM_WORDS = 100000 # the number of words/tokens from training corpus to include into the embedding
EMBEDDING_DIM = 100 # the number of element for one word in Glove Embedding

# Select label from available labels: 'gender', 'age', 'industry', 'sign'.
SELECT_LABEL = 'gender'
SAMPLE_RATE = 0.1

BASE_DATA_DIR = '../data'
RAW_TEXT_DIR = BASE_DATA_DIR + '/blogs'
ITM_DATA_DIR = BASE_DATA_DIR + '/intermediate'
GLOVE_DIR = BASE_DATA_DIR + '/glove.6B'
LOG_DIR = '..\log_'+SELECT_LABEL

TOKEN_DIR = ITM_DATA_DIR + '/' + SELECT_LABEL + '_tokenizer.pickle'
PRCD_DATA_DIR = ITM_DATA_DIR + '/' + SELECT_LABEL + '_model_data_full.pickle'
SAMPLE_DATA_DIR = ITM_DATA_DIR + '/' + SELECT_LABEL + '_model_data_sample.pickle'
