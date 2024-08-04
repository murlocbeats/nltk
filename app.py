from flask import Flask, request, jsonify
from nltk.sentiment import SentimentIntensityAnalyzer
import nltk

# تنظیم دایرکتوری محلی برای فایل‌های NLTK
nltk.data.path.append('./nltk_data') 

# ایجاد اپلیکیشن Flask
app = Flask(__name__)

# تعریف تابع تحلیل احساسات
def analyze_sentiment(text):
    analyzer = SentimentIntensityAnalyzer()
    scores = analyzer.polarity_scores(text)
    return scores

# تعریف روت برای API
@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.get_json()
    text = data.get('text', '')

    if not text:
        return jsonify({'error': 'No text provided'}), 400

    scores = analyze_sentiment(text)
    return jsonify(scores)

# اجرای اپلیکیشن
if __name__ == '__main__':
    app.run(debug=True)
