import yaml

import pytest as pytest


class TestDemo:
    @pytest.mark.parametrize("env", yaml.safe_load(open("./env.yaml")))
    def test_demo(self, env):
        if "test" in env:
            print("这是测试环境！")
            print(env)
            print("测试环境的ip是", env["test"])
        elif "dev" in env:
            print("这是开发环境！")
            print(env)
            print("开发环境的ip是", env["dev"])

    def test_yaml(self):
        print(yaml.safe_load(open("./env.yaml")))