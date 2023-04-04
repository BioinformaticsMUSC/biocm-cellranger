# biocm-cellranger docker container

This is a dockerfile for a container to be used via Sigularity on the 
Palmetto cluster. The container comes with Cell Ranger, Cell Ranger ATAC, and Cell Ranger ARC installed on it. It also contains a script to help generate PBS batch job files.

## Example usage

This container can be used interactively or with a batch job submission. For Cell Ranger, a batch job submission is ideal.


### Batch job use

For a batch job, use the following code:
```
cd /zfs/musc3/singularity_images

singularity exec -B /zfs/musc3:/mnt --pwd /mnt/project_directory/output_directory biocm-cellranger_latest.sif cellranger count \
   --id=run_count_1kpbmcs \
   --fastqs=/mnt/home/user.name/yard/run_cellranger_count/pbmc_1k_v3_fastqs \
   --sample=pbmc_1k_v3 \
   --transcriptome=/mnt/home/user.name/yard/run_cellranger_count/refdata-gex-GRCh38-2020-A
```
Note the following options:
- `-B /zfs/musc3:/mnt`: this command creates a link between the source directory (here, `/zfs/musc3`) and the destination directory inside the container `/mnt`. You may link any source directory--those directories and files will then be accessible inside the container. If you save anything within those directories inside the container, it will exist when the container is done. It's helpful to create a new directory (for example: cellranger_run_outputs) as the source directory; the outputs will be saved there.

Note that if you are accessing FASTQ files and library CSV files, they need to be located within the source directory above so that they can be accessed within the container. The outputs must also be saved within the `/mnt` directory for it to be saved outside the container.

- `--pwd /mnt`: this sets the working directory inside the container to `/mnt/project_directory/output_directory`, which is the mounted volume linked to the source directory.

It is not necessary to add any modules.

### Interactive use

Navigate to the `singularity_images` folder:
```
cd /zfs/musc3/singularity_images
```

Use the following command to open a shell command prompt:

```
singularity shell -B /zfs/musc3:/mnt --pwd /mnt biocm-cellranger_latest.sif
```

Note the same options as above.

Once inside the container, you can run cellbender as usual:
```
cellranger count \
   --id=run_count_1kpbmcs \
   --fastqs=/mnt/home/user.name/yard/run_cellranger_count/pbmc_1k_v3_fastqs \
   --sample=pbmc_1k_v3 \
   --transcriptome=/mnt/home/user.name/yard/run_cellranger_count/refdata-gex-GRCh38-2020-A
```

### Generate CR scripts
Use the command `generateCRscript` to create a PBS job script for cellranger count (default) or cellranger multi. The command takes the following arguments:
```
-s --sample_name (required) This is the name of the sample according to the fastq file (e.g. 7166-MR-43)
-i --job_id (optional) This is the name of the PBS job and cellranger output folder (if not included, the sample_name will be used)
-r --results_directory (optional) path to the directory where the CR outs will be saved
-f --fastqs (required for COUNT) path to the directory with fastq files in it
-t --transcriptome (required for COUNT) path to the directory with the 10X reference
-c --csv (required for MULTI) path to the CSV file required by cellranger multi
-o --output (optional) filepath and filename for the created .pbs file (if not included, it will save as {sample_name}.pbs)
```

### What's new

2/23/23 - Version 1.0.0
Cell Ranger versions:
- Cell Ranger: 7.1.0
- Cell Ranger ARC: 2.0.2
- Cell Ranger ATAC: 2.1.0

