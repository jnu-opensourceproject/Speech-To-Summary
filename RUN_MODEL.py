import torch
from transformers import PreTrainedTokenizerFast
from transformers import BartForConditionalGeneration

model = BartForConditionalGeneration.from_pretrained('./kobart_sum')
tokenizer = PreTrainedTokenizerFast.from_pretrained('gogamza/kobart-base-v1')

text = input()

if text:
    input_ids = tokenizer.encode(text)
    input_ids = torch.tensor(input_ids)
    input_ids = input_ids.unsqueeze(0)
    output = model.generate(input_ids, eos_token_id=1, max_length=512, num_beams=5)
    output = tokenizer.decode(output[0], skip_special_tokens=True)
    print(output)