.PHONY: clean help

REDNOSE_EXISTS = $(shell nosetests --plugins | grep rednose)
ifneq "$(REDNOSE_EXISTS)" ""
    NOSE_OPTS = --rednose
endif

test:
	nosetests $(NOSE_OPTS)

clean:
	rm -f timesheets/*.pyo timesheets/*.pyc

help:
	@echo "test:   run the test suite"
	@echo "clean:  remove automatically generated files"
