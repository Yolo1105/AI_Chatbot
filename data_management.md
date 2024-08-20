- [Introduction to HPC Data Management](#introduction-to-hpc-data management)
- [Data Security Warning](#data-security-warning)
  - [Moderate Risk Data - HPC Approved](#moderate-risk-data---hpc-approved)
  - [High Risk Data - Secure Research Data Environments (SRDE) Approved](#high-risk-data---secure-research-data-environments-srde-approved)
- [Data Storage options in the HPC Environment](#data-storage-options-in-the-hpc-environment)
  - [User Home Directories](#user-home-directories)
  - [HPC Scratch](#hpc-scratch)
  - [HPC Vast](#hpc-vast)
  - [HPC Research Project Space](#hpc-research-project-space)
  - [HPC Work](#hpc-work)
  - [HPC Archive](#hpc-archive)
  - [NYU (Google) Drive](#nyu-google-drive)
  - [HPC Storage Mounts Comparison Table](#hpc-storage-mounts-comparison-table)

## Data Management Subpages
- [Data Transfers](#data-transfers)
- [Sharing Data on HPC](#sharing-data-on-hpc)
- [Research Project Space](#research-project-space)
- [Squash File System and Singularity](#squash-file-system-and-singularity)

# Introduction to HPC Data Management

The NYU HPC Environment provides access to a number of file systems to better serve the needs of researchers managing data during the various stages of the research data lifecycle (data capture, analysis, archiving, etc.). Each HPC file system comes with different features, policies, and availability.

In addition, a number of data management tools are available that enable data transfers and data sharing, recommended best practices, and various scenarios and use cases of managing data in the HPC Environment.

Multiple public data sets are available to all users of the HPC environment, such as a subset of The Cancer Genome Atlas (TCGA), the Million Song Database, ImageNet, and Reference Genomes.

Below is a list of file systems with their characteristics and a summary table. Reviewing the list of available file systems and the various Scenarios/Use cases that are presented below, can help select the right file systems for a research project. As always, if you have any questions about data storage in the HPC environment, you can request a consultation with the HPC team by sending an email to [hpc@nyu.edu](mailto:hpc@nyu.edu).

## Data Security Warning

### Moderate Risk Data - HPC Approved

- The HPC Environment has been approved for storing and analyzing Moderate Risk research data, as defined in the [NYU Electronic Data and System Risk Classification Policy](https://www.nyu.edu/about/policies-guidelines-compliance/policies-and-guidelines/electronic-data-and-system-risk-classification.html).
- High Risk research data, such as those that include Personal Identifiable Information (PII) or electronic Protected Health Information (ePHI) or Controlled Unclassified Information (CUI) should **NOT** be stored in the HPC Environment.
- Please note that only the Office of Sponsored Projects (OSP) and Global Office of Information Security (GOIS) are empowered to classify the risk categories of data.

### High Risk Data - Secure Research Data Environments (SRDE) Approved

Because the HPC system is not approved for High Risk data, we recommend using an approved system like the [Secure Research Data Environments (SRDE)](https://www.nyu.edu/nyu-hpc/training-support/supported-research-initiatives/secure-research-data-environment-srde).

## Data Storage options in the HPC Environment

### User Home Directories

Every individual user has a home directory (under `/home/$USER`, environment variable `$HOME`) for permanently storing code and important configuration files. Home Directories provide limited storage space (50 GB) and inodes (files) 30,000 per user. Users can check their quota utilization using the `myquota` command.

- User home directories are backed up daily and old files under `$HOME` are not purged.
- The User home directories are available on all HPC clusters (Greene) and on every cluster node (login nodes, compute nodes) as well as on the Data Transfer Node (gDTN).

**Please Note:**

- Avoid changing file and directory permissions in your home directory to allow other users to access files. User Home Directories are not ideal for sharing files and folders with other users. HPC Scratch or Research Project Space (RPS) are better file systems for sharing data.
- One of the common issues that users report regarding their home directories is running out of inodes, i.e., the number of files stored under their home exceeds the inode limit, which by default is set to 30,000 files. This typically occurs when users install software under their home directories, for example, when working with Conda and Julia environments, which involve many small files.
- To find out the current space and inode quota utilization and the distribution of files under your home directory, please see: [Understanding user quota limits and the `myquota` command](https://sites.google.com/nyu.edu/nyu-hpc/hpc-systems/hpc-storage/best-practices#h.82rgw7ex9n3i).
- **Working with Conda environments:** To avoid running out of inode limits in home directories, the HPC team recommends setting up Conda environments with Singularity overlay images.

### HPC Scratch

The HPC scratch file system is the HPC file system where most users store research data needed during the analysis phase of their research projects. The scratch file system provides temporary storage for datasets needed for running jobs.

- Files stored in the HPC scratch file system are subject to the **HPC Scratch old file purging policy**: Files on the `/scratch` file system that have not been accessed for 60 or more days will be purged.
- Every user has a dedicated scratch directory (`/scratch/$USER`) with 5 TB disk quota and 1,000,000 inodes (files) limit per user.
- The scratch file system is available on all nodes (compute, login, etc.) on Greene as well as the Data Transfer Node (gDTN).

**Please Note:**

- There are **No Backups** of the scratch file system. Files that were deleted accidentally or removed due to storage system failures **CANNOT** be recovered.
- Since there are no backups of the HPC Scratch file system, users should not put important source code, scripts, libraries, executables in `/scratch`. These important files should be stored in file systems that are backed up, such as `/home` or Research Project Space (RPS). Code can also be stored in a git repository.
- **Old file purging policy on HPC Scratch:** All files on the HPC Scratch file system that have not been accessed for more than 60 days will be removed. It is a policy violation to use scripts to change the file access time. Any user found to be violating this policy will have their HPC account locked. A second violation may result in your HPC account being turned off.
- To find out the user's current disk space and inode quota utilization and the distribution of files under your scratch directory, please see: [Understanding user quota limits and the `myquota` command](https://sites.google.com/nyu.edu/nyu-hpc/hpc-systems/hpc-storage/best-practices#h.82rgw7ex9n3i).
- Once a research project is completed, users should archive their important files in the HPC Archive file system.

### HPC Vast

The HPC Vast all-flash file system is the HPC file system where users store research data needed during the analysis phase of their research projects, particularly for high I/O data that can bottleneck on the scratch file system. The vast file system provides temporary storage for datasets needed for running jobs.

- Files stored in the HPC vast file system are subject to the **HPC Vast old file purging policy**: Files on the `/vast` file system that have not been accessed for 60 or more days will be purged.
- Every user has a dedicated vast directory (`/vast/$USER`) with 2 TB disk quota and 5,000,000 inodes (files) limit per user.
- The vast file system is available on all nodes (compute, login, etc.) on Greene as well as the Data Transfer Node (gDTN).

**Please Note:**

- There are **No Backups** of the vast file system. Files that were deleted accidentally or removed due to storage system failures **CANNOT** be recovered.
- Since there are no backups of the HPC Vast file system, users should not put important source code, scripts, libraries, executables in `/vast`. These important files should be stored in file systems that are backed up, such as `/home` or Research Project Space (RPS). Code can also be stored in a git repository.
- **Old file purging policy on HPC Vast:** All files on the HPC Vast file system that have not been accessed for more than 60 days will be removed. It is a policy violation to use scripts to change the file access time. Any user found to be violating this policy will have their HPC account locked. A second violation may result in your HPC account being turned off.
- To find out the user's current disk space and inode quota utilization and the distribution of files under your vast directory, please see: [Understanding user quota limits and the `myquota` command](https://sites.google.com/nyu.edu/nyu-hpc/hpc-systems/hpc-storage/best-practices#h.82rgw7ex9n3i).
- Once a research project is completed, users should archive their important files in the HPC Archive file system.

### HPC Research Project Space

The HPC Research Project Space (RPS) provides data storage space for research projects that is easily shared amongst collaborators, backed up, and not subject to the old file purging policy. HPC RPS was introduced to ease data management in the HPC environment and eliminate the need of having to frequently copy files between Scratch and Archive file systems by having all project files under one area. These benefits of the HPC RPS come at a cost. The cost is determined by the allocated disk space and the number of files (inodes).

For detailed information about RPS, see: [HPC Research Project Space](https://nyu.edu/nyu-hpc/hpc-systems/hpc-storage/data-management/research-project-space-rps).

### HPC Work

The HPC team makes available a number of public sets that are commonly used in analysis jobs. The data sets are available Read-Only under `/scratch/work/public`.

For some of the datasets, users must provide a signed usage agreement before accessing.

Public datasets available on the HPC clusters can be viewed on the [Datasets page](https://nyu.edu/nyu-hpc/hpc-systems/hpc-storage/datasets).

### HPC Archive

Once the Analysis stage of the research data lifecycle has completed, HPC users should tar their data and code into a single tar.gz file and then copy the file to their archive directory (`/archive/$USER`). The HPC Archive file system is not accessible by running jobs; it is suitable for long-term data storage. Each user has access to a default disk quota of 2TB and 20,000 inode (files) limit. The rather low limit on the number of inodes per user is intentional. The archive file system is available only on login nodes of Greene. The archive file system is backed up daily.

Here is an example tar command that combines the data in a directory named `my_run_dir` under `$SCRATCH` and outputs the tar file in the user's `$ARCHIVE`:

```bash
# to archive $SCRATCH/my_run_dir
tar cvf $ARCHIVE/simulation_01.tar -C $SCRATCH my_run_dir

# Data Management Subpages

## Data Transfers
[Link to Data Transfers Page](#)

## Sharing Data on HPC
[Link to Sharing Data on HPC Page](#)

## Research Project Space
[Link to Research Project Space Page](#)

## Squash File System and Singularity
[Link to Squash File System and Singularity Page](#)
