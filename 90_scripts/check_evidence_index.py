#!/usr/bin/env python3
import pandas as pd
import sys
from pathlib import Path

def main():
    # Check if Evidence Index exists
    index_path = Path("VCAT_SUBMISSION_PACKAGE/02_EVIDENCE_INDEX/VCAT_Evidence_Index.csv")
    manifest_path = Path("VCAT_Evidence_Integrity_Manifest.csv")
    
    if not index_path.exists():
        print(f"ERROR: Evidence Index not found at {index_path}")
        sys.exit(1)
    
    if not manifest_path.exists():
        print(f"ERROR: Integrity manifest not found at {manifest_path}")
        sys.exit(1)
    
    try:
        index_df = pd.read_csv(index_path)
        manifest_df = pd.read_csv(manifest_path)
        
        # Basic validation
        required_columns = ["exhibit_code", "title", "file_path", "hash_sha256"]
        missing_cols = [col for col in required_columns if col not in index_df.columns]
        
        if missing_cols:
            print(f"ERROR: Missing required columns in Evidence Index: {missing_cols}")
            sys.exit(1)
        
        # Check file counts
        index_files = len(index_df)
        manifest_files = len(manifest_df)
        
        print(f"Evidence Index: {index_files} entries")
        print(f"Integrity Manifest: {manifest_files} files")
        
        # Basic consistency check
        if index_files > 0 and manifest_files > 0:
            print("✅ Evidence Index and Integrity Manifest both contain data")
        else:
            print("⚠️  Warning: One or both files appear empty")
        
        print("✅ Evidence Index validation completed")
        
    except Exception as e:
        print(f"ERROR: Failed to validate evidence index: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()