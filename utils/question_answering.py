from transformers import pipeline

qa_model = pipeline("question-answering")

def answer_question(context, question):
    answer = qa_model(question=question, context=context)
    return answer['answer']
