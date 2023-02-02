FROM fuzzers/atheris:2.0.7-python3.9

# Build
RUN pip install base58

ADD ./mayhem/fuzz_base58.py /fuzz_base58.py

CMD ["/fuzz_base58.py"]
