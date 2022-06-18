typedef struct {
    struct WordFilter *ch[27];
    int idx;
} WordFilter;

WordFilter* wordFilterCreate(char ** words, int wordsSize) {
    WordFilter *dictionary = (WordFilter *)calloc( sizeof(WordFilter), 1 );
    
    for ( int i=0; i<wordsSize; i++ ) {
        int len = strlen(words[i]);
        char ch;
        
        for ( int j=0; j<=len; j++ ) {
            WordFilter *d_ptr = dictionary;

            char *suffix = &words[i][j];
            
            /* Add all variations of the suffix.  */
            while ( ch = *suffix++ ) {
                ch -= 'a';
                
                if ( d_ptr->ch[ch] == NULL ) {
                    d_ptr->ch[ch] = (WordFilter *)calloc( sizeof(WordFilter), 1 );
                }
                
                d_ptr->idx = ch; /* Replace with highest word index, not longest length!  */
                d_ptr = d_ptr->ch[ch];
            }
            
            /* Add the separator.  */
            if ( d_ptr->ch[26] == NULL ) {
                d_ptr->ch[26] = (WordFilter *)calloc( sizeof(WordFilter), 1 );
                d_ptr->idx = 26;
            }
            d_ptr = d_ptr->ch[26];
            
            /* Add the prefix (e.g. entire word).  */
            char *prefix = words[i];

            while ( ch = *prefix++ ) {
                ch -= 'a';

                if ( d_ptr->ch[ch] == NULL ) {
                    d_ptr->ch[ch] = (WordFilter *)calloc( sizeof(WordFilter), 1 );
                }
            
                d_ptr->idx = ch; /* Replace with highest word index, not longest length!  */
                d_ptr = d_ptr->ch[ch];
            }

            /* Mark the end of the word with a negative index, to help traversal.  */
            d_ptr->idx = -(i+1);
        }
    }
    
    return dictionary;
}

int wordFilterF(WordFilter* obj, char * prefix, char * suffix) {
    char ch;

    while ( ch = *suffix++ ) {
        ch -= 'a';
        if ( obj->ch[ch] == NULL )
            return -1; /* Suffix not found.  */

        obj = obj->ch[ch];
    }
    
    if ( obj->ch[26] == NULL )
        return -1; /* Separator not found.  */
    
    obj = obj->ch[26];

    while ( ch = *prefix++ ) {
        ch -= 'a';
        
        if ( obj->ch[ch] == NULL )
            return -1; /* Prefix not found.  */

        obj = obj->ch[ch];
    }
    
    /* Traverse until the index is no longer negative, which marks
     * the end of the word.
     */
    while ( obj->idx >= 0 ) {
        obj = obj->ch[obj->idx];
    }
    
    /* Return the index, which we made negative to mark the end of
     * the word.  The offset '1' is so the 0 index can't be made
     * negative.
     */
    return -obj->idx - 1;
}

void wordFilterFree(WordFilter* obj) {
    for ( int i=0; i<27; i++ ) {
        free(obj->ch[i]);
    }
    
    free(obj);
}