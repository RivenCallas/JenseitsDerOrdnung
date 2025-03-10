import zipfile
import argparse
import os

# Create a zip file from a folder
def concat_files(target_folder, output_filename):
    zipf = ""
    for root, dirs, files in os.walk(target_folder):        
        # write files to zip
        for file in files:
            if file.endswith('.txt') and not file.endswith('.concat.txt'):
                with open(os.path.join(root, file), 'r', encoding="utf-8") as f:
                    zipf += f.read()

        with open(output_filename, 'w', encoding="utf-8") as f:
            f.write(zipf)



if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Create a concat text file from a folder')
    parser.add_argument('--folder', help='Folder to zip')
    parser.add_argument('--output', help='Output filename of the concatenated files')
    args = parser.parse_args()

    concat_files(args.folder, args.output)
    print('done.')
