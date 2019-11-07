class Character:

    @staticmethod
    def get_lower_case_chars():
        """
        Returns a list of all lower case letters
        """
        return [q,w,e,r,t,y,u,i,o,p,a,s,d,f,g,h,j,k,l]

    @staticmethod
    def get_upper_case_chars():
        """
        Returns a list of all upper case letters
        """
        return [Q,W,E,R,T,Y,U,I,O,P,A,S,D,F,G,H,J,K,L,Z,X,C,V,B,N,M]

    @staticmethod
    def get_special_chars():
        """
        Returns a list of all special characters to consider for these exercises.
        space, shift, capslock, tab, enter.
        Ignore all other keys
        """
        return []