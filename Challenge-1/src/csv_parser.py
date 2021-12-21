def csvParser(csv):
    file = open(csv,'r')
    lines = file.readlines()
    output = []
    for line in lines:
        output.append(line)
    return output

def Split_Csv(parsedCSV,*args,**kwargs):
    for csvLine in parsedCSV:
        print(csvLine)
        output.append(csvLine.split(','))
    return output

def combine_columns(csv, column1, column2, **kwargs):
    output = csv[0] # This is the headers
    for IDX in range(len(csv)):
        csv_line = csv[IDX][column1] + csv[IDX][column2]
        output.append(csv[IDX].append(csv_line))
    return output

if __name__ == '__main__':
    global output

    csv = csvParser('/Users/random/Downloads/test.csv')
    file = open('/Users/random/Downloads/test1.csv', 'a')
    file.write(str(csv)) # Write needs string not list
    csv = Split_Csv(csv)
    csv = combine_columns(csv, 0, 1)
    for line in csv:
        file2 = open('/Users/random/Downloads/test2.csv','a')
        file2.write(str(line)) # write needs string not list
        file2.close()
    file.close()