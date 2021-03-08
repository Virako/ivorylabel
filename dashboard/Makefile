lint:
	prospector

mypy:
	mypy --exclude "manage.py|migrations|tests.py" .

test:
	pytest -svv

cov:
	coverage run --source=. -m pytest
	coverage report
	coverage html
