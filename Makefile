SRC = py.py Object.py String.py Vector.py FileIO.py
TRG = bat.bat .gitignore
$(TRG): $(SRC)
	python $< > log.log
