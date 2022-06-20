import os
import re
import sys
import logging
import json
import pprint
#To add markdown,yaml parckage
#pip install --upgrade pip
#!{sys.executable} -m pip install markdown
#!{sys.executable} -m pip install pyyaml
#!{sys.executable} -m pip install python-frontmatter
import markdown
import yaml
import frontmatter

############################################################
#GET NUMBER OF MD FILE FOR EACH CATEGORIE
############################################################
print("**LANCEMENT DU PROGRAMME**")
dict_numbers_of_categories = {}
path='..\..\content'

for subdir, dirs, files in os.walk(path):
    for file in files:
        if "anti-patterns" in subdir or "patterns" in subdir:
            if re.findall(".md$", file):
                
                #print(os.path.join(subdir, file))
                md = frontmatter.load(os.path.join(subdir, file))
                
                if 'categories' not in md or md['categories'] == None or len(md['categories']) == 0:
                    if "NO CATEGORIES FOUND" not in dict_numbers_of_categories:
                        dict_numbers_of_categories['NO CATEGORIES FOUND'] = 1
                    else:
                        dict_numbers_of_categories['NO CATEGORIES FOUND'] = dict_numbers_of_categories['NO CATEGORIES FOUND'] + 1
                else:
                    for i in range(0, len(md['categories'])):
                        if md['categories'][i] not in dict_numbers_of_categories:
                            dict_numbers_of_categories[md['categories'][i]] = 1
                        else:
                            dict_numbers_of_categories[md['categories'][i]] = dict_numbers_of_categories[md['categories'][i]] + 1
                
print(dict_numbers_of_categories)



logging.basicConfig(filename='myapp.log', level=logging.DEBUG, 
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
                
                print(os.path.join(subdir, file))
                origin = subdir.split("\\")
                #print(origin[2])
                dict_data = {}
                
                try:
                    md = frontmatter.load(os.path.join(subdir, file))
                                            
                    #keep title from meta
                    if 'title' not in md or md['title'] == None or len(md['title']) == 0:
                        dict_data['title'] = "!!NO TITLE FOUND!!"
                    else:
                        #print(md['title'])
                        dict_data['title'] = md['title']
         
                    #keep description
                    if 'description' not in md or md['description'] == None or len(md['description']) == 0:
                        #print("!!NO DESCRIPTION FOUND!!")
                        dict_data['description'] = "!!NO DESCRIPTION FOUND!!"
                    else:
                        #print(md['description'])
                        dict_data['description'] = md['description']

                    #keep featured image
                    if 'featured_image' not in md or md['featured_image'] == None or len(md['featured_image']) == 0:
                        #print("!!NO FEATURED IMAGE FOUND!!")
                        dict_data['featured_image'] = "!!NO FEATURED IMAGE FOUND!!"
                    else:
                        #print(md['featured_image'])
                        dict_data['featured_image'] = md['featured_image']
                    
                    #keep categorie
                    if 'categories' not in md or md['categories'] == None or len(md['categories']) == 0:
                        #print("!!NO CATEGORIES FOUND!!")
                        if "NO CATEGORIES FOUND" not in dict_tmp_categorie:
                            dict_tmp_categorie['NO CATEGORIES FOUND'] = 1
                            dict_categorie["NO CATEGORIES FOUND"] = "[" + str(dict_data)
                        else:
                            dict_tmp_categorie['NO CATEGORIES FOUND'] = dict_tmp_categorie['NO CATEGORIES FOUND'] + 1
                            if dict_tmp_categorie['NO CATEGORIES FOUND'] == dict_numbers_of_categories['NO CATEGORIES FOUND']:
                                dict_categorie["NO CATEGORIES FOUND"] += "," + str(dict_data) + "]"
                            else:
                                dict_categorie["NO CATEGORIES FOUND"] += "," + str(dict_data)
                    else:
                        for i in range(0, len(md['categories'])):
                            #print(md['categories'][i]) 
                            if md['categories'][i] not in dict_categorie:
                                dict_tmp_categorie[md['categories'][i]] = 1
                                dict_categorie[md['categories'][i]] = "[" + str(dict_data)
                            else:
                                dict_tmp_categorie[md['categories'][i]] = dict_tmp_categorie[md['categories'][i]] + 1
                                if dict_tmp_categorie[md['categories'][i]] == dict_numbers_of_categories[md['categories'][i]]:
                                    dict_categorie[md['categories'][i]] += "," + str(dict_data) + "]"
                                else:
                                    dict_categorie[md['categories'][i]] += "," + str(dict_data)
                    
                    
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
with open("data.json", "w", encoding="utf8") as output_file:
    json.dump(final_dict, output_file) 
