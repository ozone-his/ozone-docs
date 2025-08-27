Ozone includes backup and restore out of the box. The backup and restore engine is powered by the powerful and popular [Restic](https://restic.readthedocs.io/en/stable/) project. Meaning all the storage types supported by Restic can eventually be supported by Ozone.

We wrap Restic in a convience project to allow it to seamlessly intergrate with Ozone and if you are curious about the details you can take a look at the wrapper [project](https://github.com/mekomsolutions/restic-compose-backup)

Backups stored by Restic are encrypted.

The backup and restore process is broken into two different services:

- Backup service, which will run perdiocally.
- Restore service, which will be run once, to restore from a backup.

## Backing up

While the backup services are enabled by default when starting Ozone using the Start & Stop instructions, you may want to configure how and where the backups are stored, as well as at which frequency they're made.

As of now, you have 2 options to configure the Restic repository:

- Backup to a local path
- Backup to S3

Configuration of the backup services is done through environment variables.
There are multiple ways to set environment variables in Ozone. One of them could be to export the variable before running the start scripts, and this is the method used as an example in this page.

Once you speficy where and when to backup, you can run Ozone.

Example using the standard Start & Stop instructions:

```
./start.sh
```

A container suffixed as `-backup` will be created and always running.

But be sure to configure the backup service first, as detailed in the section below.

### Configure the backup frequency

To specify the frequency of the backup, you can set the `CRON_SCHEDULE` variable.

For example, to backup daily at 3am, you can run:
```
export CRON_SCHEDULE="0 3 * * *"
```

### Backup to local path

This is the default storage. With this option, all Restic backup files will be stored on disk. The default location of the archives is set to `./restic_data`. You can override it to any path on your filesystem where it is safe to store your backups (eg, a mounted NFS folder).

To do so, set the `BACKUP_PATH` environment variable to point to the path of choice.

```
export BACKUP_PATH=/mnt/nfs/backups/
```

### Backup to S3
Alternatively, you can store your backups on an S3 bucket.
!!! tip "Setting up an AWS S3 bucket"

    For help to properly set up an S3 bucket in AWS for Restic, you can follow the [Restic documentation](https://restic.readthedocs.io/en/latest/080_examples.html).

Once you have your bucket set up, you can configure a set of environemnt variables which, when set, will disable the default and enable storing the backups on S3.

```
export AWS_ACCESS_KEY_ID='key' 
export AWS_SECRET_ACCESS_KEY='secret' 
export RESTIC_REPOSITORY='s3:s3.amazonaws.com/ozone-backup'
export AWS_DEFAULT_REGION='eu-west-1'
```

## Viewing backups

You can list the backups by using the Restic `snapshots` command.
You can either run `restic snapshots` directly from an existing Restic container, or you can run an ephemeral container just for it:

Example for a local path Restic repository (assuming you have set the `BACKUP_PATH` value)
`docker run --rm --volume $BACKUP_PATH:/restic_data -env-file .env restic/restic:0.18.0 snapshots -r /restic_data`

Example if using S3 storage. Make sure to export the S3 specific variables. The command will then be:
`docker run --rm -env-file .env restic/restic:0.18.0 snapshots -r /restic_data`

The output will look like this:

```
ID        Time                 Host          Tags        Paths    Size
----------------------------------------------------------------------------
848a1772  2025-08-08 17:00:13  b89710290fa0              /backup  72.046 MiB
d46a0a4c  2025-08-08 17:15:08  10a1aa2e1817              /backup  70.820 MiB
----------------------------------------------------------------------------
2 snapshots
```

Unless you speficy otherwise, the most recent snapshot will be used for restore.
To override this, set the `RESTIC_RESTORE_SNAPSHOT` variable to the snapshot ID of choice.


## Restoring

Depending on how you have configured the backups, you need to restore the data accordingly. As a reminder, the 2 options available are:

- Restoring from a local path
- Restoring from S3

As opposed to the backup services, the restore services will run only once. Once done, the restore service will exit and Ozone will resume its startup.

Restore is triggered by setting `RESTORE` to `true`:
```
export RESTORE="true"
```

!!! danger "Potential Data Loss!"

    Please avoid hardcoding `RESTORE="true"` in any environment file so that it doesn't persist. This is to avoid re-restoring upon next restart, which could lead to losing data.

Then you need to set a particular value to the `COMPOSE_PROFILES` to inform which app you will restore data from.
The available values are:

- `openmrs-restore`
- `odoo-restore`
- `senaite-restore`

For example:
```
export COMPOSE_PROFILES='openmrs-restore,odoo-restore'
```

And run Ozone to proceed with the restore.

Eg, using the standard Start & Stop instructions:

```
./start.sh
```

!!! danger "Potential Data Loss!"

    Once the restore is done, run `unset RESTORE`.
    This is to avoid re-restoring upon next restart, which could lead to losing data.



But before actually restoring, let's dive and see how to set the variables to tell where to retrieve the backup.

### Restoring from a local path

This option is suitable when your Restic backups have been configured to be stored at a local path.
The restore options are configured using environment variables, as usual.

For example, to restore data that has been backed up at `/mnt/nfs/backups`:
```
export BACKUP_PATH=/mnt/nfs/backups/
```

### Restoring from S3

If your backups have been configured to be stored on S3, you must set those environment variables.

```
export AWS_ACCESS_KEY_ID='key' 
export AWS_SECRET_ACCESS_KEY='secret' 
export RESTIC_REPOSITORY='s3:s3.amazonaws.com/ozone-backup'
export AWS_DEFAULT_REGION='eu-west-1'
```

And run the commands as specified earlier.

## Disable backups

When using the default Start & Stop instrucutions, the backup services are enabled by default.

However, if you want to disable them, you simply should not include the `docker-compose-backup.yml` file to your start command. In that way it is similar to any other service in Ozone.

See this link to know how to specify the list of files to run: [Enable & Disable Apps and Integrations](../enabling-apps)

## Advanced configuration

Restic provides a rich set of features and backup storage backends, but Ozone supports only a small subset of the features and local path and S3 as the backup storage backends.
Among the supported features, you can set the password to protect the archives or configure data retention duration.

__Supported Configuration__

| Env Variable | Details | Example
|--|--|--|
| BACKUP_PATH | The external directory for storing Restic backups when storing on local disk | |
|CRON_SCHEDULE| Unix Cron pattern for when the backup with happen | `*/5 * * * *`|
|AWS_DEFAULT_REGION| This is used to set the bucket region when `RESTIC_REPOSITORY`  is S3| |
|AWS_ACCESS_KEY_ID| This is used to set the AWS access key id when `RESTIC_REPOSITORY`  is S3 | |
|AWS_SECRET_ACCESS_KEY| This is used to set the AWS secret when `RESTIC_REPOSITORY`  is S3 | |
|RESTORE| This variable is only needed when you want to test the restore using the `start.sh`  helper script. It has to be set to true| `export RESTORE="true"`|
| COMPOSE_PROFILES | Along side env above, you have to enable the restore Docker compose profiles for the services you wish to restore when running with the `start.sh` | `export COMPOSE_PROFILES=openmrs-restore,odoo-restore`|
|RESTIC_KEEP_WEEKLY|How many weeks back we should keep at least one snapshot  | |
|RESTIC_KEEP_MONTHLY|How many months back we should keep at least one snapshot  | |
|RESTIC_KEEP_YEARLY| How many years back we should keep at least one snapshot | |
|RESTIC_PASSWORD| The password used to unlock the repository | `password` |
|RESTIC_RESTORE_SNAPSHOT| The snapshot to be restored | `latest` |
|LOG_LEVEL| The log level for the Docker Compose Wrapper | `info` |
|RESTIC_REPOSITORY| Location of repository. A repository in Restic is refers to where the backups will be stored |  `/restic-backups` , `s3:s3.amazonaws.com/ozone-backup`

