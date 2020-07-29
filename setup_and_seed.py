from techtest.models import *
from techtest.models.author import Author
from techtest.models.article import Article
from techtest.models.region import Region
from techtest.connector import engine, BaseModel, db_session

BaseModel.metadata.create_all(engine)

with db_session() as session:
    author = Author(first_name='Bel', last_name='Cruz')
    au = Region(code="AU", name="Australia")
    uk = Region(code="UK", name="United Kingdom")
    us = Region(code="US", name="United States of America")
    session.add_all([
        author,
        au,
        uk,
        us,
    ])
    session.flush()
    session.add_all([
        Article(
            title='Post 1',
            content='This is a post body',
            regions=[au, uk],
            author=author.id,
        ),
        Article(
            title='Post 2',
            content='This is the second post body',
            regions=[au, us],
            author=author.id,
        ),
    ])
