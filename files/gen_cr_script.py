#!/opt/cellranger-7.1.0/external/anaconda/bin/python
import os

def main(args):

    if not args.count and not args.multi:
        args.count = True

    if args.count and args.multi:
        raise RuntimeError("Please select ONE of either count (--count) or multi (--multi)")

    if args.output_dir:
        assert os.path.isdir(args.output_dir)

    #parse job ids - if there isn't one, use sample_name instead
    #even if multiple samples are given and no job id is, those samples will be assigned to the job ids
    if args.job_id:
        job_id = args.job_id
    else:
        job_id = args.sample_name

    all_samples = [s.strip() for s in args.sample_name.split(",")]
    all_job_ids = [j.strip() for j in job_id.split(",")]
    if set(all_job_ids) == 1:
        all_job_ids = [j+f"_0{i}" for i, j in enumerate(all_job_ids)]
    jobs_and_samples = zip(all_job_ids, all_samples)

    print("Creating files for:")
    for j,s in jobs_and_samples:
        print(f"JOB: {j} | SAMPLE: {s}")

    if args.count:

        for job, sample in zip(all_job_ids, all_samples):

            # create output basename and path
            outfile_basename = job + ".pbs"
            if args.output_dir:
                outfile_name = os.path.join(args.output_dir, outfile_basename)
            else:
                outfile_name = os.path.join(os.getcwd(), outfile_basename)

            #fastqs required
            if not args.fastqs:
                raise RuntimeError("Please provide directory to fastq files (-f or --fastqs)")

            #ref path required
            if not args.transcriptome:
                raise RuntimeError("Please provide path to 10X reference (-t or --transcriptome)")

            # convert filepaths if needed
            res_dir = args.results_directory if args.results_directory else "/mnt"
            res_dir = res_dir.replace("/zfs/musc3", "/mnt")
            fastq_dir = args.fastqs.replace("/zfs/musc3", "/mnt")
            ref_dir = args.transcriptome.replace("/zfs/musc3", "/mnt")

            with open(outfile_name, "w") as outfile:

                #PBS header
                outfile.write(f"#PBS -N {sample}_count\n")
                outfile.write("#PBS -l select=1:ncpus=24:mem=200gb,walltime=48:00:00\n")
                outfile.write("#PBS -m abe\n\n")

                outfile.write(f"singularity exec -B /zfs/musc3:/mnt --pwd {res_dir} /zfs/musc3/singularity_images/biocm-cellranger_latest.sif \\\n")
                outfile.write("\tcellranger count \\\n")
                outfile.write(f"\t--id={job} \\\n")
                outfile.write(f"\t--transcriptome={ref_dir} \\\n")
                outfile.write(f"\t--fastqs={fastq_dir} \\\n")
                outfile.write("\t--localmem=150")
            print(f"PBS script written and saved at {outfile_name}")

    if args.multi:
        for job, sample in zip(all_job_ids, all_samples):

            # create output basename and path
            outfile_basename = job + ".pbs"
            if args.output_dir:
                outfile_name = os.path.join(args.output_dir, outfile_basename)
            else:
                outfile_name = os.path.join(os.getcwd(), outfile_basename)

            # convert filepaths if needed
            res_dir = args.results_directory if args.results_directory else "/mnt"
            res_dir = res_dir.replace("/zfs/musc3", "/mnt")
            csv_dir = args.csv.replace("zfs/musc3", ".mnt")

            if not csv_dir.endswith(".csv"):
                csv_dir = csv_dir + ".csv"

            with open(outfile_name, "w") as outfile:
                #PBS header
                outfile.write(f"#PBS -N {sample}_multi\n")
                outfile.write("#PBS -l select=1:ncpus=24:mem=200gb,walltime=48:00:00\n")
                outfile.write("#PBS -m abe\n\n")

                outfile.write(f"singularity exec -B /zfs/musc3:/mnt --pwd {res_dir} /zfs/musc3/singularity_images/biocm-cellranger_latest.sif \\\n")
                outfile.write("\tcellranger multi \\\n")
                outfile.write(f"\t--id={job} \\\n")
                outfile.write(f"\t--csv={csv_dir} \\\n")

            print(f"PBS script written and saved at {outfile_name}")

if __name__ == "__main__":

    # setting the hyper parameters
    import argparse

    parser = argparse.ArgumentParser(description='Create Anndata file from prepared Seurat directory',
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-s', '--sample_name', default=None, required=True)
    parser.add_argument('-i', '--job_id', default=None, required=False)
    parser.add_argument("--count", action="store_true")
    parser.add_argument("--multi", action="store_true")
    parser.add_argument('-r', '--results_directory', default=None, required=False)
    parser.add_argument('-f', '--fastqs', default=None, required=False)
    parser.add_argument('-t', '--transcriptome', default=None, required=False)
    parser.add_argument('-c', '--csv', default=None, required=False)
    parser.add_argument('-o', '--output_dir', default=None)

    args = parser.parse_args()

    main(args)
