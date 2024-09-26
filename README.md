<p align="center">
  <img src="https://gcloud.devoteam.com/wp-content/uploads/sites/32/2021/09/GOOGLE-CLOUD.png" width="60%" alt="DE-DATA-INGESTION-logo">
</p>
<p align="center">
    <h1 align="center">DE-DATA-INGESTION</h1>
</p>
<p align="center">
    <em><code> This repository contains a Open Source Metadata Driver data ingestion pipeline designed to automate the process of extracting, loading data from multiple sources into a data lake.</code></em>
</p>

<p align="center">
		<em>Built with the tools and technologies:</em>
</p>
<p align="center">
  <img src="https://img.shields.io/badge/PySpark-175ea8?style=for-the-badge&logo=apache&logoColor=white" alt="PySpark">
    <img src="https://img.shields.io/badge/Apache_Hadoop-a77c47?style=for-the-badge&logo=apachehadoop&logoColor=black" alt="Hadoop">
    <img src="https://img.shields.io/badge/SQL-00758F?style=for-the-badge&logo=oracle&logoColor=white" alt="SQL">
    <img src="https://img.shields.io/badge/PostgreSQL-5843c2?style=for-the-badge&logo=postgresql&logoColor=white" alt="PostgreSQL">
    <img src="https://img.shields.io/badge/Google_Cloud-4285F4?style=for-the-badge&logo=googlecloud&logoColor=white" alt="Google Cloud"></p>

<br>

##### 🔗 Table of Contents

