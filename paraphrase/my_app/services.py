import transformers

model = transformers.PegasusForConditionalGeneration.from_pretrained("tuner007/pegasus_paraphrase")
tokenizer = transformers.PegasusTokenizerFast.from_pretrained("tuner007/pegasus_paraphrase")

def get_paraphrased_sentences(model, tokenizer, sentence, num_return_sequences=5, num_beams=5):
  # tokenize the text to be form of a list of token IDs
  inputs = tokenizer([sentence], truncation=True, padding="longest", return_tensors="pt")
  # generate the paraphrased sentences
  outputs = model.generate(
    **inputs,
    num_beams=num_beams,
    num_return_sequences=num_return_sequences,
  )
  # decode the generated sentences using the tokenizer to get them back to text
  return tokenizer.batch_decode(outputs, skip_special_tokens=True)

def main(text, limit):
    sentence = text
    res = get_paraphrased_sentences(model, tokenizer, sentence, num_beams=limit, num_return_sequences=limit)
    return(res)

if __name__=='__main__':
    main()