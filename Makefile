.PHONY: test release doc

test:
	flake8 formulator --ignore=E501,E127,E128,E124 --filename=*.py --exclude=static,migrations,tests
	coverage run --branch --source=formulator `which django-admin.py` test formulator --settings=formulator.test_settings
	coverage report --omit=formulator/test*

release:
	python setup.py sdist bdist_wheel register upload -s

doc:
	cd docs; make html; cd ..
