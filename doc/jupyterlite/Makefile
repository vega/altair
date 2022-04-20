all:
	rm files/*.ipynb -f
	cp ../../altair/examples/[a-z]*.py files/
	cp wellcome.ipynb files/
	for file_name in files/*.py; do echo $$file_name; cat file_prefix $$file_name | jupytext --from py:percent --to notebook --set-kernel python3 -o $${file_name%.*}.ipynb; done
	sed s/python3/python/ files/*.ipynb -i
	rm files/*.py
