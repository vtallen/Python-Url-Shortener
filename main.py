from flask import Flask, redirect, request, render_template
import string

# app = Flask(__name__)

url_map = {
        "abc" : "https://startpage.com"
        }

# * *********************************************************************************** *
# *                                                                                     * 
# * Function Name: gen_shortcode                                                        *
# *                                                                                     * 
# * Description: Calculates a short link based on an ID in the database of links.       *
# *     The given ID is converted to a base 62 number, then mapped to a character in    *
# *     a string containing a-z, A-Z, and 0-9                                           *
# *                                                                                     *
# * Parameters:                                                                         *
# *     int id: the id in the database for which a shortcode should be generated for    *
# *                                                                                     *
# * Return value:                                                                       *
# *     str: the shortcode corasponding to the given id                                 * 
# * *********************************************************************************** *
def gen_shortcode(id):
    validchars = string.ascii_lowercase + string.ascii_uppercase + "0123456789"
    remainders = []
    
    base = 62 
    while id > 0:
        quotient = int(id / base)
        remainder = id % base
        
        remainders.append(remainder) 

        id = quotient

    remainders.reverse();
    
    shortcode = ''
    for num in remainders:
        shortcode += validchars[num]

    return shortcode 

# * *********************************************************************************** *
# *                                                                                     * 
# * Function Name: get_id                                                               *
# *                                                                                     * 
# * Description: Calculates a short link based on an ID in the database of links.       *
# *     The given ID is converted to a base 62 number, then mapped to a character in    *
# *     a string containing a-z, A-Z, and 0-9                                           *
# *                                                                                     *
# * Parameters:                                                                         *
# *     int id: the id in the database for which a shortcode should be generated for    *
# *                                                                                     *
# * Return value:                                                                       *
# *     str: the shortcode corasponding to the given id                                 * 
# * *********************************************************************************** *
def gen_id(shortcode):
    return 0





# @app.route("/<short_link>")
# def redirect_short_link(short_link):
#     if short_link in url_map:
#         return redirect(url_map[short_link])
#     else:
#         return "URL does not exist!", 404

print(gen_shortcode(12492819991010))
    
