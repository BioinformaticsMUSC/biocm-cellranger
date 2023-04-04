FROM bioinformaticsmusc/biocm-cellranger:1.0.0

LABEL maintainer="Bryan Granger"

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