# S3 Backup Upload Script

A simple Python automation script that uploads a local file to an AWS S3 bucket as a backup.

The script:
- Reads a file in binary format
- Generates a unique backup name using UUID
- Uploads the file to a specified S3 bucket
- Stores it with a `.tar.gz` style backup naming format

---

## 🔮 Future Updates

- Add CLI arguments (`--file`, `--bucket`)  
- Add automatic bucket creation if it does not exist  
- Add error handling and logging  
- Add versioning and lifecycle policy support  
- Integrate with GitHub Actions for automated backups  
