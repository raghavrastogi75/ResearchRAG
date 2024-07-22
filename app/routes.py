from flask import Blueprint, request, jsonify
from utils.pdf_extraction import extract_text_from_pdf
from utils.summarization import summarize_text
from utils.question_generation import generate_questions
from utils.question_answering import answer_question

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return "Hello, ResearchPaperQnA!"

@main.route('/extract', methods=['POST'])
def extract():
    file = request.files['file']
    text = extract_text_from_pdf(file)
    return jsonify({'text': text})

@main.route('/summarize', methods=['POST'])
def summarize():
    text = request.json['text']
    summary = summarize_text(text)
    return jsonify({'summary': summary})

@main.route('/generate-questions', methods=['POST'])
def generate():
    text = request.json['text']
    questions = generate_questions(text)
    return jsonify({'questions': questions})

@main.route('/answer', methods=['POST'])
def answer():
    context = request.json['context']
    question = request.json['question']
    answer = answer_question(context, question)
    return jsonify({'answer': answer})
