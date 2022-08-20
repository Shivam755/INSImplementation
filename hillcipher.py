import string

class Hill:
    @classmethod
    def generate_key(cls,n,s):
        s=s.replace(" ","")
        s=s.lower()
        main=string.digits
        
        key_matrix=['' for i in range(n)]
        i=0;j=0
        for c in s:
            if c in main:
                key_matrix[i]+=c
                j+=1
                if(j>n-1):
                    i+=1
                    j=0
        
        key_num_matrix=[]
        for i in key_matrix:
            sub_array=[]
            for j in range(n):
                sub_array.append(ord(i[j])-ord('a'))
            key_num_matrix.append(sub_array)
        return(key_num_matrix)
        
    @classmethod
    def message_matrix(cls,s,n):
        s=s.replace(" ","")
        s=s.lower()
        final_matrix=[]
        if(len(s)%n!=0):
            # z is the bogus word
            while(len(s)%n!=0):
                s=s+'z'
                
        for k in range(len(s)//n):
            message_matrix=[]
            for i in range(n):
                sub=[]
                for j in range(1):
                    sub.append(ord(s[i+(n*k)])-ord('a'))
                message_matrix.append(sub)
            final_matrix.append(message_matrix)
        return(final_matrix)

    @classmethod
    def getCofactor(cls,mat, temp, p, q, n): 
        i = 0
        j = 0

        for row in range(n):  
            for col in range(n): 
                
                if (row != p and col != q) : 
                    temp[i][j] = mat[row][col] 
                    j += 1
    
                    if (j == n - 1): 
                        j = 0
                        i += 1
    
    @classmethod
    def determinantOfMatrix(cls,mat, n): 
        D = 0 # Initialize result 
    
    
        if (n == 1): 
            return mat[0][0] 
            
        # To store cofactors 
        temp = [[0 for x in range(n)]  
                for y in range(n)]  
    
        sign = 1  
    

        for f in range(n): 
            
            # Getting Cofactor of mat[0][f] 
            cls.getCofactor(mat, temp, 0, f, n) 
            D += (sign * mat[0][f] *
                cls.determinantOfMatrix(temp, n - 1)) 
    
            # terms are to be added with alternate sign 
            sign = -sign 
        return D 
    
    @classmethod
    def isInvertible(cls,mat, n): 
        if (cls.determinantOfMatrix(mat, n) != 0): 
            return True
        else: 
            return False

    @classmethod
    def multiply_and_convert(cls,key,message):
        
        res_num = [[0 for x in range(len(message[0]))] for y in range(len(key))]
        
        for i in range(len(key)): 
            for j in range(len(message[0])):
                for k in range(len(message)): 
                    # resulted number matrix
                    res_num[i][j]+=key[i][k] * message[k][j]

        res_alpha = [['' for x in range(len(message[0]))] for y in range(len(key))]
        
        for i in range(len(key)):
            for j in range(len(message[0])):
                # resultant alphabet matrix
                res_alpha[i][j]+=chr((res_num[i][j]%26)+97)
                
        return(res_alpha)

    # implementing all logic and calling function
    @classmethod
    def hill_cipher(cls,plain_text):
        n = 4
        s = "5668 2228 6628 2367"
        key=cls.generate_key(n,s)
            
        message=cls.message_matrix(plain_text,n)
        final_message=''
        for i in message:
            sub=cls.multiply_and_convert(key,i)
            for j in sub:
                for k in j:
                    final_message+=k
        return final_message
    # print(hill_cipher("I am Bored"))
