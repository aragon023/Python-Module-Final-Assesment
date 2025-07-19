# This script populates the database with initial articles data.
from articles_data import db, Article
from app import app

articles_data = [
    {
        'title': '10 Best AI tools for creative work',
        'tag': 'TECHNOLOGY',
        'summary': 'AI is redefining how professionals across departments think, plan, and execute creative work...',
        'image': 'images/home/articles/article_3_AI_Tools.jpg',
        'link': 'articles/article-2.html'
    },
    {
        'title': 'Account Based Marketing: Time for a strategic approach',
        'tag': 'STRATEGY',
        'summary': 'Account-Based Marketing (ABM) flips the traditional marketing funnel by focusing on high-value accounts...',
        'image': 'images/home/articles/article_2_people_office.jpg',
        'link': 'articles/article-3.html'
    },
    {
        'title': 'Unlocking Growth: Applying the 10 Types of Innovation Across Industries',
        'tag': 'INNOVATION',
        'summary': 'The Ten Types of Innovation framework by Doblin offers a holistic approach to innovation...',
        'image': 'images/home/articles/article_1_people_brainstorming.jpg',
        'link': 'articles/article-1.html'
    }
]

with app.app_context():
    for data in articles_data:
        existing = Article.query.filter_by(title=data['title']).first()
        if not existing:
            article = Article(
                title=data['title'],
                tag=data['tag'],
                summary=data['summary'],
                image=data['image'],
                link=data['link']
            )
            db.session.add(article)
            print(f"Added: {data['title']}")
        else:
            print(f"Skipped (already exists): {data['title']}")
    db.session.commit()
    print("All articles added or skipped (no duplicates).")
