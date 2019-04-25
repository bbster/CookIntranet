import json

from test_plus import TestCase as DjangoTestCase


class TestCase(DjangoTestCase):
    def post(self, url_name, *args, **kwargs):
        post_data = "post_data" in kwargs and kwargs["post_data"] or None
        kwargs["extra"] = {"content_type": "application/json"}
        kwargs["data"] = json.dumps(post_data)
        return self.request('post', url_name, *args, **kwargs)
