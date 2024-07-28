Quiz Application

Description

A dynamic quiz application designed to test knowledge across various categories. It features a user-friendly interface, real-time results, and a shuffle mechanism for questions. Users can take quizzes, view their results, and navigate through categories seamlessly.

Features

- Category-Based Quizzes: Choose from various categories and take quizzes specific to your interests.
- Dynamic Question Loading: Questions are loaded dynamically based on the selected category.
- Shuffle Mechanism: Questions are shuffled to ensure a unique quiz experience every time.
- Real-Time Results: View your score and total marks immediately after submitting the quiz.
- Add/Edit Questions: Admin functionality to add or edit quiz questions and answers.

Technologies Used

- Python: Backend development using Django.
- HTML/CSS: Frontend design and styling.
- JavaScript/jQuery: For dynamic content and AJAX requests.
- Bootstrap: Styling and responsive design.

 ## How to Run the Application
You can make directory then add all this files in that, you need to add html files in new directory by creating in home app called template, after adding code of model.py or making changes in it, you have to type python manage.py makemigrations and then python manage.py migrate, then you can runserver to start quiz app, you need to have little knowldge of django to make app using this code files.
I have uploaded video you can watch how app is running.
1. Clone the Repository:

   git clone https://github.com/M-Usama04/Python-Quiz-App.git
   cd Python-Quiz-App.git

2. Install Dependencies:
   EnsuRun the Development Server:
   Start the Django development server:
 
   python manage.py runserver
  

   Access the Application:
   Open your web browser and go to `http://127.0.0.1:8000/` to use the application.
   You can then select category for which subject you want to give quiz, then attempt quiz, option will display, you
   have button below 'Edit Quiz' which will redirect you to admin page for editing quiz, adding questions, etc, when    you click 'submit quiz' button result will be displayed, you can attempt quiz again.

## Accessing the Admin Interface

To manage categories, questions, and answers, log in to the Django admin interface at `http://127.0.0.1:8000/admin/`
## Adding Questions

1. Go to the admin interface and select `Questions`.
2. Click on `Add Question` to enter a new question.
3. Add possible answers and mark the correct answer.

