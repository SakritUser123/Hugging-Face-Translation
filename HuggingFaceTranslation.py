from transformers import pipeline
pipe = pipeline('translation', model="Helsinki-NLP/opus-mt-en-ru")

word = input("Enter Words to Translate")
print(pipe(word))
