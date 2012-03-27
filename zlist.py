'''
Parse a CSS file for elements with a defined z-index and list them

Usage: $ python zlist.py <file.css> <file2.css> ..
'''

import cssutils
import logging
import sys
cssutils.log.setLevel(logging.CRITICAL)

def main():
    for filename in sys.argv[1:]:
        sheet = cssutils.parseFile(filename)
        zlist = []
        for rule in sheet:
            if rule.type == rule.STYLE_RULE:
                z = None
                for prop in rule.style:
                    if prop.name == 'z-index':
                        z = prop.value
                if z:
                    zlist.append([z, rule.selectorList])
        if zlist:
            print "%s: %d z-index declaration(s) found\n" % (filename, len(zlist))
            print "index  |".rjust(13), " selector\n", "".rjust(30, '-')
            zlist.sort(key=lambda entry: int(entry[0]))
            for entry in zlist:
                print entry[0].rjust(10), "".rjust(3),
                for selector in entry[1]:
                    if selector != entry[1][0]:
                        print "".rjust(14),
                    print selector.selectorText
            print ""
        else:
            print "%s: No z-index declarations found" % filename
        

if __name__ == "__main__":
    main()
