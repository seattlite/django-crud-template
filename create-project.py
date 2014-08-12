import os
import io
import sys
import shutil

application_name = sys.argv[1]
def clean_project(destination_directory, destination_template_directory):
    try:
        print ('deleting ', destination_directory)
        shutil.rmtree(destination_directory)
    except:
        pass
    try:
        print ('deleting ', destination_template_directory)
        shutil.rmtree(destination_template_directory)
    except:
        pass

destination_directory = str.format(r'{0}\{1}', os.getcwd(), application_name)
destination_template_directory = str.format(r'{0}\templates\{1}', os.getcwd(), application_name)
clean_project(destination_directory, destination_template_directory)

if sys.argv[2] == 'clean':
    exit()

source_directory = str.format(r'{0}\projectname', os.getcwd())
source_template_directory = str.format(r'{0}\templates\projectname', os.getcwd())
shutil.copytree(source_directory, destination_directory)
shutil.copytree(source_template_directory, destination_template_directory)

for d in [destination_template_directory, destination_directory]:
    files =  os.listdir(d)
    for f in files:
        src_file_name = str.format(r'{0}\{1}', d, f)
        if 'cache' in src_file_name:
            shutil.rmtree(src_file_name)
            continue
        print (src_file_name)
        tmp_file_name = str.format(r'{0}\{1}.back', d, f)
        src_file_io = io.open(src_file_name, 'r')
        tmp_file_io = io.open(tmp_file_name, 'w')
        tmp_data = []
        for l in src_file_io.readlines():
            d1 = l.replace('projectname', application_name)
            d2 = d1.replace('Projectname', application_name.capitalize())
            tmp_data.append(d2)
        tmp_file_io.writelines(tmp_data)
        tmp_file_io.close()
        src_file_io.close()
        os.remove(src_file_name)
        dst_file_name = src_file_name.replace('projectname', application_name)
        os.rename(tmp_file_name, dst_file_name)
