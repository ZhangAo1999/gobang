from setuptools import setup


setup(
    name="gobang",
    version="0.2.0",
    author="zh_ang_ao",
    author_email="804951563@qq.com",
    url="暂无",
    description="games of gobang",
    packages={"gobang"},
    platforms='any',
    package_data={
        "gobang": ['ziti/*']
    }
)

