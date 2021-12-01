import csv

# globals
# strings for the columns names in the csv file and for the file name
style = 'style'
year_formed = 'formed'
year_split = 'split'
band_name = 'band_name'
origin_country = 'origin'
file_end_date = 2017
metal_file_name = 'metal_bands_2017_MP2.csv'

def read_data(file_name):
    with open(file_name, 'r', encoding="utf-8-sig") as csvfile:
        x= [{k: v for k,v in row.items()}
           for row in csv.DictReader(csvfile)]
       
        
    return x
                          

def get_bands_formed_in_year(year):
   
    band_data = read_data(metal_file_name)

    band_list=[]
    for i in band_data:
        if year== str(i[year_formed]):
            thistuple=(i[band_name], i[origin_country])
            band_list.append(thistuple)
    return band_list


def get_bands_with_style(style_keyword):
  
    band_data = read_data(metal_file_name)
    
    band_stylelist=[]
    for i in band_data:
        if style_keyword.lower() in i[style].lower():
            if "," in i[style]:
                i[style]=i[style].replace(","," ")
            thistuple= (i[band_name], i[style])
            band_stylelist.append(thistuple)
    return band_stylelist


def get_bands_per_country():
    # get the data using your read_data() function
    band_data = read_data(metal_file_name)
    
    band_countrylist=[]
    band_countrydict={}
    for i in band_data:
        if i[origin_country] in band_countrydict.keys():
            band_countrydict[i[origin_country]]+=1
        elif i[origin_country]==False:
            band_countrydict["Unaffiliated"]= 1
        else:
            band_countrydict[i[origin_country]]=1
    
    band_country=band_countrydict.items()
    band_countrylist=list(band_country)

    def secondElem(tuple):
        return tuple[1]
    
    band_countrylist.sort(key=secondElem, reverse=True)
                             
    return band_countrylist

def get_longest_lived_bands(num_bands):
    # return the data from the file with read_data()
    band_data = read_data(metal_file_name)

    longest_lived_bands=[]
    for i in band_data:
        if i[year_formed]=="-":
            continue
        if i[year_split]=="-":
            thistuple=(i[band_name], (int(2021)-int(i[year_formed])))
            longest_lived_bands.append(thistuple)
        elif i[year_formed]==i[year_split]:
            thistuple=(i[band_name], 1)
            longest_lived_bands.append(thistuple)
        else:
            thistuple=(i[band_name], (int(i[year_split])-int(i[year_formed])))
            longest_lived_bands.append(thistuple)

    def secondElem(tuple):
        return tuple[1]
        
    longest_lived_bands.sort(key=secondElem, reverse=True)

    w=longest_lived_bands[:num_bands]
    return w

def print_table(nested_list, col_1_name, col_2_name):
  
    print("{:<40}{:<50}".format(col_1_name, col_2_name))
    for i in range(len(nested_list)):
        num1=nested_list[i][0]
        num2=nested_list[i][1]
        print("{:<40}{:<50}".format(num1, num2))

    
