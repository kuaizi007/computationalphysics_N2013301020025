     _=['       ','       ','       ','       ','       ']
     B=[' ****  ',' *   * ',' ****  ',' *   * ',' ****  ']
     O=['  ***  ',' *   * ',' *   * ',' *   * ','  ***  ']
     S=['  **** ',' *     ','  ***  ','     * ',' ****  ']    
     H=[' *   * ',' *   * ',' ***** ',' *   * ',' *   * '] 
     E=[' ***** ',' *     ', ' *****',' *     ',' ***** ']
     N=[' *   * ',' **  * ','  * * *',' *  ** ',' *   * ']
     repository = {' ':_,'b':B,'o':O,'s':S,'h':H,'e':E,'n':N}

     letters= raw_input('please type letters from "boshen" ').lower()
     l= len(letters)

     for y in range(5):    
         letters_pixel =_
         for x in range(l):
             letters_pixel[y]+=repository[letters[x]][y]
         print letters_pixel[y]
    
     while True: input()
