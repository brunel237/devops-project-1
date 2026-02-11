install:
	#install commands
	pip install --upgrade pip &&\
		pip install -r requirements.txt
format:
	#
lint:
	#
test:
	#
deploy:
	#
all: install lint test deploy