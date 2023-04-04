FROM bioinformaticsmusc/biocm-cellranger:1.0.0

LABEL maintainer="Bryan Granger"

ENV PATH ~/bin:$PATH

RUN apt-get update && apt-get install -y wget nano

RUN wget https://raw.githubusercontent.com/BioinformaticsMUSC/biocm-cellranger/main/files/gen_cr_script.py \
    && chmod +x gen_cr_script.py \
    && mkdir ~/bin \
    && mv gen_cr_script.py ~/bin/generateCRscript

WORKDIR /opt