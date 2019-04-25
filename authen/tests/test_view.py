from base.testcase import TestCase


class Test(TestCase):
    def test(self):
        self.post(
            "/auth/member/",
            post_data={
                "username": "010-2386-8724",
                "password": "pass1",
                "first_name": "진환",
                "last_name": "정"
            }
        )
        self.response_201()
        res = self.last_response.json()
        assert res["username"] == "010-2386-8724"

    def test2(self):
        # 명령어: pytest -s
        # breakpoint() 를 활용하자
        pass
