import json
from mdutils.mdutils import MdUtils

template_path = "../data/template.md"
data_path = "../data/data.json"
table_header = ["Slot", "Item", "Source"]

def parse_data(in_path, out_path):
   
    # Preprocessing

    ## creatimg output markdown file
    output = MdUtils(file_name='../rising_gods_bis',title='Rising-Gods BiS List (WIP)')

    ## opening source file
    f = open(in_path, 'r')

    ## extract JSON dict
    data = json.load(f)

    # Fill in tables

    ## loop over all classes
    for class_key,class_value in data.items():

        ### write class name as level 1 header in title case
        output.new_header (level=1, title=class_key.title())

        ### loop over all speccs
        for specc_key, specc_value in class_value.items():

            ### write specc name as level 2 header in title case
            output.new_header (level=2, title=specc_key.title())

            ### create specc table

            #### use standard table header
            table_list = table_header.copy()

            #### loop over all items
            for item_key, item_value in specc_value.items():

                #### set source for T10 items to "Vendor"
                source = "Vendor" if "T10" in item_value else ""
                #### catch alternatives
                if type(item_value) == list:
                    
                    #### add first item (default)
                    table_list.extend([item_key.title(), item_value[0], source])

                    #### loop over alternatives
                    for alt in item_value[1:]:

                        #### add alternative marking it as such
                        table_list.extend([item_key.title() + " (Alt)", alt, ""])
                else:

                    #### apped item to table source
                    table_list.extend([item_key.title(), item_value, source])

            #### compose table
            print(table_list)
            print(int(len(table_list)/3))            
            output.new_table(columns=3, rows=int(len(table_list)/3), text=table_list, text_align='left')

    output.create_md_file()
    print(output)

if __name__ == "__main__":
    parse_data(data_path, "")




