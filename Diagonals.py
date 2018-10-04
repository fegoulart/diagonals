
#se a celula da esquerda for 1, nao pode 2
#se a celula da esquerda for 2, nao pode 1
#se a celula da diagonal esquerda baixa for 1, nao pode ser 1
#se a celula de baixo for 1, nao pode ser 2
#se a celula de baixo for 2, nao pode ser 1
#se a celula da diagonal direita baixo for 2 nao pode ser 2


import time
import sys
sys.setrecursionlimit(1000000000)


def can_be_extended_to_solution(perm,n,target):

    i = len(perm) - 1

    if len(perm) > pow(n,2):
        return False

    isFirstColumn = False
    isFirstRow = False
    isLastColumn = False

    if (i % n == 0):
        isFirstColumn = True

    if (i < n):
        isFirstRow = True

    if (i % n  == n - 1):
        isLastColumn = True

    #verifica esquerda

    #se nao for primeira coluna
    if isFirstColumn == False:
        if (perm[i-1] == 1 and perm[i] == 2):
            return False
        if perm[i - 1] == 2 and perm[i] == 1:
            return False


    #verifica embaixo
    #se nao for primeira linha
    if isFirstRow == False:
        if perm[i - n] == 1 and perm[i] == 2:
             return False
        if perm[i - n] == 2 and perm[i] == 1:
            return False

    #verifica diagonal embaixo esquerda
    #se nao for primeira linha e se nao for primeira coluna
    if isFirstRow == False and isFirstColumn == False:
        if (perm[i-1-n] == 1 and perm[i] == 1):
            return False


    #verifica diagonal direita embaixo
    #se nao for primeira linha e se nao for ultima coluna
    if isFirstRow == False and isLastColumn == False:
        if perm[i + 1 - n] == 2 and perm[i] == 2:
            return False

    #verifica se esta completando o array e nao tem o numero de diagonais necessario
    total = pow(n,2)
    following_cells = total - len(perm)

    if len(perm) == total:
        print(perm)

    cont = 0
    for j in range(len(perm)):
        if perm[j] != 3:
            cont = cont + 1
    if (target > following_cells + cont):
        return False

    return True

def extend(perm,n, target):

    if len(perm) == pow(n,2):
        print("resposta")
        print(perm)
        print "time elapsed: {:.2f}s".format(time.time() - start_time)
        # solutions.append(perm)
        #solutions = solutions + 1
        #print(solutions)
        exit()

    for k in range(1, 4):

        perm.append(k)

        if can_be_extended_to_solution(perm, n, target):
            # print('Vai recursar. perm = ')
            # print(perm)
            # print (' n= ')
            # print (n)
            extend(perm, n, target)

        perm.pop()






def extend_old(perm, n):

    if len(perm) == pow(n, 2):

        print(perm)

        cont = 0
        for j in range(pow(n,2)):
            if perm[j] != 3:
                cont = cont + 1
        if (cont >= 16 ):
            print (perm)
            print "time elapsed: {:.2f}s".format(time.time() - start_time)
            exit()


        #aux = pow(n, 2) - 1

        #if tree_pointer == aux:
        #    print('Nao ha solucao')
        #    exit()

        while (aux >= 0):

            if aux == tree_pointer:
                if (perm[aux]==1):
                    perm[aux]=2
                    if can_be_extended_to_solution(perm, n):
                        cont = 0
                        if len(perm) == range(pow(n,2)):
                            for j in range(pow(n, 2)):
                                if perm[j] != 3:
                                    cont = cont + 1
                            if (cont >= 16):
                                print (perm)
                                print "time elapsed: {:.2f}s".format(time.time() - start_time)
                                exit()
                        aux = -1
                    else:
                        perm[aux] = 3
                        if can_be_extended_to_solution(perm, n):
                            cont = 0
                            if len(perm) == range(pow(n, 2)):
                                for j in range(pow(n, 2)):
                                    if perm[j] != 3:
                                        cont = cont + 1
                                if (cont >= 16):
                                    print (perm)
                                    print "time elapsed: {:.2f}s".format(time.time() - start_time)
                                    exit()
                            aux = -1
                            tree_pointer = tree_pointer + 1
                else:
                    if perm[aux]==2:
                        perm[aux]=3
                        if can_be_extended_to_solution(perm, n):
                            cont = 0
                            if len(perm) == range(pow(n, 2)):
                                for j in range(pow(n, 2)):
                                    if perm[j] != 3:
                                        cont = cont + 1
                                if (cont >= 16):
                                    print (perm)
                                    print "time elapsed: {:.2f}s".format(time.time() - start_time)
                                    exit()
                            tree_pointer = tree_pointer + 1

                aux = - 1
            else:
                if perm[aux] == 3:
                    perm.pop()
                else:
                    if perm[aux] == 1:
                        perm[aux] = 2
                        if can_be_extended_to_solution(perm, n):
                            cont = 0
                            if len(perm) == range(pow(n,2)):
                                for j in range(pow(n, 2)):
                                    if perm[j] != 3:
                                        cont = cont + 1
                                if (cont >= 16):
                                    print (perm)
                                    print "time elapsed: {:.2f}s".format(time.time() - start_time)
                                    exit()
                            aux = 0
                        else:
                            perm[aux] = 3
                            if can_be_extended_to_solution(perm, n):
                                cont = 0
                                if len(perm) == range(pow(n, 2)):
                                    for j in range(pow(n, 2)):
                                        if perm[j] != 3:
                                            cont = cont + 1
                                    if (cont >= 16):
                                        print (perm)
                                        print "time elapsed: {:.2f}s".format(time.time() - start_time)
                                        exit()
                                aux = 0
                            else:
                                perm.pop()
                    else:
                        perm[aux] = 3
                        if can_be_extended_to_solution(perm, n):
                            cont = 0
                            if len(perm) == range(pow(n, 2)):
                                for j in range(pow(n, 2)):
                                    if perm[j] != 3:
                                        cont = cont + 1
                                if (cont >= 16):
                                    print (perm)
                                    print "time elapsed: {:.2f}s".format(time.time() - start_time)
                                    exit()
                            aux = 0
                        else:
                            perm.pop()
                aux = aux - 1


    for k in range(1,4):

        if (len(perm) < pow(n,2)):
            perm.append(k)

            if can_be_extended_to_solution(perm,n):
                extend(perm,n)
            else:
                perm.pop()
        else:
            extend(perm,n)

start_time = time.time()

extend(perm = [], n = 5, target = 16 )