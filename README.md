# biocm-cellranger docker container

This is a dockerfile for a container to be used via Sigularity on the 
Palmetto cluster. The container comes with Cell Ranger, Cell Ranger ATAC, Cell Ranger ARC, and Space Ranger installed on it. It also contains a script to help generate PBS batch job files.

## Example usage

This container can be used interactively or with a batch job submission. For Cell Ranger, a batch job submission is ideal. See below on how to use a script to generate a PBS file for batch job submission.


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

Once inside the container, you can run cellranger as usual:
```
cellranger count \
   --id=run_count_1kpbmcs \
   --fastqs=/mnt/home/user.name/yard/run_cellranger_count/pbmc_1k_v3_fastqs \
   --sample=pbmc_1k_v3 \
   --transcriptome=/mnt/home/user.name/yard/run_cellranger_count/refdata-gex-GRCh38-2020-A
```

### Generate CR scripts for batch jobs
Use the command `generateCRscript` to create a PBS job script for cellranger count (default) or cellranger multi. The command takes the following arguments:
```
-s --sample_name (required) This is the name of the sample according to the fastq file (e.g. 7166-MR-43)
   To create multiple scripts, separate multiple samples by commas (e.g. 7166-MR-43,7166-MR-44)
-i --job_id (optional) This is the name of the PBS job and cellranger output folder (if not included, the sample_name will be used)
   If creating multiple scripts, you can include as many job_ids as samples in a corresponding order
-r --results_directory (optional) path to the directory where the cellranger outputs will be saved
-f --fastqs (required for COUNT) path to the directory with fastq files in it
-t --transcriptome (required for COUNT) path to the directory with the 10X reference
--multi (required for MULTI) This is a flag to generate a multi pbs file (default is count)
-c --csv (required for MULTI) path to the CSV file required by cellranger multi
-o --output_dir (optional) directory to save the completed script(s) in - the filename will be automatically created

example for cellranger count:

generateCRscript -sample_name 7166-MR-1 \
   --job_id mouse_WT \
   --results_directory /zfs/musc3/project/cellranger_out \
   --fastqs /zfs/musc3/project/fastqs \
   --transcriptome /zfs/musc3/reference/mm10 \
   --output_dir /zfs/musc3/project/scripts

example for cellranger multi:

generateCRscript -sample_name 7166-MR-1 \
   --job_id mouse_WT_cmo \
   --results_directory /zfs/musc3/project/cellranger_out \
   --csv /zfs/musc3/project/mouse_WT.csv \
   --output_dir /zfs/musc3/project/scripts
```

Note that instances of `/zfs/musc3` will be automatically replaced by `/mnt` for binding within the container. You may need to adjust other options (PBS job header, for instance) of the generated .pbs file.

### What's new

5/17/23 - Version 1.0.2
- Space Ranger version 2.0.1 added for spatial analysis

2/23/23 - Version 1.0.0
Cell Ranger versions:
- Cell Ranger: 7.1.0
- Cell Ranger ARC: 2.0.2
- Cell Ranger ATAC: 2.1.0

