from setuptools import find_packages, setup

setup(
    name="Ecommercebot",
    version="0.0.1",
    author="SHAILESH",
    author_email="skk.jodhpur@gmail.com",
    packages=find_packages(),
    install_requires=['langchain-astradb','langchain ','langchain-openai','datasets','pypdf','python-dotenv','flask','langchain_google_genai']
)