- [📍 Overview](#-overview)
- [👾 Features](#-features)
- [📂 Repository Structure](#-repository-structure)
- [🧩 Modules](#-modules)
- [🚀 Getting Started](#-getting-started)
    - [🔖 Prerequisites](#-prerequisites)
    - [📦 Installation](#-installation)
    - [🤖 Usage](#-usage)
    - [🧪 Tests](#-tests)
- [📌 Project Roadmap](#-project-roadmap)
- [🤝 Contributing](#-contributing)


---

## 📍 Overview

 The project is about creating a Completely Metadata driven Data Ingestion Framework built using Pyspark with Google Cloud Platform as its primary cloud service. The framework reads the source data from multiple sources like Databases (Oracle, PostgreSQL, MySQL) and also files directly from GCS buckets and also from SFTP servers.

---

## 📂 Repository Structure

```sh
└── de-data-ingestion/
    ├── ingestion.zip
    ├── ingestion
    │   ├── env
    │   │   ├── __init__.py
    │   │   └── config.py
    │   ├── processing
    │   │   ├── encryptPII.py
    │   │   ├── formFileName.py
    │   │   ├── readSourceData.py
    │   │   └── saveToTarget.py
    │   ├── source
    │   │   ├── createSparkSession.py
    │   │   ├── getSaltValue.py
    │   │   └── readIngestionMetadata.py
    │   └── utils
    │       ├── connect_DB.py
    │       ├── getLogger.py
    │       ├── loadArguments.py
    │       └── uploadToAudit.py
    └── main.py
    
```

---
## 🧩 Modules

<details closed><summary>main</summary>

| File | Summary                                              |
| --- |------------------------------------------------------|
| [main.py](https://github.com/DannyBoy3310/de-data-ingestion/blob/main/main.py) | <code>❯ The Driver file for the PySpark Code </code> |

</details>

<details closed><summary>ingestion.env</summary>

| File | Summary                                                  |
| --- |----------------------------------------------------------|
| [config.py](https://github.com/DannyBoy3310/de-data-ingestion/blob/main/ingestion/env/config.py) | <code>❯ Default Values are set in the Config file</code> |

</details>

<details closed><summary>ingestion.processing</summary>

| File | Summary                                                                                                               |
| --- |-----------------------------------------------------------------------------------------------------------------------|
| [formFileName.py](https://github.com/DannyBoy3310/de-data-ingestion/blob/main/ingestion/processing/formFileName.py) | <code>❯ Regex Based File naming formation based on Execution Date</code>                                              |
| [encryptPII.py](https://github.com/DannyBoy3310/de-data-ingestion/blob/main/ingestion/processing/encryptPII.py) | <code>❯ Encrypt the PII data and load the Clear and Hash Value along with the Creation Date to the Audit Table</code> |
| [readSourceData.py](https://github.com/DannyBoy3310/de-data-ingestion/blob/main/ingestion/processing/readSourceData.py) | <code>❯ Read Source data as Dataframe </code>                                                                         |
| [saveToTarget.py](https://github.com/DannyBoy3310/de-data-ingestion/blob/main/ingestion/processing/saveToTarget.py) | <code>❯ Loading the Extracted Data into Destination</code>                                                            |

</details>

<details closed><summary>ingestion.utils</summary>

| File | Summary                                                                                   |
| --- |-------------------------------------------------------------------------------------------|
| [uploadToAudit.py](https://github.com/DannyBoy3310/de-data-ingestion/blob/main/ingestion/utils/uploadToAudit.py) | <code>❯ Upload the PII data along with the Hashed Value to Audit Table </code>            |
| [connect_DB.py](https://github.com/DannyBoy3310/de-data-ingestion/blob/main/ingestion/utils/connect_DB.py) | <code>❯ Pre-check the connection before reading and writing to Source/Destination </code> |
| [getLogger.py](https://github.com/DannyBoy3310/de-data-ingestion/blob/main/ingestion/utils/getLogger.py) | <code>❯ LoggerClass File to monitor the events</code>                                     |
| [loadArguments.py](https://github.com/DannyBoy3310/de-data-ingestion/blob/main/ingestion/utils/loadArguments.py) | <code>❯ Argument Parser file to set the command line arguments passed </code>             |

</details>

<details closed><summary>ingestion.source</summary>

| File | Summary                                                                |
| --- |------------------------------------------------------------------------|
| [readIngestionMetadata.py](https://github.com/DannyBoy3310/de-data-ingestion/blob/main/ingestion/source/readIngestionMetadata.py) | <code>❯ Read the entity and table metadata </code>                     |
| [createSparkSession.py](https://github.com/DannyBoy3310/de-data-ingestion/blob/main/ingestion/source/createSparkSession.py) | <code>❯ Entry point of Spark.</code>                                   |
| [getSaltValue.py](https://github.com/DannyBoy3310/de-data-ingestion/blob/main/ingestion/source/getSaltValue.py) | <code>❯ Read the Salt Value stored in the Google Secret manager</code> |

</details>

---

## 🚀 Getting Started

### 🔖 Prerequisites

**Python**: `version 3.8.2`

### 📦 Installation

Build the project from source:

1. Clone the de-data-ingestion repository:
```sh
❯ git clone https://github.com/DannyBoy3310/de-data-ingestion
```

2. Navigate to the project directory:
```sh
❯ cd de-data-ingestion
```

3. Install the required dependencies:
```sh
❯ pip install -r requirements.txt
```

### 🤖 Usage

To run the project, execute the following command:

```sh
❯ spark-submit \
  --jars {list_of_external_jar_files} \
  --py-files {path_to_python_files_or_zip_archive} \
  main.py \
  --entity-name {entity_name} \
  --source-bucket {source_bucket_name} \
  --source-dir {source_directory_name} \
  --source-file-name {source_file_name} \
  --target-bucket {target_bucket_name} \
  --target-dir {target_directory_name} \
  --execution-date {execution_date} \
  --metadata-bucket {metadata_bucket_name} \
  --metadata-dir {metadata_directory_name} \
  --filename-ingestion-metadata {ingestion_metadata_filename} \
  --filename-entity-metadata {entity_metadata_filename} \
  --run-mode {run_mode_full_or_incremental} \
  --audit-username {audit_database_username} \
  --audit-password {audit_database_password} \
  --audit-port {audit_database_port} \
  --audit-schema {audit_database_schema} \
  --audit-dbname {audit_database_name} \
  --audit-host {audit_database_host} \
  --audit-tablename {audit_table_name}

```

Description:

1. --jars: Specifies external JAR files that will be included in the job. These are often used for adding connectors or database drivers.
2. --py-files: Specifies additional Python files or archives that need to be distributed across the worker nodes.
3. --entity-name: Indicates the name of the entity being processed in the data ingestion (e.g., CUSTOMER_STATUS).
4. --source-bucket: The Google Cloud Storage bucket or other cloud storage where the source data files are located.
5. --source-dir: The directory within the source bucket that contains the data files.
6. --source-file-name: The specific source file name being processed from the source directory.
7. --target-bucket: The destination bucket where the transformed data will be stored.
8. --target-dir: The directory within the target bucket where the processed data will be placed.
9. --execution-date: The date that corresponds to the specific execution run of the job.
10. --metadata-bucket: Specifies the bucket where metadata files (such as mapping and schema details) are stored.
11. --metadata-dir: The directory within the metadata bucket where the relevant metadata files are kept.
12. --filename-ingestion-metadata: The name of the file that contains metadata related to the ingestion process.
13. --filename-entity-metadata: The name of the file that contains metadata related to the entity being processed.
14. --run-mode: Specifies the mode in which the job is run, such as full (full data load) or incremental.
15. --audit-username: The username for connecting to the audit database, where logs or audits of the process are stored.
16. --audit-password: The password for connecting to the audit database.
17. --audit-port: The port number used for connecting to the PostgreSQL audit database.
18. --audit-schema: The schema within the audit database where the audit logs are stored.
19. --audit-dbname: The name of the audit database where audit-related tables reside.
20. --audit-host: The host (usually an IP address or hostname) of the audit database.
21. --audit-tablename: The name of the audit table where audit records will be stored.


---

## 📌 Project Roadmap

-  **`Task 1`**: Setup Pyspark and Google Cloud in your local.
-  **`Task 2`**: Start the Postgre Server to load Audit Data.
-  **`Task 3`**: Zip the ingestion folder as zip and trigger the spark-submit command.

---

## 🤝 Contributing

Contributions are welcome! Here are several ways you can contribute:

- **[Report Issues](https://github.com/DannyBoy3310/de-data-ingestion/issues)**: Submit bugs found or log feature requests for the `de-data-ingestion` project.
- **[Submit Pull Requests](https://github.com/DannyBoy3310/de-data-ingestion/blob/main/CONTRIBUTING.md)**: Review open PRs, and submit your own PRs.
- **[Join the Discussions](https://github.com/DannyBoy3310/de-data-ingestion/discussions)**: Share your insights, provide feedback, or ask questions.

<details closed>
<summary>Contributing Guidelines</summary>

1. **Fork the Repository**: Start by forking the project repository to your github account.
2. **Clone Locally**: Clone the forked repository to your local machine using a git client.
   ```sh
   git clone https://github.com/DannyBoy3310/de-data-ingestion
   ```
3. **Create a New Branch**: Always work on a new branch, giving it a descriptive name.
   ```sh
   git checkout -b new-feature-x
   ```
4. **Make Your Changes**: Develop and test your changes locally.
5. **Commit Your Changes**: Commit with a clear message describing your updates.
   ```sh
   git commit -m 'Implemented new feature x.'
   ```
6. **Push to github**: Push the changes to your forked repository.
   ```sh
   git push origin new-feature-x
   ```
7. **Submit a Pull Request**: Create a PR against the original project repository. Clearly describe the changes and their motivations.
8. **Review**: Once your PR is reviewed and approved, it will be merged into the main branch. Congratulations on your contribution!
</details>

<details closed>
<summary>Contributor Graph</summary>
<br>
<p align="left">
   <a href="https://github.com{/DannyBoy3310/de-data-ingestion/}graphs/contributors">
      <img src="https://contrib.rocks/image?repo=DannyBoy3310/de-data-ingestion">
   </a>
</p>
</details>

---



---
