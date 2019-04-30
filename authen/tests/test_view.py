from base.testcase import TestCase


class Test(TestCase):
    def test(self):
        self.post(
            "/auth/member/join/",
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

        # login test
        self.post(
            "/auth/member/login/",
            post_data={
                "username": res["username"],
                "password": "pass1"
            }
        )
        self.response_200()
        res = self.last_response.json()
        token = res["token"]

        # api test
        self.get(
            '/auth/member/test/',
            header={
                "HTTP_X_USER_TOKEN": token

            }
        )
        self.response_200()
        assert self.last_response.json()["msg"] == "OK"

    # def test2(self):
    #     # 명령어: pytest -s
    #     pass
    #
    # def test_get(self):
    #     # pytest 에서의 get 예제
    #     self.get(
    #         "/auth/member/?a=1&b=2",
    #         header={
    #             "token": "token1"
    #         }
    #     )
    #     self.response_200()
    #     res = self.last_response.json()
    #     breakpoint()
    #     pass
