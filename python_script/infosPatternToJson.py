import os
import re
import sys
import logging
import json
import pprint
import markdown
import yaml
import frontmatter


############################################################
#GET NUMBER OF MD FILE FOR EACH CATEGORIE
############################################################
print("**LANCEMENT DU PROGRAMME**")
dict_numbers_of_categories = {}
path='./content'

for subdir, dirs, files in os.walk(path):
    for file in files:
        if "anti-patterns" in subdir or "patterns" in subdir:
            if re.findall(".md$", file):
                
                #print(os.path.join(subdir, file))
                md = frontmatter.load(os.path.join(subdir, file))
                
                if 'categories' not in md or md['categories'] == None or len(md['categories']) == 0:
                    if "DEFAULT" not in dict_numbers_of_categories:
                        dict_numbers_of_categories['DEFAULT'] = 1
                    else:
                        dict_numbers_of_categories['DEFAULT'] = dict_numbers_of_categories['DEFAULT'] + 1
                else:
                    for i in range(0, len(md['categories'])):
                        if md['categories'][i] not in dict_numbers_of_categories:
                            dict_numbers_of_categories[md['categories'][i]] = 1
                        else:
                            dict_numbers_of_categories[md['categories'][i]] = dict_numbers_of_categories[md['categories'][i]] + 1
                
print(dict_numbers_of_categories)



logging.basicConfig(filename='./python_script/myapp.log', level=logging.DEBUG, 
                    format='%(asctime)s %(levelname)s %(name)s %(message)s')
logger=logging.getLogger(__name__)
dict_tmp_categorie = {}
final_dict = {}
    
for subdir, dirs, files in os.walk(path):
    dict_temp = {}
    dict_categorie = {}
    for file in files:
        if "anti-patterns" in subdir or "patterns" in subdir:
            if re.findall(".md$", file):
                
                #print(os.path.join(subdir, file))
                origin = subdir.split("/")
                #print(origin[2])
                dict_data = {}
                
                try:
                    md = frontmatter.load(os.path.join(subdir, file))
                                            
                    #keep title from meta
                    if 'title' not in md or md['title'] == None or len(md['title']) == 0:
                        dict_data['title'] = "!!NO TITLE FOUND!!"
                    else:
                        #print(md['title'])
                        dict_data['title'] = md['title'].replace("'", "#")
         
                    #keep description
                    if 'description' not in md or md['description'] == None or len(md['description']) == 0:
                        #print("!!NO DESCRIPTION FOUND!!")
                        dict_data['description'] = "Description to come"
                    else:
                        #print(md['description'])
                        dict_data['description'] = md['description'].replace("'", "#")

                    #keep featured image
                    if 'interact_with' not in md or md['interact_with'] == None or len(md['interact_with']) == 0:
                        #print("!!NO FEATURED IMAGE FOUND!!")
                        dict_data['interact_with'] = "!!NO interact_with FOUND!!"
                    else:
                        #print(md['featured_image'])
                        dict_data['interact_with'] = md['interact_with']
                    
                    new_format_dict_data = re.sub("'","\"", str(dict_data))
                    new_format_dict_data_v2 = re.sub("#","'", new_format_dict_data)
                    
                    #keep categorie
                    if 'categories' not in md or md['categories'] == None or len(md['categories']) == 0:
                        #print("!!DEFAULT!!")
                        if "DEFAULT" not in dict_tmp_categorie:
                            dict_tmp_categorie['DEFAULT'] = 1
                            dict_categorie["DEFAULT"] = "[" + new_format_dict_data_v2
                        else:
                            dict_tmp_categorie['DEFAULT'] = dict_tmp_categorie['DEFAULT'] + 1
                            if dict_tmp_categorie['DEFAULT'] == dict_numbers_of_categories['DEFAULT']:
                                dict_categorie["DEFAULT"] += "," + new_format_dict_data_v2 + "]"
                            else:
                                dict_categorie["DEFAULT"] += "," + new_format_dict_data_v2
                    else:
                        for i in range(0, len(md['categories'])):
                            #print(md['categories'][i]) 
                            if md['categories'][i] not in dict_categorie:
                                dict_tmp_categorie[md['categories'][i]] = 1
                                dict_categorie[md['categories'][i]] = "[" + new_format_dict_data_v2
                            else:
                                dict_tmp_categorie[md['categories'][i]] = dict_tmp_categorie[md['categories'][i]] + 1
                                if dict_tmp_categorie[md['categories'][i]] == dict_numbers_of_categories[md['categories'][i]]:
                                    dict_categorie[md['categories'][i]] += "," + new_format_dict_data_v2 + "]"
                                else:
                                    dict_categorie[md['categories'][i]] += "," + new_format_dict_data_v2
                    
                    
                except Exception as e:
                    print(e)
                    logger.error(e)
                    print("\n")
       
    if len(dict_categorie) !=0:
        if  origin[2] not in final_dict:
            final_dict[origin[2]] = dict_categorie
        else:
            final_dict[origin[2]].update(dict_categorie)

pprint.pprint(final_dict)
with open("./python_script/data.json", "w", encoding="utf8") as output_file:
    json.dump(final_dict, output_file) 
