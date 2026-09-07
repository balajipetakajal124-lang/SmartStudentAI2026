def generate_notes(topic):
    topic = topic.lower()

    notes = {
        "python": """
# 🐍 Python Notes

## What is Python?
Python is a high-level programming language.

## Features
- Easy to learn
- Object-oriented
- Open source
- Cross-platform

## Applications
- Web Development
- Artificial Intelligence
- Data Science
- Automation

## Summary
Python is one of the most popular programming languages because it is simple and powerful.
""",

        "ai": """
# 🤖 Artificial Intelligence

## Definition
Artificial Intelligence (AI) enables computers to perform tasks that normally require human intelligence.

## Types
- Narrow AI
- General AI

## Applications
- Chatbots
- Self-driving cars
- Healthcare
- Robotics

## Summary
AI helps machines learn, reason, and make decisions.
""",

        "machine learning": """
# 📊 Machine Learning

## Definition
Machine Learning is a branch of AI that allows computers to learn from data.

## Types
- Supervised Learning
- Unsupervised Learning
- Reinforcement Learning

## Applications
- Recommendation systems
- Fraud detection
- Image recognition

## Summary
Machine Learning improves predictions by learning from examples.
"""
    }

    return notes.get(
        topic,
        f"""
# 📚 {topic.title()}

Notes for this topic are not available yet.

More subjects will be added in future updates.
"""
    )
