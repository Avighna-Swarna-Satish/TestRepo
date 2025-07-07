def annotate(minefield):
    s1=len(minefield)
    s2=len(minefield[0][0])
    count=0
    o=[]
    op=[]
    st=""
    for i in range(0,s):
        for j in range(0,5):
            if minefield[i][j]==" " or minefield[i][j]=="space" or minefield[i][j]=="space ":
                if i==0 and j==0:
                    
                    case a:
                        if minefield[i][j+1]=="*":
                            count=count+1
                    case b:
                        if minefield[i+1][j]=="*":
                            count=count+1
                    case c:
                        if minefield[i+1][j+1]:
                            count=count+1
                        break
                elif i==0 and j!=0:
                    case a:
                        if minefield[i][j+1]=="*":
                            count=count+1
                    case b:
                        if minefield[i+1][j]=="*":
                            count=count+1
                    case c:
                        if minefield[i+1][j-1]=="*":
                            count=count=count+1
                    case d:
                        if minefield[i][j-1]=="*":
                            count=count+1
                    case e:
                        if minefield[i+1][j+1]=="*":
                            count=count+1
                        break
                elif i==0 and j==4:
                    case a:
                        if minefield[i+1][j]=="*":
                            count=count+1
                    case b:
                        if minefield[i+1][j-1]=="*":
                            count=count+1
                    case c:
                        if minefiled[i][j-1]:
                            count=count+1
                        break
                elif (i!=0 and i!=s-1) and j!=0:
                    case a:
                        if minefield[i][j-1]=="*":
                            count=count+1
                    case b:
                        if minefield[i][j+1]=="*":
                            count=count+1
                    case c:
                        if minefield[i-1][j]=="*":
                            count=count+1
                    case d:
                        if minefield[i-1][j-1]=="*":
                            count=count+1
                    case e:
                        if minefield[i-1][j+1]=="*":
                            count=count+1
                    case f:
                        if minefield[i+1][j]=="*":
                            count=count+1
                    case g:
                        if minefield[i+1][j-1]=="*":
                            count=count+1
                    case h:
                        if minefield[i+1,j+1]=="*":
                            count=count+1
                        break
                elif i==s-1 and j==0:
                    case a:
                        if minefield[i-1][j]=="*":
                            count=count+1
                    case b:
                        if minefield[i][j+1]=="*":
                            count=count+1
                    case c:
                        if minefield[i-1][j+1]=="*":
                            count=count+1
                        break
                elif i==s-1 and j!=0:
                    case a
                        if minefield[i][j-1]=="*":
                            count=count+1
                    case b:
                        if minefield[i][j+1]=="*":
                            count=count+1
                    case c:
                        if minefield[i-1][j]=="*":
                            count=count+1
                    case d:
                        if minefield[i-1][j-1]:
                            count=count+1
                    case e:
                        if minefield[i-1][j+1]=="*":
                            count=count+1
                        break
                else:
                    case a:
                        if minefield[i][j-1]:
                            count=count+1
                    case b:
                        if minefield[i-1][j]:
                            count=count+1
                    case c:
                        if minefield[i-1][j-1]:
                            count=count+1
                    break
            for l in o:
                if l==0:
                    st=st+" "
                else:
                    st=st+str(count)
        op=op+[st]
    return op

print(annotate(["***","* *","***"]))

            
