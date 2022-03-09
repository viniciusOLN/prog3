import csv

#function to split the list in little pieaces in a frequency(count of the columns in the tsv file)
def chunks(list, frequency):
    for i in range(0, len(list), frequency):
        yield list[i:i + frequency]

#function to read the file tsv and clean the data
def purify_data_in_tsv(file_name, frequency):    
    data = list()  
    nums = list()         
    file = file_name.read().decode('UTF8')
    for row in csv.reader(file, delimiter="\t"):
        if len(row) > 0:               
            if row[0] != '':                    
                nums.append(''.join(row))
            else:                 
                data.append(''.join(nums))
                nums = list()
        else:
            data.append(''.join(nums))
            nums = list()           
    data.append(''.join(nums))

    while '' in data:
            data.remove('')  
              
    return list(chunks(data, frequency))