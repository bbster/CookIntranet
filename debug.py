import os


# Setting File 불러옴
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cook_intra.settings')


def test():
    from feeds_test.models import Feed
    feeds = Feed.objects.all()
    print(feeds)


# MAIN 시작점
if __name__ == "__main__":
    import django
    django.setup(set_prefix=False)
    test()
