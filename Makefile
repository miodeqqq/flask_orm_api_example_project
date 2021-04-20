.PHONY: clean tests

clean:
	clear; rm -rf **/*.pyc && \
    rm -rf ./.cache/ && \
    rm -rf .DS_Store && \
    rm -rf .idea && \
    rm -rf *.json && \
    rm -rf *.png && \
    rm -rf *.db && \
    rm -rf *.csv && \
    find . -name ".DS_Store" -print -delete && \
    find . -name "*.pyc" -exec rm -f {} \; && \
    find . -type d -name __pycache__* -exec rm -r {} \+

black:
	clear;poetry run black .

runserver:
	clear; poetry run flask run
