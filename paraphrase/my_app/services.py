# import transformers

# model = transformers.PegasusForConditionalGeneration.from_pretrained("tuner007/pegasus_paraphrase")
# tokenizer = transformers.PegasusTokenizerFast.from_pretrained("tuner007/pegasus_paraphrase")

# def get_paraphrased_sentences(model, tokenizer, sentence, num_return_sequences=5, num_beams=5):
#   # tokenize the text to be form of a list of token IDs
#   inputs = tokenizer([sentence], truncation=True, padding="longest", return_tensors="pt")
#   # generate the paraphrased sentences
#   outputs = model.generate(
#     **inputs,
#     num_beams=num_beams,
#     num_return_sequences=num_return_sequences,
#   )
#   # decode the generated sentences using the tokenizer to get them back to text
#   return tokenizer.batch_decode(outputs, skip_special_tokens=True)

# def main(text, limit):
#     sentence = text
#     res = get_paraphrased_sentences(model, tokenizer, sentence, num_beams=limit, num_return_sequences=limit)
#     return(res)

import nltk
from nltk.tree import Tree

def main():
    tree = nltk.Tree.fromstring('''(S (NP (NP (DT The) (JJ charming) (NNP Gothic) (NNP
Quarter) ) (, ,) (CC or) (NP (NNP Barri) (NNP Gòtic) ) ) (, ,) (VP (VBZ has) (NP (NP
(JJ narrow) (JJ medieval) (NNS streets) ) (VP (VBN filled) (PP (IN with) (NP (NP (JJ
trendy) (NNS bars) ) (, ,) (NP (NNS clubs) ) (CC and) (NP (JJ Catalan) (NNS
restaurants) ) ) ) ) ) ) )''')
                                
    def traverse_tree(tree):
    
      print(tree.label())

      for subtree in tree.subtrees():
          if isinstance(subtree, Tree):
              traverse_tree(subtree)
          else:
             if subtree.label() == "NP" and ("," in [t[0] for t in subtree.leaves()] or "CC" in [t[1] for t in subtree.leaves() if type(t) == tuple]):
                  print(subtree)
             else:
                 return

    traverse_tree(tree)

if __name__=='__main__':
    main()