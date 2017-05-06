SRC = py.py Object.py FileIO.py
TRG = bat.bat .gitignore
$(TRG): $(SRC)
	python $<
