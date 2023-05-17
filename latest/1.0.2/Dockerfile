FROM bioinformaticsmusc/biocm-cellranger:1.0.1

LABEL maintainer="Bryan Granger"

ENV PATH ~/bin:$PATH

ARG SPACERANGER_VERSION="2.0.1"

ARG SPACERANGER_DOWNLOAD_URL="https://cf.10xgenomics.com/releases/spatial-exp/spaceranger-2.0.1.tar.gz?Expires=1684373678&Policy=eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiaHR0cHM6Ly9jZi4xMHhnZW5vbWljcy5jb20vcmVsZWFzZXMvc3BhdGlhbC1leHAvc3BhY2VyYW5nZXItMi4wLjEudGFyLmd6IiwiQ29uZGl0aW9uIjp7IkRhdGVMZXNzVGhhbiI6eyJBV1M6RXBvY2hUaW1lIjoxNjg0MzczNjc4fX19XX0_&Signature=gn1J4QdweSVDu7EJDG28AHM6GQRNs3g-ixSajw3S2zmxy9OcR68Fo1e0ujDMQHsNjcWDjQkQXJzaft~VsWNaiKH1QQJOGY4MkoyNNLEHCtFXoZJeRBFDbwr3LiRmfcrBGo2KB4lQKpt~aQ0jDWtBHCdfirMStKmVQDYKZtjqTNyYMuXrS87Zj0p95fD8UneeEKra40H3R4LDZM7Xe7nWUoggwRmk51hz6-VljNt2XITlqFYRKuyoIoLPK~Tk1kCmpsf8I8~h1hczGwswc7LzUMFTN28E-wXbkzaE5Wgr~e7Ww577D4AzTrdS-b~oZsSDM3oMDuKRXz1nOWTqvFQmMg__&Key-Pair-Id=APKAI7S6A5RYOXBWRPDA"

ENV PATH /opt/spaceranger-${SPACERANGER_VERSION}:$PATH

RUN curl -o spaceranger-${SPACERANGER_VERSION}.tar.gz ${SPACERANGER_DOWNLOAD_URL} \
 	&& tar xzf spaceranger-${SPACERANGER_VERSION}.tar.gz \
    && rm -rf spaceranger-${SPACERANGER_VERSION}.tar.gz 

WORKDIR /opt