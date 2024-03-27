# SpeakWiz

Raise your confidence in English by practicing and speaking with this platform. 

Here you will find endless of cards about different topics to practice English and take your skills to the next level.

The project was made with Django Rest Framework and React


## Features
- New cards with questions are generated using LLM.
- Current cards are translated to other languages using LLM.   
- Access both free and premium cards. To unlock premium content, simply create an account.
- You can save your cards in your favorite section.
- You can give us your feedback, it will be useful to create new topics.

## Installation

#### Back End:

1. Set the next environment variables inside of .env file in ***src/*** dir:
```
    DJANGO_SECRET_KEY
    OPENAI_API_KEY
    REDIS_USER
    REDIS_PASSWORD
```

2. Install dependencies:
```
pip install -r requirements.txt
```

3. Run server:
```
python manage.py runserver
```

4. First, make sure you have running redis in your computer and run the celery worker.
In the ***src/*** dir run the next command:
```
celery -A main worker -l INFO
```

5. Run celery beat:
```
celery -A main beat -l INFO
```

#### Front End:
1. Set the environment variables inside of .env file in ***front/*** dir:
```
    REACT_APP_API_URL
```

2. Install dependencies
```
npm i
```

3. Run
```
npm start
```

## Screenshot
![Home](https://github.com/alejandrosoares/SpeakWiz/assets/48335948/0774c0c1-8091-4b4e-9fdd-6ec401db959d)
![Card](https://github.com/alejandrosoares/SpeakWiz/assets/48335948/b3e943ce-cf36-4368-a0a0-97154d573aca)