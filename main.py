import torch
from transformers import BertForQuestionAnswering 
from transformers import BertTokenizer
import pickle


model= BertForQuestionAnswering.from_pretrained('bert-large-uncased-whole-word-masking-finetuned-squad')
save_model = open(r"model.pickle","wb")
pickle.dump(model, save_model)
save_model.close()

tokenizer= BertTokenizer.from_pretrained('bert-large-uncased-whole-word-masking-finetuned-squad')
save_tokenizer = open(r"tokenizer.pickle","wb")
pickle.dump(tokenizer,save_tokenizer)
save_tokenizer.close()


