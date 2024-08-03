#############################
FILENAME := index.py
SCRIPT ?= index.py

check:
	ruff check --fix

format:
	ruff format --config indent-width=2

script:
	python3 $(SCRIPT)

install:
	pip3 install -r requirements.txt

initialize:
	python3 -m pipreqs.pipreqs --encoding=utf8 --force

generate:
	teo generate entity

start:
	python3 index.py serve

pm2-start:
	pm2 start index.py --interpreter python3 --name teo-demo

pm2-restart:
	pm2 stop teo-demo
	pm2 del teo-demo
	make install
	pm2 start index.py --interpreter python3 --name teo-demo
