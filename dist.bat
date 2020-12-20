cd dist
del *.* /Q
cd ..

python setup.py sdist bdist_wheel
python -m twine upload --repository pypi dist/*
