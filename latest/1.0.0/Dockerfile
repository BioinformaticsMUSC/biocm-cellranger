FROM ubuntu:latest

LABEL maintainer="Bryan Granger"

ARG CELLRANGER_VERSION="7.1.0"
ARG ARC_VERSION="2.0.2"
ARG ATAC_VERSION="2.1.0"

ARG CELLRANGER_DOWNLOAD_URL="https://cf.10xgenomics.com/releases/cell-exp/cellranger-7.1.0.tar.gz?Expires=1677219156&Policy=eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiaHR0cHM6Ly9jZi4xMHhnZW5vbWljcy5jb20vcmVsZWFzZXMvY2VsbC1leHAvY2VsbHJhbmdlci03LjEuMC50YXIuZ3oiLCJDb25kaXRpb24iOnsiRGF0ZUxlc3NUaGFuIjp7IkFXUzpFcG9jaFRpbWUiOjE2NzcyMTkxNTZ9fX1dfQ__&Signature=W8~qck0d6VwYpmlTDG1~KHeWgENS5RE7R6XkeUpd96ZjNVuPW2ofUC37LZge6AYHSjB52enQJvxStfyy0ektFTp4HBBkAXILgpEcrV7MdC1Hcw5cf4QPyBlMEAgOBKzebdryEjOc0B-tJpf8oeO0bPfI8tR6tZG6eYx9fnUS7CQkUGKPmLj-E4cYqaLdHetyxwPuBuNn9VhD-5YEDgXvMxhVrdcECWZ64Li3CUSj2dkS27VT41DUeLDmGzdYa-ouBEOIX8bfqtEiit4A6m7SLHqZMCsloAp6GD9jGKC2w3OKrJZI1NcJQTIkEAR1Qe4HJXyl6qAd4HBHBTe9s75Uog__&Key-Pair-Id=APKAI7S6A5RYOXBWRPDA"

ARG ARC_DOWNLOAD_URL="https://cf.10xgenomics.com/releases/cell-arc/cellranger-arc-2.0.2.tar.gz?Expires=1677219481&Policy=eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiaHR0cHM6Ly9jZi4xMHhnZW5vbWljcy5jb20vcmVsZWFzZXMvY2VsbC1hcmMvY2VsbHJhbmdlci1hcmMtMi4wLjIudGFyLmd6IiwiQ29uZGl0aW9uIjp7IkRhdGVMZXNzVGhhbiI6eyJBV1M6RXBvY2hUaW1lIjoxNjc3MjE5NDgxfX19XX0_&Signature=EAHyERNBBbCZL3f-7niRmlRmEqap7n9k4xXeIsZNXeMuJc8ZJhG-ChvNjDErg7YkfBA~-MkFwYFFm6fZBwrNW2BLGlKLmxSRAzfkU99CXEaGN8yH3kdSsmM-EmeWE4J1HUTcn0yd-~WwdYdzsog8cXRe8Mc6rig63GTF~--AfzWeGNk8vtGxicw-Lx4E20sZFwnU6xKmYXgcmdE6bpmTI7YPlx7nt9Tt1ruHvWKO0IgBtHsNenUQ7JoeMAk0pqdWkS9WQwWfQwZSon00RPjm7VBENQzB~hueEYC7OEj2WDu-cW0BztmiUaGkWeYvEWK~lXkQUD~Qj9enoq4lmcqYmQ__&Key-Pair-Id=APKAI7S6A5RYOXBWRPDA"

ARG ATAC_DOWNLOAD_URL="https://cf.10xgenomics.com/releases/cell-atac/cellranger-atac-2.1.0.tar.gz?Expires=1677219520&Policy=eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiaHR0cHM6Ly9jZi4xMHhnZW5vbWljcy5jb20vcmVsZWFzZXMvY2VsbC1hdGFjL2NlbGxyYW5nZXItYXRhYy0yLjEuMC50YXIuZ3oiLCJDb25kaXRpb24iOnsiRGF0ZUxlc3NUaGFuIjp7IkFXUzpFcG9jaFRpbWUiOjE2NzcyMTk1MjB9fX1dfQ__&Signature=Ul2rPUavdduP0O~L3E46DrTBr2cXaXG01zMzdbdtbq5YU5Wjzw9US9ub9rFY5dijjO5UuTokaFVHyG1JEycyeu5tqKty-QcZR5P-Sz4Thxk2hKXyY3cBatLbs2-GGyaf6Toc079~ibwKFui-PfR1BbAu0pg13R3TS8ZIG34M6FJN~KpFVygElsdhnX9DhvTV6~PU1Pm71gghTOOFk2I6G~6OpmUD8IDISmBk2Ess2Crgfu83WrkOAb1ToGg1Z8q8I4Ze407jErS99Gv9WxId860CF9S3rQGZmInT04lFw~ETCo21PkXZGnv5aH70k-hKOiPGGQWaZ2KgAYIgiq~j8Q__&Key-Pair-Id=APKAI7S6A5RYOXBWRPDA"

ENV PATH /opt/cellranger-${CELLRANGER_VERSION}:$PATH
ENV PATH /opt/cellranger-arc-${ARC_VERSION}:$PATH
ENV PATH /opt/cellranger-atac-${ATAC_VERSION}:$PATH

RUN apt-get update && apt-get install -y curl

# cell ranger binaries GEX/VDJ/FB/MULTI
RUN curl -o cellranger-${CELLRANGER_VERSION}.tar.gz ${CELLRANGER_DOWNLOAD_URL} \
    && tar xzf cellranger-${CELLRANGER_VERSION}.tar.gz \
    && rm -rf cellranger-${CELLRANGER_VERSION}.tar.gz \
    && mv cellranger-${CELLRANGER_VERSION} /opt/

# cellranger ARC binaries - for multi-omic GEX + ATAC
RUN curl -o cellranger-arc-${ARC_VERSION}.tar.gz ${ARC_DOWNLOAD_URL} \
    && tar xzf cellranger-arc-${ARC_VERSION}.tar.gz \
    && rm -rf cellranger-arc-${ARC_VERSION}.tar.gz \
    && mv cellranger-arc-${ARC_VERSION} /opt/

# cellranger ATAC binaries - for ATAC only
RUN curl -o cellranger-atac-${ATAC_VERSION}.tar.gz ${ATAC_DOWNLOAD_URL} \
    && tar xzf cellranger-atac-${ATAC_VERSION}.tar.gz \
    && rm -rf cellranger-atac-${ATAC_VERSION}.tar.gz \
    && mv cellranger-atac-${ATAC_VERSION} /opt/

WORKDIR /opt