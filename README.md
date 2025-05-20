Hospital Chatbot – CityCare Assistant
A simple yet functional rule-based chatbot for CityCare Hospital, developed using Python, NLP (Natural Language Processing), and machine learning. This chatbot helps users with common queries such as hospital timings, doctor availability, appointment booking, COVID-19 guidelines, emergency instructions, and more.

Technologies Used
Python

Natural Language Toolkit (nltk)

Scikit-learn (Naive Bayes Classifier)

Pickle (Model Serialization)

JSON (Intent definitions)

Features
Understands and responds to user queries based on predefined intents

Trained using sample patterns and tags in intents.json

Uses CountVectorizer for text vectorization

Trained with Multinomial Naive Bayes for intent classification

Provides dynamic and random responses for each recognized intent

Includes a simple terminal-based conversation loop

Supported Intents
The chatbot can respond to:

Greetings and farewells

Booking or canceling appointments

Doctor availability queries

Emergency instructions

Hospital departments and timings

Payment methods and insurance

COVID-19 protocols

Visitor policies

Lab tests availability
