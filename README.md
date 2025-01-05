# Sentiment-analysis-using-NLP
Disclaimer
⚠️ Important Note:
Some parts of the code, including detailed explanations and additional implementation details, are not uploaded as files in this repository. Instead, they are included in the PDF documentation provided with this project. Please refer to the PDF file for a complete understanding of the system, including:

Detailed explanations of the machine learning algorithms used.

Additional code snippets and implementation details.

Screenshots and visualizations of the system in action

# Sentiment Analysis System - Django Web Application

Welcome to the **Sentiment Analysis System** repository! This project is a Django-based web application designed to perform sentiment analysis on textual data using machine learning algorithms such as **Naive Bayes** and **Support Vector Machines (SVM)**. The system allows users to upload CSV files containing labeled text data, analyze the sentiment, and view the results in a user-friendly interface.

---

## Table of Contents
1. [Project Overview](#project-overview)
2. [Features](#features)
3. [Technologies Used](#technologies-used)
4. [Installation Guide](#installation-guide)
5. [Usage](#usage)
6. [Code Structure](#code-structure)
7. [Disclaimer](#disclaimer)
8. [Contributing](#contributing)
9. [License](#license)

---

## Project Overview

This project is a **Sentiment Analysis System** built using Django, a high-level Python web framework. The system is designed to analyze the sentiment of textual data (e.g., tweets) and classify them into positive or negative sentiments. The application uses machine learning algorithms like **Naive Bayes** and **SVM** for sentiment classification. Users can upload CSV files containing labeled data, and the system will process the data, train the models, and display the results.

---

## Features

- **User Authentication**: Admin login functionality to access the system.
- **CSV Data Upload**: Users can upload CSV files containing labeled text data for analysis.
- **Sentiment Analysis**: The system uses **Naive Bayes** and **SVM** algorithms to classify text data into positive or negative sentiments.
- **Real-Time Results**: The system provides real-time sentiment analysis results with accuracy metrics.
- **Dynamic Visualization**: Results are displayed in a user-friendly interface with detailed accuracy reports.
- **Admin Dashboard**: Admins can manage data, view analysis results, and perform actions like logging out.

---

## Technologies Used

- **Backend**: Django (Python Web Framework)
- **Frontend**: HTML, CSS, JavaScript
- **Machine Learning**: Scikit-learn (Naive Bayes, SVM)
- **Database**: SQLite (Default Django Database)
- **Data Processing**: Pandas, NumPy
- **Other Libraries**: Django-Pandas, CSV, Collections

---

## Installation Guide

### Prerequisites
- Python 3.x
- Django 3.x or higher
- Pip (Python Package Installer)

### Steps to Run the Project

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/sentiment-analysis-system.git
   cd sentiment-analysis-system
